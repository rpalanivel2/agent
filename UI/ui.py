import streamlit as st
from agent.main import call_agent
from tools.ingestion import ingest_document


def ui():
    st.set_page_config(page_title="Weather Agent", page_icon="🤖")

    st.title("🌤️ Weather Agent ")

    # -----------------------------
    # Sidebar — Context Configuration
    # -----------------------------
    st.sidebar.header("⚙️ Agent Settings")

    # Defaults stored in session state
    if "user_id" not in st.session_state:
        st.session_state.user_id = "123"
    if "user_name" not in st.session_state:
        st.session_state.user_name = ""

    st.session_state.user_id = st.sidebar.text_input(
        "User ID",
        value=st.session_state.user_id,
    )

    st.session_state.user_name = st.sidebar.text_input(
        "User Name",
        value=st.session_state.user_name,
    )

    st.sidebar.write("---")
    st.sidebar.write("These values are passed to the agent on every message.")
    st.sidebar.write("---")

    uploaded_file = st.sidebar.file_uploader("Upload a PDF document to ingest", type=["pdf"])
    if uploaded_file:
        ids = ingest_document(
            file_bytes=uploaded_file.read(),
            filename=uploaded_file.name,
        )



    # -----------------------------
    # Chat UI
    # -----------------------------
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Display existing chat history
    for role, msg in st.session_state.chat_history:
        with st.chat_message(role):
            st.write(msg)

    # Chat input area
    user_input = st.chat_input("Type your message…")

    # When the user sends a message
    if user_input:
        st.session_state.chat_history.append(("user", user_input))
        with st.chat_message("user", avatar="🧑"):
            st.write(user_input)

        agent_reply = call_agent(user_input, st.session_state.user_id, st.session_state.user_name)

        st.session_state.chat_history.append(("assistant", agent_reply))
        with st.chat_message("assistant"):
            st.write(agent_reply)
