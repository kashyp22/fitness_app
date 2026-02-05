import google.generativeai as genai
from PIL import Image
import os
from django.conf import settings

# Configure using settings
genai.configure(api_key=getattr(settings, 'GEMINI_API_KEY', os.getenv('GEMINI_API_KEY')))
model = genai.GenerativeModel("gemini-2.5-flash")  # Updated to current stable flash


def predict_disease(image_path=None, symptoms_text=None):
    """
    Analyzes an image and/or text symptoms to predict potential health issues.
    """
    prompt = """
    You are a professional medical diagnostic assistant. 
    Analyze the provided input (image of a skin condition or a text description of symptoms).

    Provide the response in the following format:
    1. Possible Condition: [Name]
    2. Confidence Level: [Percentage]
    3. Common Symptoms: [List]
    4. Recommendation: [Next steps]
    5. Disclaimer: This is an AI-generated assessment. Please consult a doctor for a formal diagnosis.
    """

    content_list = [prompt]

    # Handle Symptoms Text
    if symptoms_text:
        content_list.append(f"User Symptoms: {symptoms_text}")

    # Handle Image
    if image_path:
        try:
            img = Image.open(image_path)
            content_list.append(img)
        except Exception as e:
            return {"error": f"Image processing failed: {str(e)}"}

    try:
        # Generate prediction
        response = model.generate_content(content_list)
        return {"status": "success", "prediction": response.text}
    except Exception as e:
        return {"error": f"Gemini API error: {str(e)}"}


def generate_health_plan(bmi, age, gender, goal, weight, height):
    try:
        bmi_val = float(bmi)
    except:
        bmi_val = 0.0

    prompt = f"""
    Act as a professional Fitness Coach and Nutritionist.
    User Profile:
    - BMI: {bmi_val:.1f}
    - Age: {age}
    - Gender: {gender}
    - Current Weight: {weight}kg, Height: {height}cm
    - Goal: {goal}

    Please provide a structured plan in the following format:
    **Daily Caloric Target**: [Estimated Calories]
    **Diet Plan**: [Breakfast, Lunch, Dinner, and Snacks]
    **Workout Plan**: [Specific exercises suited for this BMI and goal]
    **Pro Tip**: [One specific piece of advice]
    """

    try:
        response = model.generate_content(prompt)
        return {"status": "success", "plan": response.text}
    except Exception as e:
        return {"error": str(e)}