# TaskWizard – Server

FastAPI + Ollama endpoint that turns any goal into a step-by-step roadmap.

## Quick start (local)

```bash
ollama serve                       # terminal 1 – starts model API on :11434
pip install -r requirements.txt
uvicorn main:app --reload --port 8000 
```