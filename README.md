# threejg-health-solutions
CSULA IBM Hackathon 2026

Our health solution app helps both patients and healthcare workers streamline the patient intake process.

Patients interact with an AI assistant powered by IBM Watson to quickly provide required information such as personal details, symptoms, and insurance information. The assistant ensures that all required fields are collected before submission.

The completed intake data is then validated and converted into a structured format for healthcare workers, allowing them to receive fully completed patient forms without missing information.

## Tech Stack
- IBM Watson AI Agents
- Streamlit
- Python
- Pandas

## Stretch Goals
We plan to incorporate basic machine learning techniques to assist healthcare workers with potential diagnosis suggestions.

- **DBSCAN** for clustering similar symptom patterns
- **K-Nearest Neighbors (KNN)** to suggest possible diagnoses based on symptom similarity


# WXO Hackathon Project

## Setup
```bash
cp .env.template .env
# fill in your keys in .env

python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run
```bash
cd app
streamlit run main.py
```

## Deploy Agents
```bash
./scripts/deploy.sh
```
