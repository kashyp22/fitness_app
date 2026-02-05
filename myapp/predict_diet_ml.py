import pickle
import numpy as np
import os
from .models import Diet_table

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ML_DIR = os.path.join(BASE_DIR, "ml_models")

# Load model and encoders
model = pickle.load(open(os.path.join(ML_DIR, "diet_model.pkl"), "rb"))
gender_encoder = pickle.load(open(os.path.join(ML_DIR, "gender_encoder.pkl"), "rb"))
type_encoder = pickle.load(open(os.path.join(ML_DIR, "type_encoder.pkl"), "rb"))

def predict_diet(age, height, weight, gender, food_preference=None, health_condition=None):
    gender_encoded = gender_encoder.transform([gender])[0]
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    bmi = round(bmi, 1)

    if bmi < 18.5:
        bmi_type = "underweight"
    elif 18.5 <= bmi < 24.9:
        bmi_type = "normal"
    elif 25 <= bmi < 29.9:
        bmi_type = "overweight"
    else:
        bmi_type = "obese"

    encoded_type = type_encoder.transform([bmi_type])[0]

    input_data = np.array([[age, height, weight, gender_encoded]])
    predicted_type_encoded = model.predict(input_data)[0]
    predicted_type = type_encoder.inverse_transform([predicted_type_encoded])[0]

    # Here you can filter DB using food preference / health condition if needed
    result = Diet_table.objects.filter(type=predicted_type).first()

    return {
        "bmi": bmi,
        "predicted_type": predicted_type,
        "diet": result.dietplan if result else "No plan found",
        "workout": result.work_out if result else "No workout found"
    }
