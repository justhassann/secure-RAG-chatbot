# 🛡️ Secure Corporate RAG Chatbot

A secure, enterprise-grade AI chatbot utilizing Retrieval-Augmented Generation (RAG). This project demonstrates the implementation of **Secure Software Design (SSD)** principles within a modern AI application.

## 🚀 Features

### 🧠 AI & RAG Capabilities
- **LLM Engine:** Local Ollama integration (Llama 3.1).
- **Vector Search:** Semantic search using `sentence-transformers`.
- **RBAC Filtering:** Documents are filtered based on user Department before retrieval.

### 🔒 Security Implementations (SSD)
This project implements a "Defense-in-Depth" architecture:
1.  **Identity:** JWT Authentication with 2FA (TOTP).
2.  **Secrets Management:** Auto-generated strong keys; Secrets encrypted at rest (Fernet).
3.  **Accountability:** Comprehensive Audit Logging (Login, Logout, Access).
4.  **Network:** Enforced HTTPS/TLS, HSTS, and CSP Headers.
5.  **Resilience:** Rate Limiting to prevent DoS and Brute Force attacks.
6.  **Session Security:** Token Blacklisting on Logout.

## 🛠️ Installation

### Prerequisites
- Python 3.9+
- [Ollama](https://ollama.com/) installed and running (`ollama pull llama3.1`)

### Setup
1.  **Clone the repo:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/secure-rag-chatbot.git](https://github.com/YOUR_USERNAME/secure-rag-chatbot.git)
    cd secure-rag-chatbot
    ```
2.  **Install Dependencies:**
    ```bash
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```
3.  **Generate SSL Certificates (for HTTPS):**
    ```bash
    openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes -subj "/CN=localhost"
    ```
4.  **Initialize Database:**
    ```bash
    python init_db.py
    # Copy the generated Admin passwords from the terminal output!
    ```

## ▶️ Usage

Run the server in **Secure Mode** (HTTPS enabled):
```bash
uvicorn main:app --reload --ssl-keyfile key.pem --ssl-certfile cert.pem
