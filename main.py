from scrape import get_headlines
from analyze import analyze_sentiment
import matplotlib.pyplot as plt
import os

if __name__ == "__main__":
    # Step 1: Get headlines
    headlines = get_headlines()
    print(f"\n📰 Total headlines scraped: {len(headlines)}\n")

    for i, h in enumerate(headlines, 1):
        print(f"{i}. {h}")

    # Step 2: Analyze sentiment
    results, analyzed = analyze_sentiment(headlines)

    # Step 3: Show summary
    print("\n📊 Sentiment Summary:")
    for sentiment, count in results.items():
        print(f"{sentiment.title()}: {count}")

    # Step 4: Print headline + sentiment pairs
    print("\n📋 Headline Sentiments:")
    for headline, sentiment in analyzed:
        print(f"[{sentiment.upper()}] {headline}")

    # Step 5: Save results to a file
    os.makedirs("output", exist_ok=True)

    with open("output/headlines_sentiment.txt", "w", encoding="utf-8") as f:
        for headline, sentiment in analyzed:
            f.write(f"[{sentiment.upper()}] {headline}\n")

    # Step 6: Save pie chart
    labels = list(results.keys())
    sizes = list(results.values())
    colors = ['green', 'red', 'grey']

    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=140)
    plt.title("Sentiment Distribution of News Headlines")
    plt.axis('equal')

    # Save pie chart to file
    plt.savefig("output/pie_chart.png", bbox_inches='tight')
    plt.show()
