import requests
import time
import datetime
import os
import json

# Headers for API requests
HEADERS = {"User-Agent": "TrendPulse/1.0"}

# Category keywords
CATEGORY_KEYWORDS = {
    "technology": ["AI", "software", "tech", "code", "computer", "data", "cloud", "API", "GPU", "LLM"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["NFL", "NBA", "FIFA", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "NASA", "genome"],
    "entertainment": ["movie", "film", "music", "Netflix", "game", "book", "show", "award", "streaming"]
}

def fetch_top_story_ids(limit=500):
    """Fetch top story IDs from HackerNews"""
    try:
        response = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json", headers=HEADERS)
        response.raise_for_status()
        return response.json()[:limit]
    except Exception as e:
        print(f"Error fetching top stories: {e}")
        return []

def fetch_story_details(story_id):
    """Fetch details of a single story"""
    try:
        url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Failed to fetch story {story_id}: {e}")
        return None

def assign_category(title):
    """Assign category based on keywords in title"""
    if not title:
        return None
    title_lower = title.lower()
    for category, keywords in CATEGORY_KEYWORDS.items():
        for kw in keywords:
            if kw.lower() in title_lower:
                return category
    return None

def main():
    # Step 1: Fetch top story IDs
    story_ids = fetch_top_story_ids()
    print(f"Fetched {len(story_ids)} story IDs.")

    collected_stories = []
    # Step 2: Loop through categories
    for category in CATEGORY_KEYWORDS.keys():
        count = 0
        for story_id in story_ids:
            if count >= 25:
                break
            story = fetch_story_details(story_id)
            if not story or "title" not in story:
                continue

            assigned_category = assign_category(story.get("title"))
            if assigned_category == category:
                collected_stories.append({
                    "post_id": story.get("id"),
                    "title": story.get("title"),
                    "category": assigned_category,
                    "score": story.get("score", 0),
                    "num_comments": story.get("descendants", 0),
                    "author": story.get("by"),
                    "collected_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                })
                count += 1

        print(f"Collected {count} stories for category '{category}'.")
        time.sleep(2)  # Sleep once per category

    # Step 3: Save to JSON file
    if not os.path.exists("data"):
        os.makedirs("data")

    filename = f"data/trends_{datetime.datetime.now().strftime('%Y%m%d')}.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(collected_stories, f, indent=4)

    print(f"Collected {len(collected_stories)} stories. Saved to {filename}")

if __name__ == "__main__":
    main()
