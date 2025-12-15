# 🧠 Grundlagen des NLP – WS25/26

## 📌 Projektbeschreibung

Dieses Repository gehört zur Lehrveranstaltung **Grundlagen des Natural Language Processing** (WS 2025/26).  
Ziel ist es, anhand eines mehrthemenbezogenen Tweet-Datensatzes eine vollständige NLP-Pipeline zu entwickeln: 

- 📥 Datenanalyse
- 🧹 Vorverarbeitung (Text Cleaning)
- ☁️ Visualisierung
- 🧠 Modellierung (Multi-Label & Single-Label Klassifikation)
- 📊 Evaluation

---

## 📂 Projektstruktur

```bash
. 
├── Abgabe/                   # Finale Abgaben
│   ├── Data/                 # Datensätze für Abgabe
│   └── Notebooks/            # Finalisierte Notebooks
├── Hikmet/                   # Persönlicher Projektordner
│   ├── notebooks/
│   ├── lab4_hikmet.ipynb     # Lab 4 Übung
│   └── skizze
├── Justus/
│   ├── Data/
│   ├── lab2.ipynb
│   ├── lab2_justus.ipynb
│   ├── lab2_single_label.ipynb
│   ├── lab4_single_label.ipynb
│   ├── lab5.ipynb
│   └── loading+textfilter+preprocessing_version2.ipynb
├── Sunny/
│   ├── lab3_sunny.ipynb
│   └── lab4_sunny.ipynb
├── environment.yml           # Conda Environment Konfiguration
└── README.md                 # Projektbeschreibung (diese Datei)
```

---

## ⚙️ Setup

### 📦 Voraussetzungen

- Python 3.11+
- [Anaconda](https://www.anaconda.com/) oder `venv`

### 🔧 Environment einrichten

```bash
# Environment erstellen
conda env create -f environment.yml

# Environment aktualisieren
conda env update -f environment.yml --prune

# Environment aktivieren
conda activate nlp_tweets
```

### 📦 Enthaltene Pakete

- `pandas`, `matplotlib`, `seaborn` – Datenanalyse & Visualisierung
- `scikit-learn` – Machine Learning
- `nltk`, `spacy` – NLP-Bibliotheken
- `datasets` – Hugging Face Datasets
- `emoji` – Emoji-Verarbeitung
- `jupyterlab` – Notebook-Umgebung

### 📚 Sprachmodelle / Ressourcen

```python
import nltk
nltk.download("stopwords")

import spacy
spacy.cli.download("en_core_web_sm")
```

---

## 🚀 Nutzung

1.  Umgebung aktivieren:
   ```bash
   conda activate nlp_tweets
   ```

2. Jupyter starten:
   ```bash
   jupyter lab
   ```

3. Notebook öffnen und loslegen! 

---

## ✅ Bearbeitete Aufgaben

| Übung | Inhalt                                         | Status         | Bearbeiter |
|-------|------------------------------------------------|----------------|------------|
| 2     | Datenanalyse, Preprocessing     | ✅ erledigt    | Justus     |
| 3     | Visualisierung & Exploration                   | ✅ erledigt    | Sunny      |
| 4     | Klassifikation (Single-Label)                  | ✅ erledigt    | Hikmet, Justus |
| 5     | Evaluation & Modellvergleich                   | in Arbeit    | Justus     |

---

## 👥 Team

- **Hikmet Acig** – Lab 4
- **Sunny Wicklein** – Lab 3, Lab 4
- **Justus Jochum** – Lab 2, Lab 5, Preprocessing

---

## 🔒 Lizenz

Dieses Projekt ist Teil einer universitären Lehrveranstaltung und nicht öffentlich lizenziert.  
Verwendung ausschließlich zu Lernzwecken im Rahmen des Kurses **Grundlagen des NLP**. 

---

## 📬 Kontakt

Für Fragen oder Beiträge:  bitte über GitHub Pull Requests oder direkt via E-Mail an das Team.