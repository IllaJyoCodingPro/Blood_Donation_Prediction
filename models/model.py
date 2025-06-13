import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score # type: ignore
# Load the dataset from an Excel file
dataset = pd.read_excel("data\BDPJ.xlsx")  # Replace "your_dataset.xlsx" with the path to your Excel file
# Data preprocessing
# Assuming 'blood group' is the target variable
X = dataset.drop(columns=['Sno', 'Blood group'])  # Adjust column names as needed
y = dataset['Blood group']
# One-hot encode categorical variables
X = pd.get_dummies(X)
# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Initialize and train the Random Forest Classifier model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
# Make predictions on the test set
predictions = model.predict(X_test)
# Evaluate the model
accuracy = accuracy_score(y_test, predictions)
print("Accuracy:", accuracy)
# Prompt the user to input the blood group
Blood_request = input("Enter the blood group you want to predict: ")

# Filter the dataset for donors matching the specified blood group
potential_donors = dataset[dataset['Blood group'] == Blood_request]

# Count the number of potential donors for the specified blood group
donor_count = len(potential_donors)

# Print the count of potential donors
print("Number of potential donors for blood group", Blood_request, ":", donor_count)
# Get detailed information of potential donors
if donor_count > 0:
    print("\nInformation of potential donors for blood group", Blood_request, ":")
    donor_info = potential_donors[['Name', 'Gender', 'Age', 'Area', 'Contact']]
    print(donor_info.to_string(index=False))
else:
    print("\nNo potential donors found for blood group", Blood_request)