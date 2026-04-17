def clean_data(df):
    print("🧹 Cleaning data...")

    df = df.dropna()

    df["Region"] = df["Region"].str.strip()
    df["Preference"] = df["Preference"].str.strip()
    df["Age_Group"] = df["Age_Group"].str.strip()

    return df