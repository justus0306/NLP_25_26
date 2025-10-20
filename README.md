# 🧠 Grundlagen des NLP – WS25/26

## 📌 Projektbeschreibung

Dieses Repository gehört zur Lehrveranstaltung **Grundlagen des Natural Language Processing** (WS 2025/26).  
Ziel ist es, anhand eines mehrthemenbezogenen Tweet-Datensatzes eine vollständige NLP-Pipeline zu entwickeln:

- 📥 Datenanalyse
- 🧹 Vorverarbeitung (Text Cleaning)
- ☁️ Visualisierung
- 🧠 Modellierung (Multi-Label Klassifikation)
- 📊 Evaluation

---

## 📂 Projektstruktur

```bash
.
├── Data/                     # Lokale Kopien der Datensätze (.parquet)
├── Hikmet/                  # Persönlicher Projektordner
│   ├── notebooks/
│   └── results/
├── Justus/
│   └── notebooks/
├── Sunny/
│   └── notebooks/
├── Übung/                   # Übungsmaterialien / Lösungen
├── README.md                # Projektbeschreibung (diese Datei)
└── .gitignore               # Ignorierte Dateien und Ordner
```

---

## ⚙️ Setup

### 📦 Voraussetzungen

- Python 3.11+
- [Anaconda](https://www.anaconda.com/) oder `venv`
- Abhängigkeiten:
  ```bash
  pip install datasets pandas matplotlib nltk spacy
  ```

### 📚 Sprachmodelle / Ressourcen

```python
import nltk
nltk.download("stopwords")

import spacy
spacy.cli.download("en_core_web_sm")
```

---

## 🚀 Nutzung

1. Umgebung aktivieren:
   ```bash
   conda activate nlp_tweets
   ```

2. Jupyter starten:
   ```bash
   jupyter notebook
   ```

3. Notebook öffnen:
   ```
   Hikmet/notebooks/01_data_exploration.ipynb
   ```

---

## ✅ Bearbeitete Aufgaben

| Übung | Inhalt                                | Status |
|-------|----------------------------------------|--------|
| 1     | Datensatz laden, erkunden, visualisieren | ✅ erledigt |
| 2     | Preprocessing (Stopwords, Tokenisierung, etc.) | 🔄 in Bearbeitung |
| 3     | Klassifikation vorbereiten              | ⏳ noch offen |
| 4     | Evaluation & Interpretation             | ⏳ noch offen |

---

## 👥 Team

- Hikmet Acig
- Sunny Wicklein
- Justus Jochum

---

## 🔒 Lizenz

Dieses Projekt ist Teil einer universitären Lehrveranstaltung und nicht öffentlich lizenziert.  
Verwendung ausschließlich zu Lernzwecken im Rahmen des Kurses **Grundlagen des NLP**.

---

## 📬 Kontakt

Für Fragen oder Beiträge: bitte über GitLab Merge Requests oder direkt via E-Mail an das Team.