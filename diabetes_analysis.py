import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the Diabetes Dataset
try:
    df = pd.read_csv("diabetes_dataset00.csv")
    print("✅ Diabetes data loaded successfully!")
    print(f"Dataset includes {df.shape[0]} patients and {df.shape[1]} metrics.")
    
    # 2. Set style
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(10, 6))

    # 3. Analyze Blood Glucose levels vs Diabetes Outcome
    # Outcome: 1 = Has Diabetes, 0 = Healthy
    if 'Blood Glucose Levels' in df.columns and 'Target' in df.columns:
        sns.histplot(data=df, x="Blood Glucose Levels", hue="Target", kde=True, multiple="stack", palette="rocket", alpha=0.7)
        
        plt.title("Blood Glucose Distribution by Diabetes Status", fontsize=14, fontweight='bold', pad=15)
        plt.xlabel("Plasma Glucose Concentration", fontsize=12)
        plt.ylabel("Patient Count", fontsize=12)
        
        plt.tight_layout()
        plt.savefig("glucose_distribution_plot.png", dpi=300) # Saves the graph automatically!
        plt.show()
    else:
        print("⚠️ Column names might be different. Here are the columns found:")
        print(df.columns.tolist())

except FileNotFoundError:
    print("❌ Cannot find diabetes.csv. Please check the file name!")
