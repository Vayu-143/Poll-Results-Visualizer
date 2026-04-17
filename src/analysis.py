import pandas as pd

def analyze_data(df):
    print("📊 Performing analysis...")

    results = {}

    # Overall counts
    counts = df["Preference"].value_counts()
    percent = (counts / len(df)) * 100

    # Region-wise
    region = pd.crosstab(df["Region"], df["Preference"])

    # Age-wise
    age = pd.crosstab(df["Age_Group"], df["Preference"])

    results["counts"] = counts
    results["percent"] = percent
    results["region"] = region
    results["age"] = age

    return results