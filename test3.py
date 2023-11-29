import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from openpyxl.workbook import Workbook
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
df_disease_symptoms = pd.DataFrame([
    {'Maladie': 'GASTROENTERITE', 'Symptome': 'DIARRHEE'},
    {'Maladie': 'GASTROENTERITE', 'Symptome': 'CRAMPES ABDOMINALES ET DOULEURS MUSCULAIRES'},
    {'Maladie': 'GASTROENTERITE', 'Symptome': 'NAUSEES et VOMISSEMENTS'},
    # Add relationships for other diseases and symptoms
])

df_symptom_medications = pd.DataFrame([
    {'Symptome': 'DIARRHEE', 'Medicament': 'Diarétil'},
    {'Symptome': 'DIARRHEE', 'Medicament': 'Other Medication1'},
    {'Symptome': 'CRAMPES ABDOMINALES ET DOULEURS MUSCULAIRES', 'Medicament': 'Other Medication2'},
    # Add relationships for other symptoms and medications
])

"""# Create a set of symptoms for each disease
diseases_symptoms = {}
for index, row in df_disease_symptoms.iterrows():
    disease = row['Maladie']
    symptom = row['Symptome']
    if disease not in diseases_symptoms:
        diseases_symptoms[disease] = set()
    diseases_symptoms[disease].add(symptom)
"""
# Create a function to simulate a doctor's consultation
def simulate_consultation(patient_id, symptoms_present, maladie_diagnosed, medicament_prescribed):
    return {
        'Patient_ID': patient_id,
        'Symptoms_Present': symptoms_present,
        'Maladie_Diagnosed': maladie_diagnosed,
        'Medicament_Prescribed': medicament_prescribed
    }

# Simulate multiple consultations
consultations = [
    simulate_consultation(1, ['DIARRHEE', 'NAUSEES et VOMISSEMENTS', "CRAMPES ABDOMINALES ET DOULEURS MUSCULAIRES"], 'GASTROENTERITE', ['Diarétil']),
    simulate_consultation(1, ['DIARRHEE', 'NAUSEES et VOMISSEMENTS', 'CRAMPES ABDOMINALES ET DOULEURS MUSCULAIRES',
                              'FIEVRES LEGERE MAL DE TETE', "PERTE D'APPETIT et Fatigue"], 'GASTROENTERITE',
                          ['Diarétil', 'Other Medication1']),
    simulate_consultation(2, ['DIARRHEE', 'CRAMPES ABDOMINALES ET DOULEURS MUSCULAIRES', 'NAUSEES et VOMISSEMENTS',
                              'FIEVRES LEGERE MAL DE TETE'], 'GASTROENTERITE', ['Diarétil', 'Other Medication2']),
    """simulate_consultation(3, ['DIARRHEE', 'CRAMPES ABDOMINALES ET DOULEURS MUSCULAIRES', 'NAUSEES et VOMISSEMENTS',
                              'FIEVRES LEGERE MAL DE TETE', 'Sneezing'], 'Common Cold', ['Other Medication1']),
    simulate_consultation(4, ['DIARRHEE', 'CRAMPES ABDOMINALES ET DOULEURS MUSCULAIRES', 'NAUSEES et VOMISSEMENTS',
                              'FIEVRES LEGERE MAL DE TETE', 'Sore Throat'], 'Common Cold', ['Other Medication2']),
"""
    # Add more simulated consultations as needed
]

, complete/modify the code to get the maladie,list of smptom,medication from here, contruct thei


# Convert consultations to DataFrame
df_consultations = pd.DataFrame([item for sublist in consultations for item in sublist])
df_consultations.to_excel('df_consult.xlsx', index=False)
# Update symptoms, diseases, and medications dataframes
for index, row in df_consultations.iterrows():
    # Update symptoms dataframe
    for symptom in row['Symptoms_Present']:
        if symptom not in df_symptoms['Symptome'].values:
            df_symptoms = df_symptoms._append({'Symptome': symptom}, ignore_index=True)

    # Update diseases dataframe
    if row['Maladie_Diagnosed'] not in df_diseases['Maladie'].values:
        df_diseases = df_diseases._append({'Maladie': row['Maladie_Diagnosed']}, ignore_index=True)

        # Update medications dataframe
        for medicament in row['Medicament_Prescribed']:
            if medicament not in df_medications['Medicament'].values:
                df_medications = df_medications._append({'Medicament': medicament}, ignore_index=True)

