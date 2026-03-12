import streamlit as st
import os
from PIL import Image
import io
import base64
import fitz  # PyMuPDF
import google.generativeai as genai
from dotenv import load_dotenv

# 1. Page Config must be the first Streamlit command
st.set_page_config(page_title="CV Expert", layout="wide")

# Load environment variables
load_dotenv()

# Configure Google generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get GEMINI AI response

def get_gemini_response(input_text, pdf_content, prompt):
    # Updated to the current supported model
    model = genai.GenerativeModel('gemini-1.5-flash') 
    response = model.generate_content([input_text, pdf_content, prompt])
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
            st.error(f"Erreur lors du traitement du fichier PDF : {e}")
            return None
    else:
        raise FileNotFoundError("Aucun fichier téléchargé")

# Custom CSS
st.markdown("""
    <style>
    body {
        background-color: #f8f9fa;
        font-family: 'Arial', sans-serif;
    }
    .main {
        background-color: #ffffff;
        border-radius: 8px;
        padding: 20px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .stButton > button {
        background-color: #007bff;
        color: white;
        border: none;
        border-radius: 4px;
        padding: 10px 20px;
        font-size: 16px;
        cursor: pointer;
        margin-top: 10px;
    }
    .stButton > button:hover {
        background-color: #0056b3;
    }
    .stTextInput > div > input {
        background-color: #e9ecef;
        border: 1px solid #ced4da;
        border-radius: 4px;
        padding: 10px;
        width: 100%;
    }
    .header {
        text-align: center;
        padding: 10px 0;
        margin-bottom: 20px;
    }
    .header img {
        width: 150px;
    }
    .sidebar .sidebar-content {
        background-color: #ffffff;
        border-radius: 8px;
        padding: 20px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Fixed Image Path: Place 'logo1.jpg' in the same folder as this script
logo_path = "logo1.jpg" 
if os.path.exists(logo_path):
    logo = Image.open(logo_path)
    with io.BytesIO() as buffer:
        logo.save(buffer, format="PNG")
        encoded_logo = base64.b64encode(buffer.getvalue()).decode()
    st.markdown('<div class="header"><img src="data:image/png;base64,{}" class="img-fluid"></div>'.format(encoded_logo), unsafe_allow_html=True)
else:
    st.warning("Fichier logo introuvable. Veuillez vérifier le chemin.")

# App Title and Description
st.title("Majal Berkane")
st.write("""
    Cette application vous aide dans la révision de votre CV grâce à GEMINI AI. Elle offre plusieurs fonctionnalités pour améliorer votre expérience:
    - Analyse de CV : Téléchargez votre CV en format PDF et obtenez des analyses détaillées.
    - Réponses personnalisées : Recevez des réponses personnalisées basées sur vos questions.
    - Lettre de motivation : Téléchargez votre CV et obtenez une correspondance avec la description du poste.
    Profitez d'une expérience améliorée et optimisez votre processus de candidature avec notre application.
""")

# Sidebar for Inputs
with st.sidebar:
    st.markdown('<div class="sidebar-content">', unsafe_allow_html=True)
    st.header("Téléchargez et décrivez")
    input_text = st.text_area("Description de l'offre de stage / poste:", height=150, key="input")
    uploaded_file = st.file_uploader("Télécharger votre CV (PDF):", type=["pdf"])

    st.write("---")
    submit1 = st.button("Parle-moi du CV")
    submit4 = st.button("Correspondance en pourcentage")
    submit3 = st.button("Quels mots-clés manquent ?")
    submit2 = st.button("Comment puis-je améliorer mes compétences ?")
    
    st.write("---")
    st.header("Poser une Question")
    input_promp = st.text_input("Requête : N'hésitez pas à demander ici")
    submit5 = st.button("Réponds à ma question")
    st.markdown('</div>', unsafe_allow_html=True)

# Prompts for GEMINI AI
input_prompt1 = """
You are an experienced Technical Human Resource Manager, your task is to review the provided resume against the job description.
Please share your professional evaluation on whether the candidate's profile aligns with the role.
Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

input_prompt2 = """
You are a Technical Human Resource Manager with expertise in data science,
your role is to scrutinize the resume in light of the job description provided.
Share your insights on the candidate's suitability for the role from an HR perspective.
Additionally, offer advice on enhancing the candidate's skills and identify areas where improvement is needed.
"""

input_prompt3 = """
You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality,
your task is to evaluate the resume against the provided job description. As a Human Resource manager,
assess the compatibility of the resume with the role. Give me what are the keywords that are missing.
Also, provide recommendations for enhancing the candidate's skills and identify which areas require further development.
"""

input_prompt4 = """
You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality,
your task is to evaluate the resume against the provided job description. Give me the percentage of match if the resume matches
the job description. First, the output should come as a percentage and then keywords missing and last final thoughts.
"""

# Main Area for Output
if uploaded_file is not None:
    # Fixed spelling
    st.success("PDF téléchargé avec succès")
    pdf_content = input_pdf_setup(uploaded_file)
    
    if pdf_content:
        if submit1:
            response = get_gemini_response(input_prompt1, pdf_content, input_text)
            st.subheader("La réponse est :")
            st.write(response)

        if submit2:
            response = get_gemini_response(input_prompt2, pdf_content, input_text)
            st.subheader("La réponse est :")
            st.write(response)

        if submit3:
            response = get_gemini_response(input_prompt3, pdf_content, input_text)
            st.subheader("La réponse est :")
            st.write(response)

        if submit4:
            response = get_gemini_response(input_prompt4, pdf_content, input_text)
            st.subheader("La réponse est :")
            st.write(response)

        if submit5 and input_promp:
            response = get_gemini_response(input_promp, pdf_content, input_text)
            st.subheader("La réponse est :")
            st.write(response)
else:
    if submit1 or submit2 or submit3 or submit4 or submit5:
        st.warning("Veuillez télécharger un fichier PDF pour continuer.")