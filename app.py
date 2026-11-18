
import streamlit as st
from groq import Groq

# ----------------------------------
# PAGE CONFIGURATION
# ----------------------------------

st.set_page_config(
    page_title="Klyro",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------------
# AI CONFIGURATION
# ----------------------------------

MODEL = "openai/gpt-oss-20b"

client = Groq(
    api_key=st.secrets["GROQ_API_KEY"]
)

SYSTEM_PROMPT = """
You are Klyro, an intelligent, friendly and helpful
AI assistant.

Your responsibilities:
- Answer questions accurately and clearly.
- Help users with programming and problem-solving.
- Explain difficult concepts in simple language.
- Be creative when brainstorming.
- Admit when you are uncertain.
- Use the language preferred by the user.
"""

# ----------------------------------
# CUSTOM CSS
# ----------------------------------

st.markdown("""
<style>

/* Main background */
.stApp {
    background: radial-gradient(
        ellipse at 65% 25%,
        #422344 0%,
        #1b101f 43%,
        #0c0a0f 85%
    );
    color: #f7f4fa;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: #080809;
    border-right: 1px solid #242026;
}

/* Main content */
.block-container {
    max-width: 1100px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* Hide Streamlit menu */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

/* Brand */
.klyro-brand {
    font-size: 25px;
    font-weight: 750;
    letter-spacing: -1px;
    color: white;
}

/* Hero */
.hero {
    text-align: center;
    padding-top: 11vh;
    padding-bottom: 3rem;
}

.orb {
    width: 85px;
    height: 85px;
    margin: 0 auto 28px;
    border-radius: 50%;
    background: radial-gradient(
        circle at 30% 25%,
        #f0c5ff,
        #a14ad8 30%,
        #43157c 60%,
        #1266d1 85%
    );
    box-shadow:
        0 0 35px #a34de866,
        inset -12px -12px 22px #180830;
}

.hero-title {
    font-size: clamp(30px, 4vw, 45px);
    font-weight: 500;
    letter-spacing: -1.5px;
    margin-bottom: 12px;
}

.hero-subtitle {
    font-size: 15px;
    color: #aaa0b0;
}

/* Feature cards */
.feature-card {
    background: #100d13;
    border: 1px solid #302735;
    border-radius: 18px;
    padding: 24px;
    min-height: 145px;
}

.feature-icon {
    font-size: 25px;
    color: #c188f3;
    margin-bottom: 13px;
}

.feature-title {
    font-size: 16px;
    font-weight: 600;
    margin-bottom: 8px;
}

.feature-description {
    color: #a8a0ac;
    font-size: 13px;
    line-height: 1.6;
}

/* Chat input */
[data-testid="stChatInput"] {
    border: 1px solid #9d65ae;
    border-radius: 18px;
    background: #201721;
}

[data-testid="stChatInput"]:focus-within {
    border-color: #d5a0ee;
    box-shadow: 0 0 15px #9f5aca33;
}

/* Buttons */
.stButton > button {
    border-radius: 12px;
    border: 1px solid #343039;
    background: #252129;
    color: white;
}

.stButton > button:hover {
    border-color: #ab76ca;
    color: white;
}

/* Chat messages */
[data-testid="stChatMessage"] {
    background: #17121b;
    border: 1px solid #302735;
    border-radius: 16px;
}

</style>
""", unsafe_allow_html=True)

# ----------------------------------
# SESSION STATE
# ----------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# ----------------------------------
# SIDEBAR
# ----------------------------------

with st.sidebar:

    st.markdown(
        '<div class="klyro-brand">✦ Klyro</div>',
        unsafe_allow_html=True
    )

    st.write("")

    if st.button(
        "＋ New Chat",
        use_container_width=True
    ):
        st.session_state.messages = []
        st.rerun()

    st.write("")
    st.caption("WORKSPACE")
    st.write("◈  Chat")
    st.write("▤  Your conversations")

    st.divider()

    st.caption("KLYRO")
    st.write("Your intelligent everyday assistant.")

    st.write("")
    st.caption("Powered by GPT-OSS 20B")
    st.caption("Version 1.0")

# ----------------------------------
# MAIN INTERFACE
# ----------------------------------

if not st.session_state.messages:

    st.markdown("""
    <div class="hero">
        <div class="orb"></div>
        <div class="hero-title">
            Ready to Create Something New?
        </div>
        <div class="hero-subtitle">
            Ask questions. Explore ideas. Create without limits.
        </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">✧</div>
            <div class="feature-title">Brainstorm</div>
            <div class="feature-description">
                Explore ideas and discover new possibilities.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">⌘</div>
            <div class="feature-title">Create Code</div>
            <div class="feature-description">
                Turn ideas into practical solutions.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">◈</div>
            <div class="feature-title">Explore</div>
            <div class="feature-description">
                Learn, discover and understand complex topics.
            </div>
        </div>
        """, unsafe_allow_html=True)

# ----------------------------------
# DISPLAY CHAT HISTORY
# ----------------------------------

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ----------------------------------
# CHAT INPUT
# ----------------------------------

prompt = st.chat_input("✦ Ask Klyro anything...")

if prompt:

    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display AI response
    with st.chat_message("assistant"):

        try:

            messages = [
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                *st.session_state.messages
            ]

            # Request streaming response
            stream = client.chat.completions.create(
                model=MODEL,
                messages=messages,
                temperature=0.6,
                reasoning_effort="low",
                max_completion_tokens=4096,
                stream=True
            )

            # Generate text chunk by chunk
            def generate_response():
                for chunk in stream:
                    if chunk.choices:
                        content = chunk.choices[0].delta.content

                        if content:
                            yield content

            # Display streaming response
            answer = st.write_stream(generate_response)

            # Save assistant response
            st.session_state.messages.append({
                "role": "assistant",
                "content": answer
            })

        except Exception as error:

            st.error(
                "Klyro couldn't generate a response. "
                "Please try again."
            )

            st.caption(str(error))

            # Remove failed user request from history
            st.session_state.messages.pop()
