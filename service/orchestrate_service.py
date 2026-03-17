import requests
import yaml
import json
from pathlib import Path

ENV_NAME = "hackathon"


def load_credentials() -> tuple[str, str]:
    """Read the instance URL and JWT token from the ADK's cached config files."""
    config_path = Path.home() / ".config" / "orchestrate" / "config.yaml"
    creds_path = Path.home() / ".cache" / "orchestrate" / "credentials.yaml"

    with open(config_path) as f:
        config = yaml.safe_load(f)

    with open(creds_path) as f:
        creds = yaml.safe_load(f)

    wxo_url = config["environments"][ENV_NAME]["wxo_url"]
    token = creds["auth"][ENV_NAME]["wxo_mcsp_token"]

    return wxo_url, token


def chat_with_agent(
    message: str,
    agent_id: str,
    thread_id: str | None,
    wxo_url: str,
    token: str,
) -> tuple[str, str | None]:
    """Send a message to any Orchestrate agent via /v1/orchestrate/runs and return the reply."""
    url = f"{wxo_url}/v1/orchestrate/runs"

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    payload = {
        "message": {
            "role": "user",
            "content": message,
        },
        "agent_id": agent_id,
    }

    if thread_id:
        payload["thread_id"] = thread_id

    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()

    data = response.json()

    # Non-streaming returns run IDs; need to poll for the result
    run_id = data.get("run_id")
    new_thread_id = data.get("thread_id", thread_id)

    if not run_id:
        return "No run_id received from the agent.", new_thread_id

    # Poll for the completed run
    result_url = f"{wxo_url}/v1/orchestrate/runs/{run_id}"
    reply = ""

    for _ in range(30):  # Poll up to 30 times (~30 seconds)
        import time
        time.sleep(1)

        result_response = requests.get(result_url, headers=headers)
        result_response.raise_for_status()
        result_data = result_response.json()

        status = result_data.get("status", "")

        if status == "completed":
            # Extract the message content
            result_msg = result_data.get("result", {}).get("data", {}).get("message", {})
            content_list = result_msg.get("content", [])
            for block in content_list:
                text = block.get("text", "")
                if text:
                    reply += text
            break
        elif status in ("failed", "cancelled", "expired"):
            error = result_data.get("last_error", "Unknown error")
            reply = f"Agent run {status}: {error}"
            break

    if not reply:
        reply = "No response received from the agent (timeout)."

    return reply, new_thread_id
