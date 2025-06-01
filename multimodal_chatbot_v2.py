
import streamlit as st
from PIL import Image
import pytesseract
import fitz  # PyMuPDF
import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain.prompts import PromptTemplate

# Load .env environment variables (API key)
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Set up the language model (GPT-4)
llm = ChatOpenAI(
    openai_api_key=openai_api_key,
    model_name="gpt-4",
    temperature=0.3
)

# Set up memory so the chatbot can remember the conversation
memory = ConversationBufferMemory()

# Initialize a conversation chain with memory
conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=False
)

# Streamlit UI setup
st.set_page_config(page_title="Multimodal Chatbot (Text + Image + PDF)")
st.title("🤖📄 Multimodal Chatbot with Memory")
st.write("Upload an image, PDF, or type text. Then ask any question — the bot will remember the chat!")

# Upload file
uploaded_file = st.file_uploader("Upload an image (.png/.jpg) or PDF (.pdf)", type=["png", "jpg", "jpeg", "pdf"])
input_text = st.text_area("Or paste some text")

# Extracted text output
extracted_text = ""

# Handle image
if uploaded_file is not None:
    file_type = uploaded_file.type

    if "image" in file_type:
        image = Image.open(uploaded_file)
        extracted_text = pytesseract.image_to_string(image)
        st.image(image, caption="Uploaded Image")
        st.write("📝 **Extracted Text from Image:**")
        st.write(extracted_text)

    elif file_type == "application/pdf":
        pdf = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        text_chunks = [page.get_text() for page in pdf]
        extracted_text = "\n".join(text_chunks)
        st.write("📖 **Extracted Text from PDF:**")
        st.write(extracted_text[:1000] + "..." if len(extracted_text) > 1000 else extracted_text)

# Combine all context
combined_context = input_text + "\n" + extracted_text

# Accept user question
user_input = st.text_input("Ask a question:")

# Generate answer
if st.button("Ask") and user_input:
    if not combined_context.strip() and memory.buffer == "":
        st.warning("Please upload a file or provide context text before asking.")
    else:
        full_input = combined_context + "\n" + user_input
        with st.spinner("Thinking..."):
            response = conversation.run(input=user_input)
        st.success("Answer ready:")
        st.write(response)

        # Display chat history (optional)
        with st.expander("🧠 Memory (Chat History)"):
            st.info(memory.buffer)
