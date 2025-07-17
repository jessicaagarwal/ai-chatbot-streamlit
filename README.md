# 🤖 AI Chatbot using Streamlit & Groq API

A simple AI-powered chatbot built with **Streamlit** and **Groq API**, leveraging **LLM models** like `llama-3.3-70b-versatile`. This project demonstrates how to integrate **Groq API** with a Python web app.

---

## 🚀 Features
- **Interactive Chat UI** with Streamlit
- **Powered by Groq API**
- **Supports LLaMA models**
- **Environment-based API key management**

---

## 🛠 Tech Stack
- **Frontend:** Streamlit
- **Backend:** Python
- **LLM Provider:** Groq API

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

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## ⚙️ Configuration

### 1. Create `.env` file
Inside the root folder, create a `.env` file and add your **Groq API Key**:
```
GROQ_API_KEY=your_api_key_here
```

> **Get API Key:** [https://console.groq.com/keys](https://console.groq.com/keys)

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

## 📁 Project Structure
```
├── app.py                # Main Streamlit App
├── requirements.txt      # Dependencies
├── .env                  # Environment Variables
└── README.md             # Documentation
```

---

## 🧩 Example `app.py`
```python
import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.title("🤖 AI Chatbot with Groq + Streamlit")
prompt = st.text_area("Ask me anything:")

if st.button("Send"):
    with st.spinner("Generating response..."):
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatilet",
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        st.success(response.choices[0].message.content)
```

---

## ✅ Requirements
- Python 3.10+
- Streamlit
- Groq Python SDK
- python-dotenv

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
