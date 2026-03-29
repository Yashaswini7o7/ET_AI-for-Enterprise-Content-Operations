# 🧠 AI Content Operations System

## Features
- AI Content Generation
- Compliance Checking
- Multi-language Translation
- Streamlit UI

---

## Setup Instructions

### 1. Clone / Create Project
Create folder:
ai-content-ops

Paste all files accordingly.

---

### 2. Backend Setup
cd backend

Install dependencies:
pip install -r requirements.txt

Run server:
uvicorn main:app --reload

---

### 3. Frontend Setup
cd frontend

Install dependencies:
pip install -r requirements.txt

Run UI:
streamlit run app.py

---

## Environment Variable

Set your OpenAI API Key:

### Mac/Linux
export OPENAI_API_KEY=your_key

### Windows
set OPENAI_API_KEY=your_key

---

## Access

Backend:
http://localhost:8000

Frontend:
http://localhost:8501
