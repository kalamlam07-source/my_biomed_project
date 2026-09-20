# 🏥 Clinical Informatics Lab: Hospital EHR Big Data Mining

This repository simulates a clinical research pipeline for querying, cleaning, and evaluating Electronic Health Records (EHR) from a hospital database of 1,000 patients.

## 🔬 How the Code Works (Pipeline Breakdown)

1. **Database Simulation (`hospital_raw_ehr.csv`)**
   - Synthesizes 1,000 unique patient cards tracking vital physiological metrics including Age, Systolic Blood Pressure (BP), and Cholesterol levels alongside current medication brackets.
   - Intentionally injects real-world data corruption (missing vital entries) to test pipeline resiliency.

2. **Automated Data Cleaning (`.dropna()`)**
   - Implements a programmatic filter that automatically discards corrupted patient rows lacking critical Systolic BP entries, throwing away 15 incomplete files to ensure clinical data integrity.

3. **Multi-Parametric Risk Scoring & ICU Profiling**
   - Evaluates a custom epidemiological equation: 
     \[\text{Cardiovascular Risk} = (\text{Age} \times 0.4) + (\text{Systolic BP} \times 0.3) + \left(\frac{\text{Cholesterol}}{10}\right)\]
   - Scans the entire cleaned dataset to flag patients with a score higher than 92.0, automatically generating an isolated `emergency_icu_alert_list.csv` capturing 121 critical danger-zone cases.

4. **Comparative Group Analytics (`.groupby()`)**
   - Aggregates risk patterns to evaluate whether the newly approved target compound demonstrates statistical efficacy over standard-of-care treatments in lowering overall cardiovascular risk scores.

