# 🧠 Emotion Detector

Ein Full-Stack Machine-Learning-Projekt zur Erkennung von Emotionen in deutschsprachigen Texten.

Die Anwendung analysiert einen beliebigen Text und klassifiziert ihn in eine der folgenden Emotionen:

- 😊 Freude
- 😢 Traurigkeit
- 😠 Wut
- 😨 Angst
- 😐 Neutral

Zusätzlich werden Wahrscheinlichkeiten für jede Emotion berechnet und visuell dargestellt.

---

## 🚀 Features

- Emotionserkennung für deutschsprachige Texte
- Machine-Learning-Modell mit Scikit-Learn
- Wahrscheinlichkeitsbewertung für jede Emotion
- Interaktive Visualisierung mit Diagrammen
- Moderne React-Benutzeroberfläche
- Analyse-Historie mit lokaler Speicherung
- REST API mit FastAPI
- Responsive Design

---

## 🏗️ Architektur

```text
React Frontend
       │
       ▼
FastAPI Backend
       │
       ▼
TF-IDF Vectorizer
       │
       ▼
Logistic Regression
       │
       ▼
Emotion Prediction
```

---

## 🛠️ Verwendete Technologien

### Frontend

- React
- Vite
- Recharts
- CSS3

### Backend

- FastAPI
- Uvicorn

### Machine Learning

- Scikit-Learn
- TF-IDF Vectorization
- Logistic Regression
- Pandas

---

## 📊 Funktionsweise

1. Der Benutzer gibt einen Text ein.
2. Der Text wird an die FastAPI-Schnittstelle gesendet.
3. Der TF-IDF-Vectorizer wandelt den Text in numerische Merkmale um.
4. Das trainierte Modell analysiert die Merkmale.
5. Die vorhergesagte Emotion und die Wahrscheinlichkeiten werden zurückgegeben.
6. Das Frontend visualisiert die Ergebnisse in Form von Diagrammen und Fortschrittsbalken.

---

## 📁 Projektstruktur

```text
emotion-detector/

├── api/
│   └── main.py

├── data/
│   ├── emotions.csv
│   └── generate_dataset.py

├── model/
│   ├── train.py
│   ├── predict.py
│   └── inspect_model.py

├── saved_models/
│   ├── emotion_model.pkl
│   └── vectorizer.pkl

├── frontend/
│   ├── src/
│   └── package.json

├── requirements.txt
└── README.md
```

---

## ⚙️ Lokale Installation

### Backend

Repository klonen:

```bash
git clone <repository-url>
cd emotion-detector
```

Abhängigkeiten installieren:

```bash
pip install -r requirements.txt
```

Backend starten:

```bash
uvicorn api.main:app --reload
```

API-Dokumentation:

```text
http://127.0.0.1:8000/docs
```

---

### Frontend

In das Frontend-Verzeichnis wechseln:

```bash
cd frontend
```

Abhängigkeiten installieren:

```bash
npm install
```

Entwicklungsserver starten:

```bash
npm run dev
```

---

## 🎯 Lernziele des Projekts

Dieses Projekt wurde entwickelt, um praktische Erfahrungen in folgenden Bereichen zu sammeln:

- Natural Language Processing (NLP)
- Machine Learning
- REST API Entwicklung
- Frontend-Entwicklung mit React
- Datenvisualisierung
- Full-Stack-Architektur

---

## 🔮 Mögliche Weiterentwicklungen

- Einsatz eines Transformer-Modells (BERT)
- Erweiterung des Datensatzes
- Benutzerkonten
- Cloud Deployment
- Mehrsprachige Emotionserkennung
- Echtzeit-Analyse

---

## 📜 Lizenz

Dieses Projekt dient Lern- und Portfoliozwecken.

```

```
