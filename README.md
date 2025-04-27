![Made with FastAPI](https://img.shields.io/badge/Made%20with-FastAPI-00c7b7?style=for-the-badge&logo=fastapi)
# TaskWizard Server ✨

Your personal task breakdown assistant, powered by **FastAPI** and a local **LLM** (Llama3.2 via Ollama).

## 🛠️ Features
- 🚀 FastAPI backend
- 🔥 Local LLM (Ollama) integration
- 🧠 Smart prompt engineering (goal → steps)
- 🌎 Web frontend (React Native + Expo exported)
- 🌟 100% Offline or Local server running
- 📦 Deployable to Render / Vercel / your own server

## 📂 Project Structure

taskwizard-server/
├── main.py         # FastAPI server logic
├── requirements.txt # Python dependencies
├── .gitignore
├── LICENSE
└── README.md

## ⚙️ Requirements
- Python 3.10+ ✅
- Ollama (local LLM runner) ✅
- FastAPI, Uvicorn, Requests

## 🚀 Quick Start
```bash
# Clone the repo
git clone https://github.com/prjwrld/taskwizard-server.git
cd taskwizard-server

# Install dependencies
pip install -r requirements.txt

# Start Ollama (make sure it's running)
ollama run llama3.2

# Run the FastAPI server
uvicorn main:app --reload --port 8000

	•	Visit: http://localhost:8000/docs (Swagger UI to test)

🏆 Credits
	•	FastAPI
	•	Ollama
	•	Llama 3.2B Model
