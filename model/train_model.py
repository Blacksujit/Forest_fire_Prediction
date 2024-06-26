import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import pickle


# Load dataset
data = pd.read_csv('C:\\Users\\HP\\OneDrive\\Desktop\\ML_Model\\scrap_ex_project\\data\\forestfires.csv')

# Data Preprocessing (assuming month and day are categorical variables)
data['month'] = data['month'].astype('category').cat.codes
data['day'] = data['day'].astype('category').cat.codes


# Define significant fire: if area > 0, we consider it as fire
data['fire'] = np.where(data['area'] > 0, 1, 0)


# Select features and target
features = ['temp', 'RH', 'wind']
target = 'fire'

X = data[features]
y = data[target]


# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Train model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Model Accuracy: {accuracy:.2f}')
print(classification_report(y_test, y_pred))

print("training data :" , model.score(X_train, y_train)*100)
print('--------------------------------')
print("Testing data :" ,model.score(X_test, y_test)*100)

# Save the model
with open('./model/model.pkl', 'wb') as f:
    pickle.dump(model, f)


#____________________________________ OLD CODE(Old_MLModel) _____________________________


# # Training the model (if not already trained)
# def train_model():
#     # Load dataset
#     data = pd.read_csv('C:\\Users\\HP\\OneDrive\\Desktop\\Machine Learning Projects\\Forest_Fire_Prediction\\data\\forestfires.csv')

#     # Data Preprocessing (e.g., handling missing values, encoding)
#     data['month'] = data['month'].astype('category').cat.codes
#     data['day'] = data['day'].astype('category').cat.codes

#     # Feature and target selection
#     X = data.drop('area', axis=1)  # assuming 'area' is the target column
#     y = data['area']

#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#     # Train model
#     model = RandomForestRegressor()
#     model.fit(X_train, y_train)

#     # Save the trained model
#     pickle.dump(model, open('model/model.pkl', 'wb'))

# # Uncomment the line below to train the model
# train_model()
