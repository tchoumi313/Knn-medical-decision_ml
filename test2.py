import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

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

# Create a set of symptoms for each disease
diseases_symptoms = {}
for index, row in df_disease_symptoms.iterrows():
    disease = row['Maladie']
    symptom = row['Symptome']
    if disease not in diseases_symptoms:
        diseases_symptoms[disease] = set()
    diseases_symptoms[disease].add(symptom)

# Create training data for kNN
X_train = [[1, 1, 0, 1, 0],  # symptoms for German Measles
[0, 1, 1, 1, 1],  # symptoms for Common Cold
]
y_train = ["German Measles","Common Cold"]

for disease, symptoms in diseases_symptoms.items():
    symptoms_vector = [1 if symptom in symptoms else 0 for symptom in df_symptoms['Symptome']]
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
new_symptoms = [[0, 1, 1, 1, 0], [1, 1, 1, 1, 1], [0, 0, 0, 1, 1]]  # Modify with actual symptoms
predicted_disease = knn_classifier.predict(new_symptoms)

print(f"The new symptoms: {new_symptoms}")
print(f"The predicted disease for the given symptoms is: {predicted_disease}")
