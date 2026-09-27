import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure GenAI Key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input_text):
    """Gets response from Gemini model."""
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(input_text)
    return response.text

def input_pdf_text(uploaded_file):
    """Extracts text from uploaded PDF."""
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        page_obj = reader.pages[page]
        text += str(page_obj.extract_text())
    return text

# Prompt Template
input_prompt_template = """
Act like a highly skilled ATS (Applicant Tracking System) with deep understanding of the tech field, software engineering, data science, and related domains.
Your task is to evaluate the resume based on the given job description. 
Given the competitive job market, provide the best assistance for improving the resume.
Assign the percentage match based on the JD and identify the missing keywords with high accuracy.

Resume Context:
{text}

Job Description Context:
{jd}

Respond exactly in this JSON-like structure without any markdown formatting:
{{"JD Match": "%", "MissingKeywords": [], "Profile Summary": "Detailed feedback and improvement tips here..."}}
"""

# Streamlit UI
st.set_page_config(page_title="ResumeFit", page_icon="📄")
st.title("ResumeFit 🚀")
st.markdown("### AI Resume Parser & ATS Optimizer")
st.text("Compare your resume against a job description and get improvement tips.")

jd = st.text_area("Paste the Job Description Here", height=200)
uploaded_file = st.file_uploader("Upload Your Resume", type="pdf", help="Upload your resume in PDF format")

submit = st.button("Evaluate Resume")

if submit:
    if uploaded_file is not None and jd.strip() != "":
        with st.spinner("Analyzing resume..."):
            text = input_pdf_text(uploaded_file)
            prompt = input_prompt_template.format(text=text, jd=jd)
            response = get_gemini_response(prompt)
            
            st.subheader("Analysis Results:")
            st.write(response)
    elif uploaded_file is None:
        st.warning("Please upload a PDF resume.")
    elif jd.strip() == "":
        st.warning("Please paste a Job Description.")
