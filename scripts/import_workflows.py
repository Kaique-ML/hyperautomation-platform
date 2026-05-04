"""Importa workflows JSON para o n8n via API."""
import argparse
import json
import os
import requests
from pathlib import Path


def import_workflows(n8n_url: str, workflows_dir: str = "workflows"):
    session = requests.Session()
    session.auth = ("admin", os.getenv("N8N_PASSWORD", "admin123"))

    for wf_file in Path(workflows_dir).glob("*.json"):
        with open(wf_file) as f:
            workflow = json.load(f)
        resp = session.post(f"{n8n_url}/api/v1/workflows", json=workflow)
        if resp.status_code in (200, 201):
            print(f"✅ Importado: {wf_file.name}")
        else:
            print(f"❌ Erro em {wf_file.name}: {resp.text}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--n8n-url", default="http://localhost:5678")
    parser.add_argument("--dir", default="workflows")
    args = parser.parse_args()
    import_workflows(args.n8n_url, args.dir)
