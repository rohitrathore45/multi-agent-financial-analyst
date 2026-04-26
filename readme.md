# AI Financial Analyst System (Backend)

An intelligent **AI-powered financial analysis backend** built using **LangGraph (multi-agent architecture)**, combining **Machine Learning, LLMs, and RAG memory** to analyze stock queries and generate actionable insights.

---
<img width="640" height="772" alt="Screenshot 2026-04-26 193818" src="https://github.com/user-attachments/assets/6f5e1e35-274e-489f-909c-f516e1c3c0cd" />
<img width="552" height="697" alt="Screenshot 2026-04-26 193852" src="https://github.com/user-attachments/assets/48c9c7bd-b7dc-48ac-a38c-f407f6680c75" />
<img width="559" height="690" alt="Screenshot 2026-04-26 194033" src="https://github.com/user-attachments/assets/4794199a-6037-44aa-94c6-9840893586ed" />


# Overview

This system processes natural language queries like:

```bash
Analyze AAPL
```

and returns structured financial insights:

```json
{
  "ticker": "AAPL",
  "sentiment": "neutral",
  "trend": "upward",
  "risk": "low",
  "predicted_price": 185.4,
  "decision": {
    "action": "BUY",
    "confidence": 0.75,
    "reason": "Predicted price is 3.2% higher than current"
  },
  "memory_used": [...]
}
```

---

# Architecture

The system is built using a **multi-agent pipeline (LangGraph)**:

<img width="519" height="704" alt="image" src="https://github.com/user-attachments/assets/e9110d24-efc6-4f2d-b8a8-0d6fa9c177de" />

---

# Tech Stack

* **LangGraph** → Multi-agent orchestration
* **FastAPI** → Backend API
* **yfinance** → Market data
* **Tavily API** → Financial news
* **OpenAI API** → LLM (decision + sentiment)
* **XGBoost** → Price prediction model
* **FAISS** → Vector database for memory (RAG)
* **Python** → Core language

---

# Key Features

### Multi-Agent System

* Modular agents for each task
* Clean, scalable pipeline using LangGraph

### Real-Time Market Data

* Fetches live stock data via `yfinance`

### News + Sentiment Analysis

* Retrieves latest news
* Uses LLM to classify sentiment (positive/neutral/negative)

### Feature Engineering

* Trend detection
* Moving averages
* Volatility
* Momentum

### ML-Based Forecasting

* XGBoost model predicts future stock price

### Intelligent Decision Engine

* ML-driven logic (primary)
* LLM fallback for edge cases
* Outputs structured decision JSON

### RAG Memory System

* Stores past decisions using FAISS
* Retrieves similar past analysis for context

### FastAPI Backend

* REST API for integration with frontend

---

# API Endpoints

## Analyze Stock

```http
POST /analyze
```

### Request

```json
{
  "query": "analyze TSLA"
}
```

### Response

```json
{
  "ticker": "TSLA",
  "sentiment": "positive",
  "trend": "downward",
  "risk": "high",
  "predicted_price": 373.6,
  "decision": {
    "action": "HOLD",
    "confidence": 0.5
  },
  "memory_used": [...]
}
```

---

# Project Structure

```
AI-Finance-Agent/
│
├── agents/              # All LangGraph agents
├── graph/               # Workflow + state management
├── memory/              # FAISS vector store (RAG)
├── tools/               # External integrations (yfinance)
├── app/
│   ├── api/             # FastAPI routes
│   ├── config.py        # Environment variables
│   ├── main.py          # FastAPI entry point
│   └── schema.py        # Request/response models
│
├── faiss_index/         # Persistent memory storage
├── requirements.txt
└── README.md
```

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone <your-repo-url>
cd AI-Finance-Agent
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Setup Environment Variables

Create `.env` file:

```env
OPENAI_API_KEY=your_openai_key
TAVILY_API_KEY=your_tavily_key
```

---

## 5. Run Backend

```bash
uvicorn app.main:app --reload
```

---

## 6. API Docs

Open in browser:

```text
http://127.0.0.1:8000/docs
```
---

# 🧠 How Decision Works

The system combines:

* **ML Prediction (XGBoost)**
* **Market Trend**
* **News Sentiment**
* **Risk Level**

### Logic:

* If predicted price ↑ → BUY
* If predicted price ↓ → SELL
* Small change → HOLD
* LLM handles edge cases

---

# ⚠️ Limitations

* Predictions are based on short-term historical data
* News sentiment is simplified
* Ticker resolution may not be perfect for all companies
* Not intended for real financial trading

---

# 🚀 Future Improvements

* Better ML models (LSTM / Time Series)
* Structured memory system
* Real-time streaming data
* Advanced sentiment analysis
* Portfolio optimization

---

# Author

Built as a **full-stack AI system** combining:

* Multi-agent architecture
* Machine learning
* Retrieval-augmented generation (RAG)



# Final Note
This project demonstrates how modern AI systems are built by combining:
LLMs + ML Models + Memory + APIs + Orchestration

