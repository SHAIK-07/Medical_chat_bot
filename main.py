import streamlit as st
from src.helper import download_hugging_face_embeddings
from langchain_pinecone import PineconeVectorStore
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os
from src.prompt import *

# Load environment variables
load_dotenv()
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

# Initialize embeddings
embeddings = download_hugging_face_embeddings()
index_name = "medicat-chat-bot"

# Load the Pinecone vector store
docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name, embedding=embeddings
)
retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k": 3})

# Initialize LLM and prompt with chat history support

llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0.4)
prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{input}"),
])

question_answer_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)

# Streamlit UI
st.set_page_config(page_title="AI Chatbot", page_icon="🤖")
st.markdown("<h1 style='text-align: center;'>🤖 Medical AI Chatbot with Gemini & Pinecone</h1>", unsafe_allow_html=True)

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display chat history
for query, resp in st.session_state.chat_history:
    with st.chat_message("user"):
        st.markdown(f"<div style='background-color:#dcf8c6; padding:10px; border-radius:10px; max-width:80%;'>👤 **You:** {query}</div>", unsafe_allow_html=True)
    with st.chat_message("assistant"):
        st.markdown(f"<div style='background-color:#f1f1f1; padding:10px; border-radius:10px; max-width:80%;'>🤖 **Bot:** {resp}</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# User input in a chat-like box
user_input = st.chat_input("Type your message...")

if user_input:
    # Format chat history for context
    chat_history_str = "\n".join([f"User: {q}\nBot: {a}" for q, a in st.session_state.chat_history])

    # Invoke the RAG chain
    response = rag_chain.invoke({"input": user_input, "chat_history": chat_history_str})
    answer = response["answer"]

    # Store in history
    st.session_state.chat_history.append((user_input, answer))

    # Display real-time chat response
    with st.chat_message("user"):
        st.markdown(f"<div style='background-color:#dcf8c6; padding:10px; border-radius:10px; max-width:80%;'>👤 **You:** {user_input}</div>", unsafe_allow_html=True)
    with st.chat_message("assistant"):
        st.markdown(f"<div style='background-color:#f1f1f1; padding:10px; border-radius:10px; max-width:80%;'>🤖 **Bot:** {answer}</div>", unsafe_allow_html=True)

# Button to clear chat history
if st.button("🗑️ Clear Chat"):
    st.session_state.chat_history = []
    st.rerun()
