# 🤖 AI Chatbot using Streamlit & Groq API

A **personalized AI-powered chatbot** built with **Streamlit** and **Groq API**, leveraging **LLaMA-3 models**. This project demonstrates **LLM integration**, **prompt customization**, and a **friendly UI with mood-based interaction**.

---

## 🚀 Live Demo
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://ai-chatbot-app-jessicatesting.streamlit.app/)

---

## ✨ Features  
✅ Chat interface built with **Streamlit**  
✅ Powered by **Groq API** using `llama-3.3-70b-versatile`  
✅ **Personalization** – Add your name & mood  
✅ **Dynamic system role** for better context handling  
✅ **Creativity control** with `temperature` slider  
✅ **Few-shot examples toggle** for better responses  
✅ Maintains **chat history** using `st.session_state`  
✅ Secure deployment using **Streamlit Secrets**  
✅ **Dark theme UI** with friendly emoji responses

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
- [Prompt Engineering Guide](https://www.promptingguide.ai/)

---

## 🔥 Future Enhancements
- Export **chat history**
- Deploy on **Render/ Vercel**
- Add **speech-to-text and text-to-speech**
- Add Multi-LLM Support (OpenAI, Claude, Gemini)

---

### ⭐ If you like this project, give it a star on GitHub!
