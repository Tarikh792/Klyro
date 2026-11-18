# ✦ Klyro

**Think. Create. Beyond.**

Klyro is a conversational AI web application built with Python, Streamlit, and GroqCloud. It combines a modern dark-themed interface with large language model integration to deliver interactive, context-aware conversations.

## Features

- **AI Conversations:** Powered by GPT-OSS 20B through GroqCloud.
- **Streaming Responses:** Displays AI-generated answers progressively.
- **Conversation History:** Maintains chat context during the active session.
- **Dark Minimal Interface:** Custom CSS, purple gradients, and responsive layout.
- **New Chat:** Start a fresh conversation instantly.
- **Secure Configuration:** API credentials are managed through Streamlit Secrets.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Application logic |
| Streamlit | Web interface |
| Custom CSS | UI styling |
| GroqCloud | LLM inference |
| GPT-OSS 20B | Language model |
| Git & GitHub | Version control |

## Project Architecture

```text
User
  |
  v
Streamlit Interface
  |
  v
Python Application
  |
  +-- Session State (Chat History)
  |
  v
GroqCloud API
  |
  v
GPT-OSS 20B
  |
  v
Streaming AI Response
```

## Getting Started

**1. Clone the repository**

```bash
git clone https://github.com/Tarikh792/Klyro.git
cd Klyro
```

**2. Install dependencies**

```bash
python -m pip install -r requirements.txt
```

**3. Configure API credentials**

Create `.streamlit/secrets.toml`:

```toml
GROQ_API_KEY = "your_groq_api_key"
```

Never commit your API key to version control.

**4. Launch the application**

```bash
python -m streamlit run app.py
```

## Current Limitations

- Chat history is stored only for the current session.
- AI responses depend on GroqCloud's API availability and rate limits.
- The application does not train or host its own foundation model.
- Authentication, persistent storage, and automated evaluation are not yet implemented.

## Future Improvements

- Persistent conversations with SQLite
- User authentication
- Document question-answering
- Automated AI evaluations
- Improved error handling and observability

## Developer

**Syed Ali Tarikh**

BS Artificial Intelligence — SZABIST Islamabad

[GitHub Profile](https://github.com/Tarikh792)

---

*Built to explore practical AI application engineering, LLM integration, and modern Python development.*
