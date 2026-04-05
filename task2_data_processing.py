import json
import pandas as pd
import os

def main():
    # Load JSON file
    files = [f for f in os.listdir("data") 
             if f.startswith("trends_") and f.endswith(".json")]
    print (files)

    if not files:
        print("No JSON file found.")
        return
    latest_file = sorted(files)[-1]
    print(latest_file)

    with open(os.path.join("data", latest_file), "r") as f:
        stories = json.load(f)

    # Convert to DataFrame
    df = pd.DataFrame(stories)

    # Clean data
    df.fillna({"score": 0, "num_comments": 0, "author": "unknown"}, inplace=True)

    # Save to CSV
    output_file = "data/trends_clean.csv"
    df.to_csv(output_file, index=False)
    print(f"Saved cleaned data to {output_file}")

if __name__ == "__main__":
    main()
