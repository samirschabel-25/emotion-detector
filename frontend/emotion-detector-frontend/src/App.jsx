import { useState, useEffect } from "react";
import "./App.css";
import { PieChart, Pie, Cell, ResponsiveContainer, Tooltip } from "recharts";

const emotionConfig = {
  Freude: {
    emoji: "😊",
    color: "#22c55e",
  },
  Traurigkeit: {
    emoji: "😢",
    color: "#3b82f6",
  },
  Wut: {
    emoji: "😠",
    color: "#ef4444",
  },
  Angst: {
    emoji: "😨",
    color: "#f59e0b",
  },
  Neutral: {
    emoji: "😐",
    color: "#94a3b8",
  },
  Unsicher: {
    emoji: "🤔",
    color: "#eab308",
  },
};

const chartColors = {
  Freude: "#22c55e",
  Traurigkeit: "#3b82f6",
  Wut: "#ef4444",
  Angst: "#f59e0b",
  Neutral: "#94a3b8",
  Unsicher: "#eab308",
};

function App() {
  const [text, setText] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [history, setHistory] = useState([]);

  useEffect(() => {
    const savedHistory = localStorage.getItem("emotion-history");

    if (savedHistory) {
      setHistory(JSON.parse(savedHistory));
    }
  }, []);

  useEffect(() => {
    localStorage.setItem("emotion-history", JSON.stringify(history));
  }, [history]);

  const analyzeText = async () => {
    if (!text.trim()) return;

    setLoading(true);

    try {
      const response = await fetch(`${import.meta.env.VITE_API_URL}/predict`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          text,
        }),
      });

      const data = await response.json();

      setResult(data);

      setHistory((prev) => [
        {
          text,
          emotion: data.emotion,
          confidence: data.confidence,
          timestamp: new Date().toLocaleTimeString(),
        },
        ...prev.slice(0, 4),
      ]);
    } catch (error) {
      console.error(error);
      alert("Fehler beim Verbinden zur API");
    }

    setLoading(false);
  };

  const currentEmotion =
    result && emotionConfig[result.emotion]
      ? emotionConfig[result.emotion]
      : emotionConfig.Unsicher;

  const chartData = result
    ? Object.entries(result.probabilities).map(([emotion, value]) => ({
        name: emotion,
        value,
      }))
    : [];

  return (
    <div className="app">
      {" "}
      <div className="container">
        {" "}
        <h1 className="title">Emotion Detector</h1>
        <p className="subtitle">
          Analysiere die emotionale Stimmung eines Textes mit Machine Learning.
        </p>
        <div className="card">
          <textarea
            className="textarea"
            rows="6"
            placeholder="Schreibe hier deinen Text..."
            value={text}
            onChange={(e) => setText(e.target.value)}
          />

          <button className="button" onClick={analyzeText} disabled={loading}>
            {loading ? "Analysiere..." : "Analysieren"}
          </button>
        </div>
        {result && (
          <>
            <div className="card result-card">
              <h2>Analyseergebnis</h2>

              <div
                className="emotion-badge"
                style={{
                  backgroundColor: `${currentEmotion.color}20`,
                  borderColor: currentEmotion.color,
                  color: currentEmotion.color,
                }}
              >
                <span>{currentEmotion.emoji}</span>

                <span>{result.emotion}</span>
              </div>

              <p className="confidence">
                Confidence: <strong>{result.confidence}%</strong>
              </p>

              <div className="chart-container">
                <ResponsiveContainer width="100%" height={320}>
                  <PieChart>
                    <Pie
                      data={chartData}
                      dataKey="value"
                      nameKey="name"
                      innerRadius={80}
                      outerRadius={120}
                    >
                      {chartData.map((entry) => (
                        <Cell key={entry.name} fill={chartColors[entry.name]} />
                      ))}
                    </Pie>

                    <Tooltip />
                  </PieChart>
                </ResponsiveContainer>
              </div>

              <div className="probabilities">
                <h3>Wahrscheinlichkeiten</h3>

                {Object.entries(result.probabilities).map(
                  ([emotion, value]) => {
                    const config =
                      emotionConfig[emotion] || emotionConfig.Unsicher;

                    return (
                      <div key={emotion} className="probability-item">
                        <div className="probability-header">
                          <span>
                            {config.emoji} {emotion}
                          </span>

                          <span>{value}%</span>
                        </div>

                        <div className="progress-bar">
                          <div
                            className="progress-fill"
                            style={{
                              width: `${value}%`,
                              background: config.color,
                            }}
                          />
                        </div>
                      </div>
                    );
                  },
                )}
              </div>
            </div>

            {history.length > 0 && (
              <div className="card history-card">
                <h2>Letzte Analysen</h2>

                <button
                  className="clear-history-btn"
                  onClick={() => setHistory([])}
                >
                  Historie löschen
                </button>

                {history.map((item, index) => {
                  const config =
                    emotionConfig[item.emotion] || emotionConfig.Unsicher;

                  return (
                    <div key={index} className="history-item">
                      <div className="history-top">
                        <span>
                          {config.emoji} {item.emotion}
                        </span>

                        <span>{item.confidence}%</span>
                      </div>

                      <p>{item.text}</p>

                      <small>{item.timestamp}</small>
                    </div>
                  );
                })}
              </div>
            )}
          </>
        )}
      </div>
    </div>
  );
}

export default App;
