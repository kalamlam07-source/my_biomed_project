import pandas as pd

# 1. An expanded virtual library of advanced chemical candidates against a viral enzyme
# Each string represents a unique molecular structure mapped out via text
advanced_chemical_library = {
    "Candidate_01 (Remdesivir-like)": "C1=CC=C2C(=C1)C(=NN2)N",  # Core active structure
    "Candidate_02 (Heavy Ring Compound)": "C1=CC=C(C=C1)C2=CC=CC=C2C3=CC=CC=C3C4=CC=CC=C4",  # Too bulky!
    "Candidate_03 (Synthetic Peptide)": "CC(C)C(C(=O)O)NC(=O)C",  # Highly absorbable protein piece
    "Candidate_04 (Fluorinated Blocker)": "C1=CC=C(C=C1)F",  # Small modified structure
    "Candidate_05 (Reactive Hazard)": "C1=CC=C(C=C1)S(=O)(=O)Cl",  # High toxic reaction risk!
    "Candidate_06 (Natural Plant Extract)": "CC1=CC(=O)C2=C(C1)C(=O)C=CC2=O"  # Balanced quinone structure
}

print("=" * 70)
print("💊 ADVANCED COMPUTER-AIDED DRUG DESIGN: MULTI-PARAMETRIC FILTER 💊")
print("=" * 70)
print(f"🧬 Scanning {len(advanced_chemical_library)} complex molecular strings in the digital library...\n")

screening_results = []

# 2. Dual-Gate Bioavailability & Toxicity Screening Loop
for name, smiles in advanced_chemical_library.items():
    # Calculate simple structural attributes
    carbon_atoms = smiles.count("C")
    heavy_atoms = len(smiles)  # Proxy for molecular weight/complexity
    
    # Calculate Simulated Lipophilicity Score (LogP Proxy)
    # Balanced ratio of Carbon creates proper oil-water partition balance
    if "O" in smiles or "N" in smiles:
        hetero_atoms = smiles.count("O") + smiles.count("N")
        lipophilicity_score = (carbon_atoms / hetero_atoms) * 12.5
    else:
        lipophilicity_score = carbon_atoms * 8.0 # Pure hydrocarbons lack water solubility

    # Apply Dual-Gate Filters:
    # Filter 1: Size & Absorption Check (Complexity must be balanced, absorption between 35-75)
    # Filter 2: Toxic Structural Alert Check (Flagging dangerous Chlorine 'Cl' or excessive size)
    
    is_absorbable = 35.0 <= lipophilicity_score <= 75.0
    is_too_bulky = heavy_atoms > 35
    has_toxic_alert = "Cl" in smiles or ("S(=O)" in smiles)

    if has_toxic_alert:
        final_status = "REJECTED (Chemical Toxicity Alert)"
    elif is_too_bulky:
        final_status = "REJECTED (Molecular Weight Too Heavy)"
    elif is_absorbable:
        final_status = "APPROVED (Lead Candidate Select)"
    else:
        final_status = "REJECTED (Poor Pharmacokinetic Profile)"

    screening_results.append({
        "Compound_ID": name,
        "SMILES": smiles,
        "Structural_Complexity": heavy_atoms,
        "Simulated_Bio_Score": round(lipophilicity_score, 2),
        "Decision": final_status
    })

# 3. Compile Database and Print Clinical Lead Report
df_advanced_drugs = pd.DataFrame(screening_results)
df_advanced_drugs.to_csv("advanced_screening_output.csv", index=False)

print("📋 High-Throughput Screening Log:")
print("-" * 70)
for index, row in df_advanced_drugs.iterrows():
    print(f"🧪 {row['Compound_ID']}:")
    print(f"   [SMILES]: {row['SMILES']}")
    print(f"   [Metrics]: Complexity: {row['Structural_Complexity']} | Score: {row['Simulated_Bio_Score']}%")
    print(f"   [Decision]: {row['Decision']}\n")

print("=" * 70)
# Extract the winning candidates to advance to live cell assays
approved_leads = df_advanced_drugs[df_advanced_drugs["Decision"] == "APPROVED (Lead Candidate Select)"]

print(f"🚨 【HTS SCREENING RESULTS SUMMARY】:")
print(f"   Total Compounds Scanned: {len(df_advanced_drugs)}")
print(f"   Total Approved Leads Moving to Lab Assays: {len(approved_leads)}")
if not approved_leads.empty:
    print(f"   🚀 Selected Lead Molecules:")
    for name in approved_leads["Compound_ID"]:
        print(f"      -> {name}")
else:
    print("   ❌ No compounds met the dual-gate safety criteria.")
print("=" * 70)
