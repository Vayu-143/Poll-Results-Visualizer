import pandas as pd
import numpy as np

def generate_data():
    np.random.seed(42)
    n = 1000

    # Add bias (realistic simulation)
    regions = np.random.choice(["North", "South", "East", "West"], n)

    preferences = []
    for r in regions:
        if r == "North":
            preferences.append(np.random.choice(["Product A", "Product B"], p=[0.6, 0.4]))
        elif r == "South":
            preferences.append(np.random.choice(["Product B", "Product C"], p=[0.7, 0.3]))
        elif r == "East":
            preferences.append(np.random.choice(["Product A", "Product C"], p=[0.5, 0.5]))
        else:
            preferences.append(np.random.choice(["Product A", "Product B", "Product C"]))

    df = pd.DataFrame({
        "Respondent_ID": range(1, n+1),
        "Region": regions,
        "Age_Group": np.random.choice(["18-25", "26-35", "36-50", "50+"], n),
        "Preference": preferences,
        "Date": pd.date_range(start="2024-01-01", periods=n)
    })

    df.to_csv("data/poll_data.csv", index=False)
    print("📁 Synthetic dataset created!")

    return df