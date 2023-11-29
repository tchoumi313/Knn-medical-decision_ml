import pandas as pd

# Define the data
diseases_data = [
    {'Maladie': 'GASTROENTERITE'},
    # Add data for other diseases
]

symptoms_data = [
    {'Symptome': 'DIARRHEE'},
    {'Symptome': 'CRAMPES ABDOMINALES ET DOULEURS MUSCULAIRES'},
    {'Symptome': 'NAUSEES et VOMISSEMENTS'},
    {'Symptome': "FIEVRES LEGERE MAL DE TETE"},
    {'Symptome': "PERTE D'APPETIT et Fatigue"},
    # Add data for other symptoms
]

medications_data = [
    {'Medicament': 'Diarétil'},
    {'Medicament': 'Tiorfan'},
    {'Medicament': 'Ercuferyl'},
    {'Medicament': 'Interix'},
    {'Medicament': 'Flagyl'},
    # Add data for other medications
]

# Create DataFrames
df_diseases = pd.DataFrame(diseases_data)
df_symptoms = pd.DataFrame(symptoms_data)
df_medications = pd.DataFrame(medications_data)

# Create junction tables
# Diseases-Symptoms relationship
df_disease_symptoms = pd.DataFrame([
    {'Maladie': 'GASTROENTERITE', 'Symptome': 'DIARRHEE'},
    {'Maladie': 'GASTROENTERITE', 'Symptome': 'CRAMPES ABDOMINALES ET DOULEURS MUSCULAIRES'},
    {'Maladie': 'GASTROENTERITE', 'Symptome': 'NAUSEES et VOMISSEMENTS'},
    # Add relationships for other diseases and symptoms
])

# Symptoms-Medications relationship
df_symptom_medications = pd.DataFrame([
    {'Symptome': 'DIARRHEE', 'Medicament': 'Diarétil'},
    {'Symptome': 'DIARRHEE', 'Medicament': 'Other Medication1'},
    {'Symptome': 'CRAMPES ABDOMINALES ET DOULEURS MUSCULAIRES', 'Medicament': 'Other Medication2'},
    # Add relationships for other symptoms and medications
])

# Print the DataFrames
print("Diseases:")
print(df_diseases)

print("\nSymptoms:")
print(df_symptoms)

print("\nMedications:")
print(df_medications)

print("\nDiseases-Symptoms Relationship:")
print(df_disease_symptoms)

print("\nSymptoms-Medications Relationship:")
print(df_symptom_medications)
