import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load your Cancer Dataset
try:
    df = pd.read_csv("Cancer_Data.csv")
    print("✅ Data loaded successfully!")
    
    # 2. Set academic plot style
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(10, 6))

    # 3. Create a chart of tumor radius size
    # Note: Kaggle cancer sets usually use 'radius_mean' and 'diagnosis'
    # If your specific dataset column names are slightly different, it will let us know!
    if 'radius_mean' in df.columns and 'diagnosis' in df.columns:
        sns.histplot(data=df, x="radius_mean", hue="diagnosis", kde=True, multiple="stack", palette="rocket" , alpha=0.7)
        plt.title("Tumor Size Distribution by Cancer Diagnosis", fontsize=14, fontweight='bold', pad=15)
        plt.xlabel("Mean Radius of Tumor Cells", fontsize=12)
        plt.ylabel("Patient Count", fontsize=12)
        plt.tight_layout()
        plt.savefig("cancer_tumor_distribution.png", dpi=300)
        plt.show()
    else:
        print("\n--- First 5 rows of your dataset ---")
        print(df.head())

except FileNotFoundError:
    print("❌ Cannot find Cancer_Data.csv. Please check the file name!")
