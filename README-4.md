
# 🤖 Multimodal Chatbot (Text + Image + PDF) with Memory

This Streamlit app allows you to upload **images, PDFs, or text**, and ask questions about the content using **OpenAI GPT-4**. It also includes **conversation memory**, so the chatbot remembers your previous questions and answers!

---

## 📦 Features
- Upload `.png`, `.jpg`, `.jpeg` images and extract text with OCR
- Upload `.pdf` documents and extract readable text
- Paste raw text directly into the interface
- Ask questions about the content using **GPT-4**
- Supports **conversation history and follow-up questions**

---

## 🚀 How to Run

1. **Install dependencies:**
```bash
pip install -r requirements.txt
```

2. **Create a `.env` file** with your OpenAI key:
```
OPENAI_API_KEY=your_openai_api_key_here
```

3. **Run the chatbot:**
```bash
streamlit run multimodal_chatbot_v2.py
```

---

## 🧠 Tech Stack
- [Streamlit](https://streamlit.io/)
- [LangChain](https://github.com/langchain-ai/langchain)
- [OpenAI GPT-4 API](https://platform.openai.com/)
- [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/) for PDF parsing
- [pytesseract](https://github.com/madmaze/pytesseract) for OCR

---

## 💡 Example Use Cases
- Ask questions about a scanned image or document
- Upload a lecture PDF and get summaries or clarifications
- Build a foundation for document-based or visual Q&A systems

---

## 📬 Author
Created with ❤️ by [Your Name]. Powered by OpenAI, LangChain, and Streamlit.
