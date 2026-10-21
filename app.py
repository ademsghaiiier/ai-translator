import os
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="AI Translator",
    page_icon="🌍",
)

# Title
st.title("🌍 AI Translator")

st.write("Translate text between languages using AI.")

# Inputs
from_language = st.text_input(
    "Main Language",
    placeholder="Example: English"
)

to_language = st.text_input(
    "Target Language",
    placeholder="Example: French"
)

text = st.text_area(
    "Text to Translate",
    placeholder="Type your text here..."
)

# Initialize model
llm = ChatGroq(
    model="openai/gpt-oss-20b",
    api_key=os.getenv("GROQ_API_KEY")
)

# Prompt template
prompt_template = ChatPromptTemplate.from_template(
    """
    Translate the following text from {from_language}
    to {to_language}.

    Return ONLY the translated text.

    Text:
    {text}
    """
)

# Translate button
if st.button("Translate 🚀"):

    if not from_language or not to_language or not text:
        st.warning("Please fill all fields.")
    else:
        try:
            prompt = prompt_template.invoke(
                {
                    "from_language": from_language,
                    "to_language": to_language,
                    "text": text,
                }
            )

            response = llm.invoke(prompt)

            st.subheader("Translation")
            st.success(response.content)

        except Exception as e:
            st.error(f"Error: {e}")