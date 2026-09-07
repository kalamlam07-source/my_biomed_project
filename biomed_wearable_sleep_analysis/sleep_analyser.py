import pandas as pd
import numpy as np

# 1. Simulate 8 Hours of Continuous Wearable Sleep Data (480 minutes of tracking)
np.random.seed(88)
minutes = np.arange(0, 480) # 0 to 479 minutes (11:00 PM to 7:00 AM)

# Baseline daytime resting heart rate is 70 bpm
# As the patient falls into deep sleep, the heart rate naturally dips down
base_hr = 68 - 12 * np.sin(np.pi * minutes / 480) 

# Inject normal physiological heart rate fluctuations (noise)
heart_rates = base_hr + np.random.normal(0, 2.5, len(minutes))

# Force a severe "Heart Rate Drop & Spike" around minute 200 (Simulating a temporary breathing block/apnea event)
heart_rates[195:205] -= 18  # Dangerous sudden drop
heart_rates[205:212] += 25  # Rebound sudden panic spike

# Ensure heart rates stay in a realistic human boundary
heart_rates = np.clip(heart_rates, 35, 120)

# Create the Wearable Smart Watch Big Data Table
df_sleep = pd.DataFrame({
    "Sleep_Minute": minutes,
    "Heart_Rate_BPM": heart_rates
})
df_sleep.to_csv("wearable_sleep_time_series.csv", index=False)

print("=" * 65)
print("⌚ BIOMEDICAL WEARABLE LAB: CONTINUOUS SLEEP ANALYSER ⌚")
print("=" * 65)
print(f"📊 Successfully loaded {len(df_sleep)} minutes of continuous continuous physiological data.\n")

# 2. Automated Clinical Screening Filters
# Rule: A baseline deep sleep heart rate should hover between 45 and 55 BPM.
# Anything dropped sharply below 42 BPM is flagged as a potential Apnea/Hypoxia anomaly!

average_sleep_hr = df_sleep["Heart_Rate_BPM"].mean()
min_sleep_hr = df_sleep["Heart_Rate_BPM"].min()

print("📋 Sleep Physiology Summary Statistics:")
print(f"   - Average Overnight Heart Rate: {average_sleep_hr:.1f} BPM")
print(f"   - Absolute Minimum Heart Rate Detected: {min_sleep_hr:.1f} BPM\n")

# 3. Time-Series Event Detection (Searching for anomalies)
anomalies = df_sleep[df_sleep["Heart_Rate_BPM"] < 42.0]

print("-" * 65)
print("🚨 Automated Time-Series Cardiac Anomaly Scan:")
if not anomalies.empty:
    anomaly_duration = len(anomalies)
    peak_anomaly_time = anomalies.loc[anomalies["Heart_Rate_BPM"].idxmin(), "Sleep_Minute"]
    
    print(f"   ⚠️ WARNING: Abnormal Midnight Heart Drop Detected!")
    print(f"   - Total Duration of Hypoxia/Drop: {anomaly_duration} minutes")
    print(f"   - Peak Panic Event Occurred at: Minute {peak_anomaly_time} after sleep onset.")
    print("\n🚨 【CLINICAL CARDIOVASCULAR CONCLUSION】:")
    print("   Patient exhibits signs of severe Nocturnal Bradycardia/Sleep Apnea.")
    print("   The cardiac dropping threshold was violated significantly around the 3.5-hour mark.")
    print("   RECOMMENDATION: Referral to a full overnight hospital Sleep Lab (Polysomnography).")
else:
    print("   ✅ Sleep pattern is stable. Cardiac dipping is within safe physiological limits.")
print("=" * 65)
