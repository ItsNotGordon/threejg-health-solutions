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
