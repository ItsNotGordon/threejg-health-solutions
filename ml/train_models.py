import os
import joblib
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder

DATA_PATH = "data/Training.csv"
MODEL_DIR = "ml/models"
MODEL_PATH = os.path.join(MODEL_DIR, "knn_model.joblib")
ENCODER_PATH = os.path.join(MODEL_DIR, "label_encoder.joblib")
FEATURES_PATH = os.path.join(MODEL_DIR, "feature_columns.joblib")

def train_knn():
    df = pd.read_csv(DATA_PATH)
    df = df.fillna(0)

    X = df.drop(columns=["prognosis"])
    y = df["prognosis"]

    encoder = LabelEncoder()
    y_encoded = encoder.fit_transform(y)

    model = KNeighborsClassifier(n_neighbors=5)
    model.fit(X, y_encoded)

    os.makedirs(MODEL_DIR, exist_ok=True)
    joblib.dump(model, MODEL_PATH)
    joblib.dump(encoder, ENCODER_PATH)
    joblib.dump(list(X.columns), FEATURES_PATH)

    print("KNN model trained and saved.")

if __name__ == "__main__":
    train_knn()