import pandas as pd
import joblib
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

# Daten laden
df = pd.read_csv(r"C:\Users\samir\Desktop\Programme_Samir\emotion-detector\data\emotions.csv")
# Eingaben und Labels
X = df["text"]
y = df["emotion"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Text -> Zahlen
vectorizer = TfidfVectorizer(
    lowercase=True,
    ngram_range=(1, 2),
    min_df=2
)

X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

# Modell erzeugen
model = LogisticRegression(max_iter=1000)

# Training
model.fit(X_train_vectorized, y_train)

predictions = model.predict(X_test_vectorized)

accuracy = accuracy_score(y_test, predictions)

print()
print(f"Accuracy: {accuracy:.2%}")

print()
print(classification_report(y_test, predictions))

print("Training abgeschlossen!")

# Modell speichern

SAVE_DIR = Path(__file__).resolve().parent.parent / "saved_models"
SAVE_DIR.mkdir(exist_ok=True)

joblib.dump(model, SAVE_DIR / "emotion_model.pkl")
joblib.dump(vectorizer, SAVE_DIR / "vectorizer.pkl")

print("Modell gespeichert!")

# Testvorhersagen
tests = [
    "Ich freue mich riesig auf morgen",
    "Ich habe Angst vor dem Gespräch",
    "Das macht mich unglaublich wütend",
    "Heute gehe ich spazieren"
]

for text in tests:
    transformed = vectorizer.transform([text])
    prediction = model.predict(transformed)[0]

    print()
    print("Text:", text)
    print("Emotion:", prediction)