from src.data_generator import generate_data
from src.data_cleaning import clean_data
from src.analysis import analyze_data
from src.visualization import create_visualizations
from src.insights import generate_insights

def main():
    print("🚀 Starting Poll Results Visualizer...\n")

    # Step 1: Generate or Load Data
    df = generate_data()

    # Step 2: Clean Data
    df = clean_data(df)

    # Step 3: Analyze Data
    results = analyze_data(df)

    # Step 4: Create Visualizations
    create_visualizations(df, results)

    # Step 5: Generate Insights
    generate_insights(results)

    print("\n✅ Project Completed! Check outputs folder.")

if __name__ == "__main__":
    main()