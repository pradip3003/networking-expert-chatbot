import streamlit as st
from google import genai


#  GEMINI API KEY

API_KEY = "AIzaSyD3khLyYyA8dt2QuUL8DA5FRKClgd2Ai0s"

client = genai.Client(api_key=API_KEY)


#  Networking Expert Logic 

def ask_networking(question):
    try:
        prompt = f"""
You are a COMPUTER NETWORKING EXPERT.

Answer ONLY computer networking related questions.
Topics include:
- OSI Model
- TCP/IP
- DNS, DHCP, ARP
- Subnetting
- Routing and Switching
- TCP vs UDP
- HTTP / HTTPS
- CCNA / interview concepts

If the question is NOT networking related, reply exactly:
"I can answer only computer networking questions."

Explain clearly with examples.

Question:
{question}
"""
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"❌ Gemini Error: {e}"


st.set_page_config(
    page_title="Networking Expert",
    page_icon="🌐",
    layout="centered"
)


st.markdown("""
<style>
/* App Background */
.stApp {
    background-color: #0f172a;
    color: #e5e7eb;
}

/* Center content */
.block-container {
    max-width: 820px;
    padding-bottom: 7rem;
}

/* Chat message spacing */
[data-testid="stChatMessage"] {
    padding: 0.2rem 0;
}

/* Assistant bubble */
[data-testid="stChatMessage"][data-role="assistant"] .stMarkdown {
    background: #020617;
    padding: 14px 18px;
    border-radius: 14px;
    max-width: 95%;
    line-height: 1.6;
}

/* User bubble */
[data-testid="stChatMessage"][data-role="user"] {
    display: flex;
    justify-content: flex-end;
}

[data-testid="stChatMessage"][data-role="user"] .stMarkdown {
    background: #2563eb;
    padding: 14px 18px;
    border-radius: 14px;
    max-width: 95%;
    color: white;
    line-height: 1.6;
}

/* Chat Input fixed bottom */
[data-testid="stChatInput"] {
    position: fixed;
    bottom: 0;
    left: 50%;
    transform: translateX(-50%);
    width: 100%;
    max-width: 820px;
    background: #0f172a;
    padding: 0.8rem 1rem;
    border-top: 1px solid #1e293b;
    z-index: 100;
}

/* Input box */
[data-testid="stChatInput"] textarea {
    background: #020617;
    color: #e5e7eb;
    border-radius: 14px;
    padding: 12px;
    font-size: 15px;
}

/* Placeholder */
[data-testid="stChatInput"] textarea::placeholder {
    color: #9ca3af;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #020617;
}

/* Remove footer */
footer {
    display: none;
}

/* Mobile responsiveness */
@media (max-width: 768px) {
    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
    }
}
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("## 🌐 Networking Expert")
    st.markdown(
        """
        **AI-powered chatbot** for  
        Computer Networking concepts.

        **Covers:**
        - OSI Model  
        - TCP/IP  
        - DNS, DHCP, ARP  
        - Subnetting  
        - CCNA & Interview Qs
        """
    )

    if st.button("🧹 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

    st.markdown("---")
    st.markdown("👨‍💻 Built with Streamlit + Gemini")


st.markdown(
    "<h2 style='text-align:center;'>🌐 Networking Expert Chatbot</h2>",
    unsafe_allow_html=True
)

if "messages" not in st.session_state:
    st.session_state.messages = []

if not st.session_state.messages:
    st.session_state.messages.append({
        "role": "assistant",
        "content": "👋 Ask me any computer networking question."
    })

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Ask networking question...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    if user_input.lower() in ["exit", "quit", "bye"]:
        reply = "👋 Bye! Best of luck for your networking journey."
    else:
        reply = ask_networking(user_input)

    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.rerun()
