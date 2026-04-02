def get_recommendation(disease):
    recommendations = {
        "Flu": "Rest and drink fluids",
        "Malaria": "Visit nearest health center",
        "Migraine": "Avoid stress and rest"
    }

    return recommendations.get(disease, "Seek medical advice")