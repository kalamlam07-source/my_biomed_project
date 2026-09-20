import pandas as pd
import numpy as np

# 1. Simulate a Hospital EHR Database (1,000 Patient Electronic Health Records)
np.random.seed(99)
patient_ids = [f"PATIENT_{i:04d}" for i in range(1, 1001)]

# Generate clinical physiological data
ages = np.random.randint(18, 90, size=1000)
systolic_bp = np.random.normal(125, 15, size=1000) # Blood pressure
cholesterol = np.random.normal(200, 35, size=1000)

# Simulate Medication Tracking (Some patients are on our newly discovered approved drug)
medication_status = np.random.choice(
    ["New_Approved_Drug", "Standard_Care", "No_Medication"], 
    size=1000, 
    p=[0.3, 0.4, 0.3]
)

# Compile into a Hospital Master Database
df_hospital = pd.DataFrame({
    "Patient_ID": patient_ids,
    "Age": ages,
    "Systolic_BP": np.round(systolic_bp, 1),
    "Cholesterol_mgDL": np.round(cholesterol, 1),
    "Current_Medication": medication_status
})

# Inject real-world missing data (simulating a nurse forgetting to log blood pressure)
df_hospital.loc[np.random.choice(1000, 15, replace=False), "Systolic_BP"] = np.nan
df_hospital.to_csv("hospital_raw_ehr.csv", index=False)

print("=" * 70)
print("🏥 CLINICAL INFORMATICS LAB: HOSPITAL EHR BIG DATA MINING 🏥")
print("=" * 70)
print(f"📊 Successfully loaded {len(df_hospital)} raw electronic health records from hospital server.\n")

# 2. Data Cleaning: Drop corrupted rows missing vital blood pressure records
initial_count = len(df_hospital)
df_clean = df_hospital.dropna(subset=["Systolic_BP"]).copy()
dropped_count = initial_count - len(df_clean)
print(f"🧹 Data Cleaning: Dropped {dropped_count} corrupted patient files missing vital signs.\n")

# 3. Clinical Risk Index Calculation
# Formula: Cardiovascular Risk = (Age * 0.4) + (Systolic_BP * 0.3) + (Cholesterol / 10)
df_clean["CV_Risk_Score"] = (df_clean["Age"] * 0.4) + (df_clean["Systolic_BP"] * 0.3) + (df_clean["Cholesterol_mgDL"] / 10)

# 4. Extract High-Risk ICU Red Flags
# Patients with a Risk Score > 90 are flagged for emergency specialist intervention
high_risk_patients = df_clean[df_clean["CV_Risk_Score"] > 92.0]
high_risk_patients.to_csv("emergency_icu_alert_list.csv", index=False)

# 5. Evaluate Medication Effectiveness (Is our approved drug working?)
med_analysis = df_clean.groupby("Current_Medication")["CV_Risk_Score"].mean()

print("📈 Group Analytics: Average Cardiovascular Risk by Medication Group:")
print("-" * 70)
for med, score in med_analysis.items():
    print(f"  💊 {med:<20} -> Average Clinical Risk Score: {score:.2f}")
print("-" * 70)

print(f"\n🚨 【CRITICAL EPIDEMIOLOGICAL FINDING】:")
print(f"   Identified 【{len(high_risk_patients)}】 patients currently in the Critical Cardiovascular Danger Zone.")
print(f"   Emergency alert roster successfully generated and exported to emergency_icu_alert_list.csv")
print("=" * 70)
