import requests
import os
from dotenv import load_dotenv

load_dotenv()


def get_iam_token() -> str:
    resp = requests.post(
        "https://iam.cloud.ibm.com/identity/token",
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        data=(
            "grant_type=urn:ibm:params:oauth:grant-type:apikey"
            f"&apikey={os.getenv('IBM_API_KEY')}"
        )
    )
    resp.raise_for_status()
    return resp.json()["access_token"]


def chat_with_agent(message: str, token: str) -> dict:
    resp = requests.post(
        f"{os.getenv('WXO_HOST')}/v1/chat",
        headers={"Authorization": f"Bearer {token}"},
        json={
            "message": message,
            "agentId": os.getenv("AGENT_ID"),
            "agentEnvironmentId": os.getenv("AGENT_ENVIRONMENT_ID"),
        }
    )
    resp.raise_for_status()
    return resp.json()
