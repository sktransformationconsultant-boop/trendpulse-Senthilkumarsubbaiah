import pandas as pd
import matplotlib.pyplot as plt
import os

def main():
    # Step 1 — Setup
    if not os.path.exists("data/trends_analysed.csv"):
        print("No analysed CSV file found. Run task3_analysis.py first.")
        return

    df = pd.read_csv("data/trends_analysed.csv")

    if not os.path.exists("outputs"):
        os.makedirs("outputs")

    # Step 2 — Chart 1: Top 10 Stories by Score
    top10 = df.sort_values("score", ascending=False).head(10)
        # Truncate titles inline (simple loop)
    titles = []
    for t in top10["title"]:
        if len(t) <= 50:
            titles.append(t)
        else:
            titles.append(t[:50] + "...")

    plt.figure(figsize=(10, 6))
    plt.barh(titles, top10["score"], color="skyblue")
    plt.xlabel("Score")
    plt.ylabel("Story Title")
    plt.title("Top 10 Stories by Score")
    plt.gca().invert_yaxis()  # highest score at top
    plt.tight_layout()
    plt.savefig("outputs/chart1_top_stories.png")
    plt.show()
    plt.close()

      # Step 3 — Chart 2: Stories per Category
    category_counts = df["category"].value_counts()

    plt.figure(figsize=(8, 6))
    plt.bar(category_counts.index, category_counts.values, color=plt.cm.tab10.colors[:len(category_counts)])
    plt.xlabel("Category")
    plt.ylabel("Number of Stories")
    plt.title("Stories per Category")
    plt.tight_layout()
    plt.savefig("outputs/chart2_categories.png")
    plt.show()
    plt.close()


   # Step 4 — Chart 3: Score vs Comments
    plt.figure(figsize=(8, 6))
    colors = df["is_popular"].map({True: "green", False: "red"})
    plt.scatter(df["score"], df["num_comments"], c=colors, alpha=0.6)
    plt.xlabel("Score")
    plt.ylabel("Number of Comments")
    plt.title("Score vs Comments")
    plt.legend(handles=[
        plt.Line2D([0], [0], marker='o', color='w', label='Popular', markerfacecolor='green', markersize=8),
        plt.Line2D([0], [0], marker='o', color='w', label='Not Popular', markerfacecolor='red', markersize=8)
    ])
    plt.tight_layout()
    plt.savefig("outputs/chart3_scatter.png")
    plt.show()
    plt.close()

    # Bonus — Dashboard
    fig, axes = plt.subplots(1, 3, figsize=(20, 6))

    # Dashboard Chart 1
    axes[0].barh(titles, top10["score"], color="skyblue")
    axes[0].set_xlabel("Score")
    axes[0].set_ylabel("Story Title")
    axes[0].set_title("Top 10 Stories by Score")
    axes[0].invert_yaxis()

    # Dashboard Chart 2
    axes[1].bar(category_counts.index, category_counts.values, color=plt.cm.tab10.colors)
    axes[1].set_xlabel("Category")
    axes[1].set_ylabel("Number of Stories")
    axes[1].set_title("Stories per Category")

    # Dashboard Chart 3
    axes[2].scatter(df["score"], df["num_comments"], c=colors, alpha=0.6)
    axes[2].set_xlabel("Score")
    axes[2].set_ylabel("Number of Comments")
    axes[2].set_title("Score vs Comments")

    fig.suptitle("TrendPulse Dashboard", fontsize=16)
    plt.tight_layout()
    plt.savefig("outputs/dashboard.png")
    plt.show()
    plt.close()

    print("Charts saved in 'outputs/' folder:")
    print(" chart1_top_stories.png")
    print(" chart2_categories.png")
    print(" chart3_scatter.png")
    print(" dashboard.png")

if __name__ == "__main__":
    main()
