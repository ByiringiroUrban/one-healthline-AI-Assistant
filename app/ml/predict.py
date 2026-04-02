from pathlib import Path

import joblib

SYMPTOMS = ["fever", "cough", "headache", "pain"]
MODEL_PATH = Path(__file__).resolve().parents[2] / "models" / "disease_model.pkl"


def _load_model():
    if not MODEL_PATH.exists() or MODEL_PATH.stat().st_size == 0:
        return None

    try:
        return joblib.load(MODEL_PATH)
    except Exception:
        return None


def _rule_based_prediction(symptoms):
    normalized = {symptom.lower().strip() for symptom in symptoms}

    if {"fever", "cough"}.issubset(normalized):
        return "Flu"
    if {"fever", "pain"}.issubset(normalized):
        return "Malaria"
    if "headache" in normalized:
        return "Migraine"
    if normalized:
        return "General Checkup Recommended"
    return "No matching condition found"


model = _load_model()


def predict_disease(symptoms):
    normalized = [symptom.lower().strip() for symptom in symptoms]

    if model is not None:
        vector = [1 if symptom in normalized else 0 for symptom in SYMPTOMS]
        try:
            prediction = model.predict([vector])
            return prediction[0]
        except Exception:
            pass

    return _rule_based_prediction(normalized)
