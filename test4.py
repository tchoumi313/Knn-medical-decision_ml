
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier


# Create a DataFrame from the provided data
df = pd.read_csv("dataset.csv")

# Find the index of the "Maladie" column
maladie_column_index = df.columns.get_loc("Maladie")

# Extract symptoms and diseases up to "Maladie" column
symptoms_columns = df.columns[1:maladie_column_index]
X_train = df[symptoms_columns].values
y_train = df['Maladie'].values
print(X_train)
print("")
print(y_train)
# Create a kNN classifier with k=3
knn_classifier = KNeighborsClassifier(n_neighbors=3, weights='distance')
# Fit the classifier with training data
knn_classifier.fit(X_train, y_train)

# Predicting disease for new symptoms
new_symptoms = [[0, 1, 1, 1, 0], [1, 1, 1, 1, 1], [0, 0, 0, 1, 1]]  # Modify with actual symptoms
predicted_diseases = knn_classifier.predict(new_symptoms)

# Display the new symptoms and predicted diseases
print(f"The new symptoms: {new_symptoms}")
print(f"The predicted diseases for the given symptoms are: {predicted_diseases}")
