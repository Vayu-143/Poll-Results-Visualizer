import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

def create_visualizations(df, results):
    print("📈 Creating visualizations...")

    counts = results["counts"]
    region = results["region"]
    age = results["age"]

    # Bar Chart
    plt.figure(figsize=(6,4))
    sns.barplot(x=counts.index, y=counts.values)
    plt.title("Overall Preference Count")
    plt.xlabel("Product")
    plt.ylabel("Votes")
    plt.tight_layout()
    plt.savefig("outputs/bar_chart.png")
    plt.close()

    # Pie Chart
    plt.figure(figsize=(6,6))
    counts.plot.pie(autopct='%1.1f%%')
    plt.title("Preference Share")
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig("outputs/pie_chart.png")
    plt.close()

    # Region Chart
    region.plot(kind="bar", stacked=True, figsize=(7,5))
    plt.title("Region-wise Preferences")
    plt.xlabel("Region")
    plt.ylabel("Votes")
    plt.tight_layout()
    plt.savefig("outputs/region_chart.png")
    plt.close()

    # Age Chart
    age.plot(kind="bar", stacked=True, figsize=(7,5))
    plt.title("Age-wise Preferences")
    plt.xlabel("Age Group")
    plt.ylabel("Votes")
    plt.tight_layout()
    plt.savefig("outputs/age_chart.png")
    plt.close()