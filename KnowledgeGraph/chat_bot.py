import streamlit as st
import ollama
st.sidebar.title("Ollama Python Chatbot")

#initilize history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

#init models
if "model" not in st.session_state:
    st.session_state["model"] = ""

models = [model["name"] for model in ollama.list()["models"]]
selectedModel = st.sidebar.selectbox("Choose your model", models)
if selectedModel:
    st.session_state["model"] = selectedModel
    st.session_state["messages"] = []


def model_response_generator():
    stream = ollama.chat(
        model=st.session_state["model"],
        messages=st.session_state["messages"],
        stream=True,
    )
    for chunk in stream:
        yield chunk["message"]["content"]


# Display chat messages from history on app rerun
for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input(placeholder="Type your message")

if prompt:
    #add latest message to history in format {role, content}

    with st.chat_message("user"):
        st.markdown(prompt)
        st.session_state["messages"].append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        message = st.write_stream(model_response_generator())
        st.session_state["messages"].append({"role": "assistant", "content": message})
