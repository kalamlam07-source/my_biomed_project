import pandas as pd

# 1. A virtual library of potential drug molecules represented by their SMILES chemical codes
# We are testing 4 different compound formulas against a target viral protein (like COVID-19 protease)
chemical_library = {
    "Compound_A (Experimental)": "CCN(CC)CC",  # Small molecule
    "Compound_B (Aspirin-like)": "CC(=O)OC1=CC=CC=C1C(=O)O",  # Medium complex
    "Compound_C (Heavy Blocker)": "C1=CC=C(C=C1)C2=CC=CC=C2C3=CC=CC=C3",  # Large ring structure
    "Compound_D (Toxic Control)": "ClC(Cl)(Cl)Cl",  # Chloroform-like (Too harsh for human cells)
}

print("=" * 60)
print("💊 VIRTUAL DRUG DISCOVERY LAB: MOLECULAR SCREENING 💊")
print("=" * 60)
print(f"🧬 Loaded {len(chemical_library)} candidate molecules into the computer model.\n")

# 2. Automated Molecular Property Filtering
# In drug development, Lipinski's Rule of 5 states that a good drug should not be too heavy or complex, 
# otherwise the human stomach and cells cannot absorb it!

results = []

for name, smiles in chemical_library.items():
    # Calculate structural complexity simply by counting key atoms
    carbon_count = smiles.count("C")
    oxygen_count = smiles.count("O")
    total_length = len(smiles)

    # Biological Drug-Likeness Score Formula (Simulated Absorption Rate)
    # Higher carbon-to-oxygen ratio generally means better membrane permeability, 
    # but too long means it won't dissolve in water (blood).
    if oxygen_count == 0:
        absorption_rate = 15.0  # Hard to dissolve
    else:
        absorption_rate = (carbon_count / oxygen_count) * 25.0

    # Ensure absorption stays within a realistic 0-100% boundary
    absorption_rate = min(100.0, max(5.0, absorption_rate))

    # Determine if it passes the preliminary drug safety scan
    if 40.0 <= absorption_rate <= 85.0 and "Cl" not in smiles:
        status = "PASSED (Safe & Absorbable)"
    elif "Cl" in smiles:
        status = "FAILED (High Toxicity Risk)"
    else:
        status = "FAILED (Poor Bioavailability)"

    results.append(
        {
            "Molecule_Name": name,
            "SMILES_Structure": smiles,
            "Est_Absorption_%": round(absorption_rate, 2),
            "Screening_Status": status,
        }
    )

# 3. Process with Pandas and Print Report
df_drugs = pd.DataFrame(results)
df_drugs.to_csv("virtual_screening_report.csv", index=False)

print("📊 Automated Chemical Screening Report:")
print("-" * 60)
for index, row in df_drugs.iterrows():
    print(f"🧪 {row['Molecule_Name']}:")
    print(f"   Structure: {row['SMILES_Structure']}")
    print(f"   Absorption: {row['Est_Absorption_%']}% | Status: {row['Screening_Status']}\n")

print("=" * 60)
# Find the winning drug candidate
winners = df_drugs[df_drugs["Screening_Status"] == "PASSED (Safe & Absorbable)"]
if not winners.empty:
    top_drug = winners.iloc[0]["Molecule_Name"]
    print(f"🚨 【LEAD OPTIMIZATION SUCCESS】:\n   【{top_drug}】 successfully passed all computer safety filters!")
    print("   This molecule is recommended to move forward to real physical lab testing on cells.")
else:
    print("🚨 【SCREENING FAILED】: No molecules passed the safety thresholds.")
print("=" * 60)

