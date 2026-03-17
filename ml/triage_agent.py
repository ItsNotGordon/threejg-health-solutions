import joblib
from ml.preprocess import extract_symptoms, symptoms_to_vector

MODEL_PATH = "ml/models/knn_model.joblib"
ENCODER_PATH = "ml/models/label_encoder.joblib"
FEATURES_PATH = "ml/models/feature_columns.joblib"

model = joblib.load(MODEL_PATH)
encoder = joblib.load(ENCODER_PATH)
feature_columns = joblib.load(FEATURES_PATH)

def run_triage(symptom_text: str) -> dict:
    found = extract_symptoms(symptom_text)
    vector = symptoms_to_vector(found, feature_columns)

    if hasattr(model, "predict_proba"):
        probs = model.predict_proba([vector])[0]
        top_indices = probs.argsort()[-3:][::-1]
        predictions = [
            {
                "condition": encoder.inverse_transform([i])[0],
                "confidence": float(probs[i]),
            }
            for i in top_indices
        ]
    else:
        pred = model.predict([vector])[0]
        predictions = [
            {
                "condition": encoder.inverse_transform([pred])[0],
                "confidence": 1.0,
            }
        ]

    return {
        "detected_symptoms": found,
        "predictions": predictions,
    }