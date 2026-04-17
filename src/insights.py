def generate_insights(results):
    print("\n🧠 SMART INSIGHTS\n")

    counts = results["counts"]
    percent = results["percent"]
    region = results["region"]

    top_product = counts.idxmax()
    least_product = counts.idxmin()

    print(f"🏆 Most Preferred Product: {top_product}")
    print(f"❌ Least Preferred Product: {least_product}")

    print("\n📊 Percentage Distribution:")
    print(percent.round(2))

    print("\n🌍 Region-wise Leaders:")
    for r in region.index:
        leader = region.loc[r].idxmax()
        print(f"{r}: {leader}")