# Update relationships in df_disease_symptoms and df_symptom_medications
# Update relationships in df_disease_symptoms and df_symptom_medications
for index, row in df_consultations.iterrows():
    maladie_id = df_diseases[df_diseases['Maladie'] == row['Maladie_Diagnosed']].index[0]

    for symptom in row['Symptoms_Present']:
        symptom_id = df_symptoms[df_symptoms['Symptome'] == symptom].index[0]

        # Update df_disease_symptoms
        if len(df_disease_symptoms[(df_disease_symptoms['Maladie'] == maladie_id) & (df_disease_symptoms['Symptome'] == symptom_id)]) == 0:
            df_disease_symptoms = df_disease_symptoms._append({'Maladie': maladie_id, 'Symptome': symptom_id}, ignore_index=True)

    for medicament in row['Medicament_Prescribed']:
        print(medicament)
        medicament_id = df_medications[df_medications['Medicament'] == medicament].index[0]

        # Update df_symptom_medications
        for symptom in row['Symptoms_Present']:
            symptom_id = df_symptoms[df_symptoms['Symptome'] == symptom].index[0]
            if len(df_symptom_medications[(df_symptom_medications['Symptome'] == symptom_id) & (df_symptom_medications['Medicament'] == medicament_id)]) == 0:
                df_symptom_medications = df_symptom_medications._append({'Symptome': symptom_id, 'Medicament': medicament_id}, ignore_index=True)

# Save dataframes to Excel files
df_symptoms.to_excel('symptoms_data_updated.xlsx', index=False)
df_diseases.to_excel('diseases_data_updated.xlsx', index=False)
df_medications.to_excel('medications_data_updated.xlsx', index=False)
df_disease_symptoms.to_excel('disease_symptoms_updated.xlsx', index=False)
df_symptom_medications.to_excel('symptom_medications_updated.xlsx', index=False)

"""
# Convert consultations to DataFrame
df_consultations = pd.DataFrame(consultations)
# Create separate rows for each symptom in df_consultations
df_consultations_exploded = df_consultations.explode('Symptoms_Present')

# Merge DataFrames
df_combined = pd.merge(df_consultations_exploded, df_symptoms, left_on='Symptoms_Present', right_on='Symptome', how='left')
df_combined = pd.merge(df_combined, df_diseases, left_on='Maladie_Diagnosed', right_on='Maladie', how='left')
df_combined = pd.merge(df_combined, df_medications, left_on='Medicament_Prescribed', right_on='Medicament', how='left')

# Print the combined DataFrame
print(df_combined)

df_combined.to_excel('consultations_data.xlsx', index=False)


# Create a set of symptoms for each disease, including new symptoms from consultations
for index, row in df_combined.iterrows():
    if pd.notna(row['Symptoms_Present']):
        diseases_symptoms[row['Maladie']].update(row['Symptoms_Present'])

# Create training data for kNN
X_train = []
y_train = []

for disease, symptoms in diseases_symptoms.items():
    symptoms_vector = [len(symptoms.intersection(set(df_symptoms['Symptome']))) / len(symptoms)]
    X_train.append(symptoms_vector)
    y_train.append(disease)

# Create a kNN classifier with k=3
knn_classifier = KNeighborsClassifier(n_neighbors=3, weights='distance')
print(X_train)
print("")
print(y_train)
# Fit the classifier with training data
knn_classifier.fit(X_train, y_train)

# Predicting disease for new symptoms
new_symptoms = [[1]]  # Modify with actual symptoms
predicted_disease = knn_classifier.predict([new_symptoms])

print(f"The predicted disease for the given symptoms is: {predicted_disease[0]}")
"""
# Questions to ask the patient
"""questions = [
    "Do you have diarrhea? (yes/no): ",
    "Do you experience abdominal cramps and muscle pain? (yes/no): ",
    "Do you have nausea and vomiting? (yes/no): ",
    # Add more questions for other symptoms
]

# Patient's responses
patient_responses = []

for question in questions:
    response = input(question).lower()
    patient_responses.append(response)

# Convert patient responses to symptoms vector
new_symptoms = [1 if response == 'yes' else 0 for response in patient_responses]

predicted_disease = knn_classifier.predict(new_symptoms)

print(f"The predicted disease for the given symptoms is: {predicted_disease[0]}")
"""