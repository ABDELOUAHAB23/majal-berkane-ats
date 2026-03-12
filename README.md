# 🎯 CV Expert — AI-Powered ATS Resume Analyzer

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/Google%20Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" />
</p>

<p align="center">
  A smart, AI-driven resume analysis tool that helps candidates optimize their CVs against job descriptions using Google Gemini AI and ATS scoring logic.
</p>

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Configuration](#configuration)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [API Reference](#-api-reference)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🧠 Overview

**CV Expert** is a Streamlit-based web application that leverages **Google Gemini 1.5 Flash** to provide deep, context-aware analysis of resumes against job descriptions. Whether you're a candidate looking to improve your profile or an HR professional screening applicants, this tool offers instant, actionable feedback.

---

## ✨ Features

| Feature | Description |
|---|---|
| 📄 **CV Analysis** | Detailed evaluation of your resume against a specific job description |
| 📊 **ATS Match Score** | Percentage-based compatibility score with keyword gap analysis |
| 🔍 **Missing Keywords** | Identifies ATS keywords absent from your resume |
| 💡 **Skill Improvement Tips** | Personalized recommendations to strengthen your profile |
| 💬 **Custom Q&A** | Ask any question about your CV and get an AI-powered answer |

---

## 🛠 Tech Stack

- **Frontend:** [Streamlit](https://streamlit.io/)
- **AI Model:** [Google Gemini 1.5 Flash](https://ai.google.dev/)
- **PDF Processing:** [PyMuPDF (fitz)](https://pymupdf.readthedocs.io/)
- **Backend API:** [Flask](https://flask.palletsprojects.com/)
- **Environment Management:** [python-dotenv](https://pypi.org/project/python-dotenv/)

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- A valid [Google Gemini API key](https://ai.google.dev/)

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/your-username/cv-expert.git
cd cv-expert
```

2. **Create and activate a virtual environment** *(recommended)*

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

### Configuration

1. Create a `.env` file in the project root:

```bash
touch .env
```

2. Add your Google Gemini API key:

```env
GOOGLE_API_KEY=your_google_gemini_api_key_here
```

> ⚠️ Never commit your `.env` file. It is already listed in `.gitignore`.

---

## 💻 Usage

### Run the Streamlit App

```bash
streamlit run app.py
```

The app will be available at `http://localhost:8501` by default.

### Run the Flask API (optional)

```bash
python api.py
```

The API will be available at `http://localhost:8506`.

### How to Use

1. Paste the **job description** in the sidebar text area.
2. **Upload your CV** in PDF format.
3. Choose one of the available analysis options:
   - **"Parle-moi du CV"** — General resume review
   - **"Correspondance en pourcentage"** — ATS match percentage
   - **"Quels mots-clés manquent ?"** — Missing keywords
   - **"Comment puis-je améliorer mes compétences ?"** — Skill improvement advice
4. Or type a **custom question** and click *"Réponds à ma question"*.

---

## 📁 Project Structure

```
cv-expert/
│
├── app.py                  # Main Streamlit application
├── api.py                  # Flask REST API (candidates endpoint)
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (not committed)
├── logo1.jpg               # App logo (optional)
└── README.md               # Project documentation
```

---

## 🔌 API Reference

### `GET /api/candidates`

Returns a list of candidates.

**Response:**

```json
[
  {
    "name": "John Doe",
    "position": "Developer"
  }
]
```

> This endpoint is currently a stub and should be connected to your database.

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

<p align="center">Made with ❤️ using Google Gemini AI & Streamlit</p>
