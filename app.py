import os
import json
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

# Setup
load_dotenv()
GROQ_API_KEY = st.secrets.get("GROQ_API_KEY") or os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    st.error("❌ API key is missing! Add it in `.streamlit/secrets.toml` or `.env`.")
    st.stop()

client = Groq(api_key=GROQ_API_KEY)

st.set_page_config(page_title="AI Chatbot", page_icon="🤖")
st.title("🤖 ChatGPT-like Assistant (Groq LLaMA‑3)")

# Sidebar Controls
st.sidebar.header("⚙️ Settings")

user_name = st.sidebar.text_input("👤 Your Name", "")
mood = st.sidebar.selectbox("😊 How are you feeling?", ["Neutral", "Happy", "Sad", "Stressed"])

system_role_input = st.sidebar.text_area("System Role:", "You are a helpful assistant.")
temperature = st.sidebar.slider("Creativity (temperature):", 0.0, 1.0, 0.7)
few_shot = st.sidebar.checkbox("Enable Few-Shot Examples")

# Clear chat
if st.sidebar.button("🗑 Clear Chat"):
    st.session_state.messages = []
    st.rerun()

# Download buttons (only if chat exists)
if "messages" in st.session_state and st.session_state.messages:
    chat_txt = "\n".join([f"{m['role'].title()}: {m['content']}" for m in st.session_state.messages])
    chat_json = json.dumps(st.session_state.messages, indent=2, ensure_ascii=False)

    st.sidebar.download_button(
        "⬇ Download Chat (.txt)",
        data=chat_txt,
        file_name="chat_history.txt",
        mime="text/plain",
    )
    st.sidebar.download_button(
        "⬇ Download Chat (.json)",
        data=chat_json,
        file_name="chat_history.json",
        mime="application/json",
    )

# Few-Shot Examples (pattern shaping)
few_shot_examples = [
    {"role": "user", "content": "What is AI?"},
    {"role": "assistant", "content": "AI stands for Artificial Intelligence, which lets machines do tasks that seem smart—like recognizing images or answering questions."},
    {"role": "user", "content": "Explain LLM in simple words."},
    {"role": "assistant", "content": "An LLM is a Large Language Model (like ChatGPT) that reads lots of text and learns to talk like people."},
]

# Build personalized system prompt FRESH each rerun (avoid stacking)
system_role = system_role_input.strip()
if user_name:
    system_role += f" Always call the user '{user_name}'."
if mood != "Neutral":
    system_role += f" The user feels {mood}. Respond in an empathetic, encouraging way."

# Session State
if "messages" not in st.session_state:
    st.session_state.messages = []  # store ONLY user & assistant turns

# Render existing history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
user_input = st.chat_input("Type your question...")

if user_input:
    # 1. store + render user turn
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # 2. build LLM context
    context = [{"role": "system", "content": system_role}]
    if few_shot:
        context += few_shot_examples
    context += st.session_state.messages  # includes latest user turn

    # 3. call Groq
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            resp = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                temperature=temperature,
                messages=context,
            )
            answer = resp.choices[0].message.content or ""

            # prepend emoji if missing (human touch)
            if not answer.startswith("✨"):
                answer = "✨ " + answer

            st.markdown(answer)

    # 4. save assistant turn (with emoji so history looks the same)
    st.session_state.messages.append({"role": "assistant", "content": answer})

# Style tweaks (layout + full-width chat input)
st.markdown(
    """
    <style>
    /* Main container full width */
    .block-container {
        max-width: 95% !important;
        padding-left: 2rem;
        padding-right: 2rem;
    }
    
    /* Chat input full width & bigger */
    [data-testid="stChatInput"] {
        width: 100% !important;
        margin-top: 1rem !important;
    }
    [data-testid="stChatInput"] textarea {
        font-size: 1.1rem !important;
        padding: 0.75rem !important;
        border-radius: 10px !important;
    }
    
    /* Chat messages styling */
    [data-testid="stChatMessage"] {
        border-radius: 10px;
        padding: 0.75rem 1rem;
        margin: 0.5rem 0;
        font-size: 1rem;
    }
    
    /* Assistant message color */
    [data-testid="stChatMessage"][data-testid="stChatMessage-assistant"] {
        background: #222; /* darker for contrast */
        color: #fff;
    }
    
    /* User message color */
    [data-testid="stChatMessage"][data-testid="stChatMessage-user"] {
        background: #3a3a3a;
        color: #fff;
    }
    
    /* Sidebar tweak */
    section[data-testid="stSidebar"] {
        width: 280px;
    }
    </style>
    """, 
unsafe_allow_html=True
)
