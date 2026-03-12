from dotenv import load_dotenv
import streamlit as st
import os
from PIL import Image
import io
import base64
import fitz  # PyMuPDF
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Google generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get GEMINI AI response
def get_gemini_response(input, pdf_content, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([input, pdf_content, prompt])
    return response.text

# Function to process PDF files
def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        try:
            document = fitz.open(stream=uploaded_file.read(), filetype="pdf")
            text_parts = [page.get_text() for page in document]
            pdf_text_content = " ".join(text_parts)
            return pdf_text_content
        except Exception as e:
            st.error(f"Error processing PDF file: {e}")
            return None
    else:
        raise FileNotFoundError("No file uploaded")

# Streamlit App Configuration
st.set_page_config(page_title="CV Expert", layout="wide")

# Custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
        padding: 20px;
    }
    .stButton > button {
        background-color: #4CAF50;
        color: white;
    }
    .stTextInput > div > input {
        background-color: #e8f0fe;
    }
    .header {
        text-align: center;
        padding: 10px 0;
    }
    .header img {
        width: 150px;
    }
    </style>
    """, unsafe_allow_html=True)

# Load and display the logo
logo_path = r"C:\Users\lenovo\ATS\logo1.jpg"
if os.path.exists(logo_path):
    logo = Image.open(logo_path)
    with io.BytesIO() as buffer:
        logo.save(buffer, format="PNG")
        encoded_logo = base64.b64encode(buffer.getvalue()).decode()
    st.markdown('<div class="header"><img src="data:image/png;base64,{}" class="img-fluid"></div>'.format(encoded_logo), unsafe_allow_html=True)
else:
    st.error("Logo file not found!")

# App Title and Description
st.title("Majale Berkane")
st.write("""
    Cette application vous aide dans la révision de votre CV grâce à GEMINI AI [LLM]. Elle offre plusieurs fonctionnalités pour améliorer votre expérience:
    - Analyse de CV : Téléchargez votre CV en format PDF et obtenez des analyses détaillées.
    - Réponses personnalisées : Recevez des réponses personnalisées basées sur vos questions.
    - Correspondance avec la description du poste : Téléchargez votre CV et obtenez une correspondance avec la description du poste.
    Profitez d'une expérience améliorée et optimisez votre processus de candidature avec notre application.
""")

# Sidebar for Inputs
with st.sidebar:
    st.header("Upload and Describe")
    input_text = st.text_area("Job Description:", height=150, key="input")
    uploaded_file = st.file_uploader("Upload your CV (PDF):", type=["pdf"])
    st.write("---")
    submit4 = st.button("Percentage Match")
    extract_info = st.button("Extract Key Information")
    extract_skills = st.button("Extract Skills")
    job_fit_analysis = st.button("Job Fit Analysis")
    keyword_highlight = st.button("Highlight Keywords")

# Prompts for GEMINI AI
input_prompt4 = """
You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality,
your task is to evaluate the CV against the provided job description. Give me the percentage of match if the CV matches
the job description. First, the output should come as a percentage and then keywords missing and last final thoughts.
"""

input_prompt_extract_info = """
You are an intelligent CV analyzer. Your task is to extract key information such as the candidate's name,
contact details, and education from the provided CV.
"""

input_prompt_extract_skills = """
You are an intelligent CV analyzer. Your task is to extract the list of skills mentioned in the provided CV.
"""

input_prompt_job_fit_analysis = """
You are an intelligent CV analyzer. Your task is to analyze how well the provided CV fits the given job description.
Highlight the strengths and weaknesses in the CV and provide a detailed analysis. Based on your analysis, determine whether the candidate
is fit for the job or needs to work on certain skills. Provide a clear conclusion stating "Yes, this person is fit for the job" or 
"No, this person is not fit for the job and needs to work on certain skills".
"""

input_prompt_keyword_highlight = """
You are an intelligent CV analyzer. Your task is to highlight the keywords from the provided job description that are present in the CV.
"""

# Main Area for Output
if uploaded_file is not None:
    st.success("PDF Uploaded Successfully")
    pdf_content = input_pdf_setup(uploaded_file)
    
    if pdf_content:
        if submit4:
            response = get_gemini_response(input_prompt4, pdf_content, input_text)
            st.subheader("The Response is")
            st.write(response)

        if extract_info:
            response = get_gemini_response(input_prompt_extract_info, pdf_content, input_text)
            st.subheader("Extracted Key Information")
            st.write(response)

        if extract_skills:
            response = get_gemini_response(input_prompt_extract_skills, pdf_content, input_text)
            st.subheader("Extracted Skills")
            st.write(response)

        if job_fit_analysis:
            response = get_gemini_response(input_prompt_job_fit_analysis, pdf_content, input_text)
            st.subheader("Job Fit Analysis")
            st.write(response)

        if keyword_highlight:
            response = get_gemini_response(input_prompt_keyword_highlight, pdf_content, input_text)
            st.subheader("Highlighted Keywords")
            st.write(response)
else:
    if submit4 or extract_info or extract_skills or job_fit_analysis or keyword_highlight:
        st.warning("Please upload a PDF file to proceed.")
