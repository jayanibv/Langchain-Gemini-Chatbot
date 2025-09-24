# LangChain + Gemini + Gradio Chatbot 🤖

A simple chatbot built with **LangChain**, **Google Gemini API**, and **Gradio** as the user interface.

---

## 🚀 Features
- Uses **Google Gemini 1.5 models** (`gemini-1.5-flash` / `gemini-1.5-pro`)
- Supports **multi-turn conversations** with memory
- Web UI powered by **Gradio v5**
- Lightweight & easy to deploy locally

---

## 📦 Requirements

- Python 3.11 (recommended)
- Google Gemini API key ([Get it here](https://aistudio.google.com/app/apikey))

---

## 🔧 Installation

1. **Clone the repo**
   ```bash
   git clone https://github.com/your-username/langchain-gemini-chatbot.git
   cd langchain-gemini-chatbot

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   venv\Scripts\activate   # On Windows
   source venv/bin/activate  # On Linux/Mac
   
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
---

## 🔑 Setup

1. Get your Gemini API key from  ([Google AI Studio](https://aistudio.google.com/app/apikey))

2. Open chatbot.py and replace:
   ```bash
   os.environ["GOOGLE_API_KEY"] = "your_api_key_here"
with your actual API key.

3. Alternatively, you can set it as an environment variable:
   ```bash
   # Windows
   setx GOOGLE_API_KEY "your_api_key_here"
   # Linux/Mac
   export GOOGLE_API_KEY="your_api_key_here"

---

## 🚀 Run the Chatbot

1. To start the chatbot, run:
   ```bash
   python chatbot.py

---
## This will start a local Gradio server:

Running on local URL: http://127.0.0.1:7860

👉 Open it in your browser and start chatting! 🎉
