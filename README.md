# 🤖 AI Chatbot using Streamlit & Groq API

A simple AI-powered chatbot built with **Streamlit** and **Groq API**, leveraging **LLM models** like `llama-3.3-70b-versatile`. This project demonstrates how to integrate **Groq API** with a Python web app.

---


## 🚀 Live Demo
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://ai-chatbot-app-jessicatesting.streamlit.app/)

---

## 🚀 Features
- Chat interface built with **Streamlit**
- Powered by **Groq API** using LLaMA-3
- Maintains chat history using `st.session_state`
- Supports **local development** with `.env`
- Secure deployment using **Streamlit Secrets**

---

## 🛠 Tech Stack
- **Frontend:** Streamlit
- **Backend:** Python
- **LLM Provider:** Groq API

---

## 📂 Project Structure
```
├── app.py
├── README.md
├── requirements.txt
└── .env.example
```

---

## 📦 Installation

### 1. Clone the repository
```bash
git clone https://github.com/jessicaagarwal/ai-chatbot-streamlit.git
cd ai-chatbot-streamlit
```

### 2. Create Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate   # On Mac/Linux
.venv\Scripts\activate      # On Windows
```

---


## 🔑 API Setup

### 1. Get Groq API Key
- Visit [Groq Console](https://console.groq.com/keys)
- Copy your API key

### 2. Local Development
Create `.env` file in project root:
```
GROQ_API_KEY=your_api_key_here
```

Install dependencies:
```
pip install -r requirements.txt
```

Run the app:
```
streamlit run app.py
```

### 3. Streamlit Cloud Deployment
- Add your key in **Streamlit Secrets**:
```
GROQ_API_KEY="your_api_key_here"
```

---


## ✅ requirements.txt
```
streamlit
python-dotenv
groq
httpx==0.27.0
```

---

## ▶️ Run the App
```bash
streamlit run app.py
```

The app will be available at:
```
http://localhost:8501
```

---

## 📚 Resources
- [Groq API Docs](https://console.groq.com/docs)
- [Streamlit Docs](https://docs.streamlit.io)

---

## 🔥 Future Enhancements
- Add **chat history**
- Deploy on **Streamlit Cloud / Render**
- Add **speech-to-text and text-to-speech**

---

### ⭐ If you like this project, give it a star on GitHub!
