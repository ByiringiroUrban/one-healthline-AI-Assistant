def extract_symptoms(text: str):
    symptoms_db = ["fever", "cough", "headache", "pain"]

    found = []
    for s in symptoms_db:
        if s in text.lower():
            found.append(s)

    return found