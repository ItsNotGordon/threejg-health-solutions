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
## Prerequisites
 
- Python 3.11+
- A watsonx Orchestrate account (IBM Cloud or AWS)
- An active Orchestrate environment with agents deployed
 
## Setup
 
### 1. Install dependencies
 
```bash
pip install -r requirements.txt
```
 
### 2. Install the Orchestrate ADK
 
```bash
pip install --upgrade ibm-watsonx-orchestrate
```
 
### 3. Add your Orchestrate environment
 
```bash
orchestrate env add -n hackathon -u <your-service-instance-url>
```
 
To find your service instance URL:
1. Log in to your watsonx Orchestrate instance
2. Click your user icon → Settings
3. Go to the API details tab
4. Copy the Service instance URL
 
### 4. Generate an API key
 
On the same API details page, click **Generate API key** and copy it.
 
### 5. Activate your environment
 
```bash
orchestrate env activate hackathon --api-key <your-api-key>
```
 
Note: the token expires every 2 hours. Re-run this command when it expires.
 
### 6. Import and deploy agents
 
```bash
orchestrate agents import -f agents/triage-router-agent.yaml
orchestrate agents import -f agents/occupational-health.yaml
orchestrate agents import -f agents/urgent-care-intake.yaml
orchestrate agents import -f agents/insurance-agent.yaml
 
orchestrate agents deploy --name triage_router_agent
orchestrate agents deploy --name occupational_health_Agent_7688qz
orchestrate agents deploy --name Urgent_Care_Intake_5198eo
orchestrate agents deploy --name agent_Insurance_Eligibility_and_Verification__51871W
```
 
### 7. Get the triage router agent ID
 
```bash
orchestrate agents list
```
 
Copy the ID for `triage_router_agent` and update it in `config.py`:
 
```python
TRIAGE_ROUTER_AGENT_ID = "<your-triage-router-id>"
```
 
### 8. Run the app
 
```bash
streamlit run app.py
```
 
Open `http://localhost:8501` in your browser.
 
To access from another machine on the same network:
 
```bash
streamlit run app.py --server.address 0.0.0.0
```
 
Then open `http://<your-ip>:8501` from the other machine.
 
## Project Structure
 
```
.
├── app.py                  # Streamlit chat UI
├── config.py               # Agent IDs
├── requirements.txt
├── agents/
│   ├── triage-router-agent.yaml
│   ├── occupational-health.yaml
│   ├── urgent-care-intake.yaml
│   ├── insurance-agent.yaml
│   ├── forms-agent.yaml
│   ├── health-bot.yaml
│   └── patient-intake-agent.yaml
└── service/
    ├── __init__.py
    └── orchestrate_service.py
```
 
## Agent Flow
 
1. **Triage Router** — asks the patient why they're visiting, routes to the correct intake agent
2. **Occupational Health Agent** — collects workplace injury intake fields from its knowledge base
3. **Urgent Care Intake Agent** — collects urgent care intake fields from its knowledge base
4. **Insurance Verification Agent** — verifies coverage using the covered plans knowledge base
 
## Multilingual Support
 
The triage router detects the patient's language and instructs collaborator agents to continue in that language.
