import joblib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_DIR = BASE_DIR / "saved_models"

model = joblib.load(MODEL_DIR / "emotion_model.pkl")
vectorizer = joblib.load(MODEL_DIR / "vectorizer.pkl")

while True:
    text = input("Text eingeben: ")

    transformed = vectorizer.transform([text])

    prediction = model.predict(transformed)[0]

    probabilities = model.predict_proba(transformed)[0]

    print("Erkannte Emotion:", prediction)

    for emotion, prob in zip(model.classes_, probabilities):
        print(f"{emotion}: {prob:.2%}")
        print()