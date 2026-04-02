from app.nlp.extractor import extract_symptoms
from app.ml.predict import predict_disease
from app.services.recommendation_service import get_recommendation

def handle_chat(message: str):
    symptoms = extract_symptoms(message)
    disease = predict_disease(symptoms)
    recommendation = get_recommendation(disease)

    return {
        "symptoms": symptoms,
        "possible_condition": disease,
        "advice": recommendation,
        "disclaimer": "Consult a doctor for professional advice."
    }