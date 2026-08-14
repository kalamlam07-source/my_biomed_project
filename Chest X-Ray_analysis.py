import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. 讀取胸部 X 光片的元數據
try:
    # 根據截圖，你的檔名叫做 Chest_xray_Corona_Metadata.csv
    df = pd.read_csv("Chest_xray_Corona_Metadata.csv")
    print("✅ 胸部 X 光元數據載入成功！")
    print(f"總共包含 {df.shape[0]} 張 X 光片記錄。")
    print("\n欄位名稱如下：", df.columns.tolist())
    
    # 2. 設定學術圖表風格
    sns.set_theme(style="whitegrid")
    
    # 建立一個左右並排的畫布 (一個看大分類，一個看具體病毒分類)
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # 3. 圖表 A：繪製 Normal vs Pnemonia 的大分類數量
    if 'Label' in df.columns:
        sns.countplot(data=df, x="Label", ax=axes[0], palette="Set2")
        axes[0].set_title("Distribution of X-Ray Labels (Normal vs Disease)", fontsize=12, fontweight='bold')
        axes[0].set_xlabel("Clinical Diagnosis")
        axes[0].set_ylabel("Image Count")

    # 4. 圖表 B：繪製更細的病毒種類 (Label_2_Virus_category) 數量
    # 修正名稱以防有空格，這裡配合你截圖中的 Label_2_Virus_category
    if 'Label_2_Virus_category' in df.columns:
        # 使用 countplot 自動統計各類病毒的 X 光片數量
        sns.countplot(data=df, y="Label_2_Virus_category", ax=axes[1], palette="flare", order=df['Label_2_Virus_category'].value_counts().index)
        axes[1].set_title("Detailed Virus Categories Count", fontsize=12, fontweight='bold')
        axes[1].set_xlabel("Image Count")
        axes[1].set_ylabel("Virus/Bacteria Type")

    # 5. 優化佈局並自動儲存
    plt.tight_layout()
    plt.savefig("xray_metadata_distribution.png", dpi=300)
    print("📸 論文級長條統計圖已自動儲存為 xray_metadata_distribution.png！")
    plt.show()

except FileNotFoundError:
    print("❌ 找不到 Chest_xray_Corona_Metadata.csv，請檢查檔案名稱是否完全一致！")
