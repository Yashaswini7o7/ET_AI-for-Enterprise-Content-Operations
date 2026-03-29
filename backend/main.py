from fastapi import FastAPI
from agents.generator import generate_content
from agents.compliance import check_compliance
from agents.translator import translate_content

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Content Ops Running (Offline Mode)"}

@app.post("/process")
def process(topic: str):
    content = generate_content(topic)

    compliance = check_compliance(content)

    if not compliance["approved"]:
        return {
            "status": "rejected",
            "issues": compliance["issues"],
            "content": content
        }

    translated = translate_content(content)

    return {
        "status": "approved",
        "original": content,
        "translated": translated
    }
