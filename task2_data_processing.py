import json
import pandas as pd
#import os
from pathlib import Path

def main():
    # Load JSON file
  
    data_folder = Path("F:/Learning/miniproject/data")
    file_path = data_folder / "trends_20260405.json"
  
    with open(file_path, "r") as f: 

        stories = json.load(f)

    # Convert to DataFrame
    df = pd.DataFrame(stories)

  # Step 3: Cleaning process
    # Remove duplicates by post_id
    df.drop_duplicates(subset="post_id", inplace=True)
    print(f"After removing duplicates: {len(df)}")
    
    # Drop rows where post_id, title, or score is missing
    df.dropna(subset=["post_id", "title", "score"], inplace=True)
    print(f"After removing nulls: {len(df)}")
    
    # Ensure score and num_comments are integers
    df["score"] = df["score"].astype(int)
    df["num_comments"] = df["num_comments"].astype(int)

    # Remove low-quality stories (score < 5)
    df = df[df["score"] >= 5]
    print(f"After removing low scores: {len(df)}")

    # Strip whitespace from titles
    df["title"] = df["title"].str.strip()

    # Step 4: Save cleaned data
    output_file = "data/trends_clean.csv"
    df.to_csv(output_file, index=False)

    # Step 5: Print summary
    print(f"\nSaved {len(df)} rows to {output_file}\n")

    # Step 5: Print category counts
    category_counts = df["category"].value_counts()
    print("Stories per category:")
    for cat, count in category_counts.items():
        print(f"  {cat:<15} {count}")

if __name__ == "__main__":
    main()
