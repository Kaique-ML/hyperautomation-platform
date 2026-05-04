"""FastAPI — Worker API para workflows de hiperautomação."""
from fastapi import FastAPI
from pydantic import BaseModel
from workers.email_classifier import classify_email
from workers.order_approver import evaluate_order

app = FastAPI(title="Hyperautomation Platform API")


class EmailRequest(BaseModel):
    subject: str
    body: str
    sender: str


class OrderRequest(BaseModel):
    order_id: str
    value: float
    client_id: str
    items: list[dict]


@app.post("/email/classify")
async def classify(req: EmailRequest):
    result = classify_email(req.subject, req.body, req.sender)
    return result


@app.post("/orders/evaluate")
async def evaluate(req: OrderRequest):
    result = evaluate_order(req.dict())
    return result


@app.get("/health")
def health():
    return {"status": "ok"}
