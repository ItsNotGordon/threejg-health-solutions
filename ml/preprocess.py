from ml.symptom_map import SYMPTOMS

ALIASES = {
    "coughing": "cough",
    "cough": "cough",
    "fever": "high_fever",
    "feverish": "high_fever",
    "throwing up": "vomiting",
    "vomit": "vomiting",
    "tired": "fatigue",
    "exhausted": "fatigue",
}

def extract_symptoms(symptom_text: str) -> list[str]:
    text = symptom_text.lower()
    found = set()

    for phrase, canonical in ALIASES.items():
        if phrase in text:
            found.add(canonical)

    for symptom in SYMPTOMS:
        if symptom in text:
            found.add(symptom)

    return sorted(found)

def symptoms_to_vector(found_symptoms: list[str], feature_columns: list[str]) -> list[int]:
    found_set = set(found_symptoms)
    return [1 if col in found_set else 0 for col in feature_columns]