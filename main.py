from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
import json
import os  # ADD this line

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class GoalRequest(BaseModel):
    goal: str

@app.get("/")
def read_root():
    return {"message": "Hello from TaskWizard Server!"}

@app.post("/generate-steps")
def generate_steps(request: GoalRequest):
    user_goal = request.goal
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "tinyllama:latest",
                "prompt": f"Break down the goal '{user_goal}' into a clear step-by-step plan.",
                "stream": True
            },
            stream=True
        )

        full_response = ""
        for chunk in response.iter_lines():
            if chunk:
                data = json.loads(chunk.decode())
                full_response += data.get("response", "")

        return {"steps": full_response}
    
    except Exception as e:
        return {"error": f"Failed to generate steps: {str(e)}"}

# 🚀 Add this at the bottom
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))  # 📢 Try to get PORT from env else fallback 8000
    uvicorn.run("main:app", host="0.0.0.0", port=port)