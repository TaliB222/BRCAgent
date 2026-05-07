🧬 Breast Cancer AI Assistant (RAG + Flask)

An AI-powered full stack system that analyzes social media–like text related to breast cancer and women’s health, and generates empathetic, safe, and knowledge-grounded responses using a modular AI pipeline and a retrieval-augmented generation (RAG) architecture.

📌 Project Overview

This project simulates a real-world healthcare AI assistant designed to:

Detect whether a user message is medically relevant
Classify intent, emotional state, and sensitivity level
Decide whether the system should respond
Retrieve relevant medical knowledge (RAG layer)
Generate a safe and empathetic response
Expose everything via a Flask web interface
🧠 System Architecture
User (Web UI)
      ↓
Flask Backend (routes.py)
      ↓
Classifier → Decision Layer
      ↓
RAG (retrieve_context)
      ↓
LLM Generator (OpenAI GPT)
      ↓
Response UI
⚙️ Key Components
1️⃣ Classifier
Analyzes user text
Detects:
relevance (breast cancer / menopause / etc.)
intent (question, sharing, support)
emotional tone
sensitivity level
2️⃣ Decision Layer
Applies safety rules
Determines whether the system should respond
Prevents unsafe or inappropriate outputs
3️⃣ RAG (Retrieval Module)
Loads medical knowledge from local .txt files
Retrieves relevant context for the model
Currently rule-based (MVP version)
Designed to evolve into embedding-based retrieval
4️⃣ Generator (LLM)
Uses GPT-based model
Produces empathetic and safe responses
Grounded in retrieved knowledge
Avoids medical diagnosis or direct advice
5️⃣ Flask Web App
Simple UI for user interaction
Collects structured medical parameters:
Age
Cancer type
BRCA status
Disease stage
Free text input
🖥️ UI Features
Simple web form
Real-time AI response
Clean static HTML/CSS interface
Designed for accessibility and emotional safety
📂 Project Structure
Breast_cancer_agent/
│
├── app/
│   ├── classifier/
│   ├── decision/
│   ├── generator/
│   ├── rag/
│   ├── routes.py
│   └── __init__.py
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
├── data/
│   └── websites/
│
├── run.py
└── README.md
