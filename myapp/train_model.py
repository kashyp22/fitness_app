import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import pickle

# Absolute paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # points to myapp/
ML_DIR = os.path.join(BASE_DIR, "ml_models")
CSV_PATH = os.path.join(ML_DIR, "diet_data.csv")

# Load CSV
df = pd.read_csv(CSV_PATH)

# Encode gender
le_gender = LabelEncoder()
df["gender_encoded"] = le_gender.fit_transform(df["gender"])

# Encode type
le_type = LabelEncoder()
df["type_encoded"] = le_type.fit_transform(df["type"])

# Features and labels
X = df[["age", "height", "weight", "gender_encoded"]]
y = df["type_encoded"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model + encoders in same folder
pickle.dump(model, open(os.path.join(ML_DIR, "diet_model.pkl"), "wb"))
pickle.dump(le_gender, open(os.path.join(ML_DIR, "gender_encoder.pkl"), "wb"))
pickle.dump(le_type, open(os.path.join(ML_DIR, "type_encoder.pkl"), "wb"))

print("Training complete. Models saved in ml_models folder.")
