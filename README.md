# 🔄 Hyperautomation Platform — n8n + Python + AI Agents
> Plataforma de hiperautomação: n8n para low-code + Python para lógica complexa + IA para decisões

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)](https://python.org)
[![n8n](https://img.shields.io/badge/n8n-1.40-EA4B71)](https://n8n.io)
[![CrewAI](https://img.shields.io/badge/CrewAI-Agents-FF6B35)](https://crewai.com)
[![Docker](https://img.shields.io/badge/Docker-ready-2496ED?logo=docker)](https://docker.com)

## 🎯 Sobre

Plataforma que combina **n8n** (automação visual low-code) com **agentes Python+IA** para processos que exigem raciocínio.

**Workflows incluídos:**
- 📧 Triagem inteligente de e-mails com classificação por IA
- 📋 Aprovação automática de pedidos com regras + IA
- 📊 Sync bidirecional CRM → Planilhas → Slack
- 🔔 Monitoramento de SLA com escalonamento automático

## 🛠️ Stack

| Componente | Tech |
|-----------|------|
| Low-code | n8n 1.40 (self-hosted) |
| Python Workers | FastAPI + Celery |
| IA | OpenAI GPT-4o + CrewAI |
| Mensageria | RabbitMQ |
| Banco | PostgreSQL + Redis |

## 🚀 Rodando

```bash
git clone https://github.com/Kaique-ML/hyperautomation-platform
cd hyperautomation-platform

cp .env.example .env
docker compose up --build
# n8n UI: http://localhost:5678
# API:    http://localhost:8000/docs

python scripts/import_workflows.py --n8n-url http://localhost:5678
```

---
**Gabriel Kaique Portel Silva** | [LinkedIn](https://linkedin.com/in/gabriel-kaique-881475284) | [GitHub](https://github.com/Kaique-ML)
