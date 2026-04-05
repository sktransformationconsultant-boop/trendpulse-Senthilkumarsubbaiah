import pandas as pd
import numpy as np
import os

def main():
    # Step 1 — Load and Explore
    if not os.path.exists("data/trends_clean.csv"):
        print("No cleaned CSV file found. Run task2_data_processing.py first.")
        return

    
    df = pd.read_csv("data/trends_clean.csv")

    print(f"Loaded data: {df.shape}\n")
    print("First 5 rows:")
    print(df.head(), "\n")

    avg_score = df["score"].mean()
    avg_comments = df["num_comments"].mean()
    print(f"Average score   : {avg_score:.0f}")
    print(f"Average comments: {avg_comments:.0f}\n")

    # Step 2 — Basic Analysis with NumPy
    scores = df["score"].to_numpy()

    print("--- NumPy Stats ---")
    print(f"Mean score   : {np.mean(scores):.0f}")
    print(f"Median score : {np.median(scores):.0f}")
    print(f"Std deviation: {np.std(scores):.0f}")
    print(f"Max score    : {np.max(scores):.0f}")
    print(f"Min score    : {np.min(scores):.0f}\n")

    # Category with most stories
    category_counts = df["category"].value_counts()
    category_counts = df["category"].value_counts()
    top_category = category_counts.idxmax()
    print(f"Most stories in: {top_category} ({category_counts.max()} stories)\n")

    # Story with most comments
    most_commented = df.loc[df["num_comments"].idxmax()]
    print(f'Most commented story: "{most_commented["title"]}"  — {most_commented["num_comments"]} comments\n')

    # Step 3 — Add New Columns
    df["engagement"] = df["num_comments"] / (df["score"] + 1)
    df["is_popular"] = df["score"] > avg_score

    # Step 4 — Save the Result
    output_file = "data/trends_analysed.csv"
    df.to_csv(output_file, index=False)
    print(f"Saved to {output_file}")

    # check the additional columns are added
    print(f"Loaded data: {df.shape}\n")
          

if __name__ == "__main__":
    main()
