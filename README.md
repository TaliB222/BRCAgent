breast-cancer-agent/
│
├── app/
│   ├── main.py                # נקודת כניסה
│   ├── config.py              # הגדרות (API keys וכו')
│
│   ├── classifier/
│   │   ├── prompt.py
│   │   ├── classify.py
│
│   ├── decision/
│   │   ├── rules.py
│
│   ├── rag/
│   │   ├── ingest.py
│   │   ├── retrieve.py
│
│   ├── generator/
│   │   ├── prompt.py
│   │   ├── generate.py
│
│   ├── utils/
│   │   ├── json_utils.py
│
├── data/
│   ├── sample_posts.json
│
├── notebooks/
│   ├── evaluation.ipynb
│
├── requirements.txt
└── README.md

breast-cancer-agent/
│
├── app/
│   │
│   ├── main.py
│   │   └── מנהל את כל הזרימה (orchestrator)
│   │
│   ├── classifier/
│   │   ├── __init__.py
│   │   ├── prompt.py
│   │   │   └── ההוראות למודל איך לסווג
│   │   └── classify.py
│   │       └── שולח טקסט ל-LLM ומחזיר JSON
│   │
│   ├── decision/
│   │   ├── __init__.py
│   │   └── rules.py
│   │       └── מחליט אם להגיב או לא
│   │
│   ├── rag/
│   │   ├── __init__.py
│   │   └── retrieve.py
│   │       └── מחזיר ידע רלוונטי (כרגע פשוט)
│   │
│   ├── generator/
│   │   ├── __init__.py
│   │   ├── prompt.py
│   │   │   └── איך לנסח תגובה
│   │   └── generate.py
│   │       └── מייצר את התשובה
│   │
│   └── utils/
│       └── (לעתיד)
│
├── data/
│   └── sample_posts.json
│
├── requirements.txt
└── README.md

        ┌────────────────────┐
        │   User Input       │
        │  (פוסט/שאלה)       │
        └─────────┬──────────┘
                  │
                  ▼
        ┌────────────────────┐
        │   CLASSIFIER       │
        │ classify_text()    │
        └─────────┬──────────┘
                  │
                  ▼
        ┌────────────────────┐
        │   CLASSIFICATION   │
        │ JSON output        │
        │ (intent, emotion…) │
        └─────────┬──────────┘
                  │
                  ▼
        ┌────────────────────┐
        │   DECISION         │
        │ should_respond()   │
        └─────────┬──────────┘
                  │
        ┌─────────┴──────────┐
        │                    │
        ▼                    ▼
┌──────────────┐     ┌────────────────┐
│ No Response  │     │      RAG       │
│ (stop)       │     │ retrieve()     │
└──────────────┘     └───────┬────────┘
                              │
                              ▼
                    ┌────────────────────┐
                    │   CONTEXT          │
                    │ (knowledge base)   │
                    └─────────┬──────────┘
                              │
                              ▼
                    ┌────────────────────┐
                    │   GENERATOR        │
                    │ generate_response  │
                    └─────────┬──────────┘
                              │
                              ▼
                    ┌────────────────────┐
                    │   FINAL RESPONSE   │
                    └────────────────────┘


# Breast Cancer Support AI Agent

An AI agent designed to identify relevant discussions about breast cancer and respond with **empathetic, context-aware, and non-intrusive support**, optionally referencing resources such as *עמותת גנים טובים* when appropriate.

---

## 🧠 Overview

This project demonstrates an end-to-end AI system that:

* Detects whether a social media post is relevant to breast cancer
* Understands user intent and emotional tone
* Decides **whether it is appropriate to respond**
* Retrieves relevant knowledge using a basic RAG pipeline
* Generates a **sensitive, human-like response**

The system prioritizes **emotional safety, ethical considerations, and real user value** over engagement.

---

## 🎯 Key Features

* **Context-aware classification**
  Identifies intent (question, sharing, support), emotional state, and sensitivity level

* **Decision engine (guardrails)**
  Prevents responses in high-sensitivity situations (e.g., emotional distress without a question)

* **RAG (Retrieval-Augmented Generation)**
  Enhances responses with external knowledge (currently MVP-level, extensible to vector DB)

* **Tone-aware response generation**
  Produces empathetic, non-promotional replies with optional, subtle mention of relevant support resources

---

## 🏗️ Project Structure

```
app/
│
├── main.py                # Orchestrates the full pipeline
│
├── classifier/
│   ├── prompt.py          # Classification instructions for LLM
│   └── classify.py        # Runs classification
│
├── decision/
│   └── rules.py           # Determines whether to respond
│
├── rag/
│   └── retrieve.py        # Retrieves relevant knowledge (MVP)
│
├── generator/
│   ├── prompt.py          # Response generation instructions
│   └── generate.py        # Generates final response
│
└── utils/                 # (reserved for future use)
```

---

## 🔄 System Flow

1. **Input**: User-generated text (e.g., social media post)
2. **Classification**:

   * Relevance
   * Intent
   * Emotional state
   * Sensitivity level
3. **Decision**:

   * Should the agent respond?
4. **Retrieval (RAG)**:

   * Fetch relevant knowledge
5. **Generation**:

   * Produce a response aligned with tone and safety constraints

---

## ⚙️ Setup

### 1. Install dependencies

```
pip install -r requirements.txt
```

### 2. Set API key

```
export OPENAI_API_KEY=your_key
```

(Windows)

```
set OPENAI_API_KEY=your_key
```

### 3. Run the agent

```
python -m app.main
```

---

## 🧪 Example

**Input:**

```
"יש למישהי ניסיון עם תופעות לוואי של הקרנות?"
```

**Output:**

```
תגובה אמפתית עם מידע רלוונטי, ובמידת הצורך אזכור עדין של משאבים תומכים
```

---

## ⚠️ Ethical Considerations

This system is designed with strict constraints:

* Does **not provide medical advice**
* Avoids responding in high emotional distress scenarios
* Prevents promotional or intrusive behavior
* Prioritizes user well-being over engagement

---

## 🚀 Future Improvements

* Vector database (FAISS / Pinecone) for real RAG
* Evaluation pipeline (precision/recall on response decisions)
* Memory and multi-turn conversation support
* Integration with real social platforms APIs
* Fine-tuned classification models

---

## 💡 Why This Project?

This project combines:

* NLP & LLMs
* Healthcare sensitivity
* Product thinking
* Responsible AI design

It reflects real-world challenges in deploying AI systems in emotionally sensitive domains.

---

## 👤 Authors



---
