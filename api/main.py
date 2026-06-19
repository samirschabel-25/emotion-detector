from fastapi import FastAPI
import joblib
from pathlib import Path
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_DIR = BASE_DIR / "saved_models"

model = joblib.load(MODEL_DIR / "emotion_model.pkl")
vectorizer = joblib.load(MODEL_DIR / "vectorizer.pkl")
class PredictionRequest(BaseModel):
    text: str

@app.get("/")
def root():
    return {"message": "Emotion Detection API läuft"}

@app.post("/predict")
def predict(request: PredictionRequest):

    transformed = vectorizer.transform([request.text])

    prediction = model.predict(transformed)[0]

    probabilities = model.predict_proba(transformed)[0]

    confidence = max(probabilities) * 100

    # Unsicherheitsprüfung
    if confidence < 40:
        prediction = "Unsicher"

    probability_map = {}

    for emotion, prob in zip(model.classes_, probabilities):
        probability_map[emotion] = round(float(prob * 100), 2)

    return {
        "emotion": prediction,
        "confidence": round(confidence, 2),
        "probabilities": probability_map
    }