
import base64
import gc
import random
import tempfile
import time
import uuid

import streamlit as st

from rag.client import RAGClient

model = 'zephyr'

if 'id' not in st.session_state:
    st.session_state.id = uuid.uuid4()
    st.session_state.file_cache = {}

session_id = st.session_state.id
client = None

def reset_chat():
    st.session_state.messages = []
    st.session_state.context = None
    gc.collect()

def display_pdf(file):
    st.markdown('### PDF Preview')
    base64_pdf = base64.b64encode(file.read()).decode('utf-8')

    # Emedding PDF in HTML
    pdf_display = f"""<iframe src= "data:application/pdf;base64,{base64_pdf}" width = "400" height = "100%" type="application/pdf"
                        style = "height:100vh; width:100%
                        >
                    <iframe>"""

    # display the file
    st.markdown(pdf_display, unsafe_allow_html=True)

with st.sidebar:
    uploaded_file = st.file_uploader('choose you `.pdf` file', type = 'pdf')
    if uploaded_file is not None:
        with tempfile.NamedTemporaryFile() as temp_file, st.status(
            'Processing document', expanded=False, state='running'
        ):

            with open(temp_file.name, 'wb') as f:
                f.write(uploaded_file.getvalue())

            file_key = f'{session_id}-{uploaded_file.name}'
            st.write("Indexing")
            if file_key not in st.session_state.file_cache:
                client = RAGClient(files = temp_file.name)
                st.session_state.file_cache[file_key] = client
            else:
                client = st.session_state.file_cache[file_key]

            st.write("Complete, ask you questions...")

        display_pdf(uploaded_file)


col1, col2 = st.columns([6,1])

with col1:
    st.header(f"Chat with Document")

with col2:
    st.button("Clear ↺", on_click = reset_chat)


# Initialize the chat history
if 'messages' not in st.session_state:
    reset_chat()

# display chat messages from history on app run
for messages in st.session_state.messages:
    with st.chat_message(messages['role']):
        st.markdown(messages['content'])

# accept user input
if prompt := st.chat_input("Write Your query..."):
    if uploaded_file is None:
        st.exception(FileNotFoundError("Upload a Document First!"))
        st.stop()

    # add user message to chat history
    st.session_state.messages.append({'role':"user", 'content': prompt})

    # display user message in chat messages container
    with st.chat_message('user'):
        st.markdown(prompt)

    # display assistant response in chat message container
    with st.chat_message("assistant"):
        messages_placeholder = st.empty()
        full_response = ""
        
        # simulate stream of response with milliseconds delay
        for chunk in client.stream(prompt):
            full_response += chunk
            messages_placeholder.markdown(full_response + " ")

        messages_placeholder.markdown(full_response)

    # add assistant response to chat history
    st.session_state.messages.append({'role': 'assistant', 'content' : full_response})