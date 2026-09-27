# ResumeFit 🚀

ResumeFit is an AI-powered resume parser and Applicant Tracking System (ATS) optimizer. It ranks resumes against job descriptions, provides match percentages, and offers actionable improvement tips using Google's Generative AI (Gemini).

## Features
- **Upload Resumes:** Supports PDF resume uploads.
- **Job Description Comparison:** Paste any job description to evaluate fit.
- **ATS Match Percentage:** Get an instant compatibility score.
- **Missing Keywords:** Identify skills and keywords missing from your resume.
- **Improvement Tips:** Receive a personalized profile summary and tips to enhance your chances of getting hired.

## Tech Stack
- Python
- Streamlit (Web Interface)
- Google Generative AI (Gemini 1.5 Flash)
- PyPDF2 (PDF Parsing)

## Setup & Installation

1. **Clone the repository (or navigate to the project folder):**
   ```bash
   cd Resume.Fit
   ```

2. **Create a virtual environment (Optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up Environment Variables:**
   - Copy the `.env.example` file to `.env`.
   - Add your Google Gemini API key to the `.env` file.
   ```env
   GOOGLE_API_KEY="your_api_key_here"
   ```

5. **Run the Application:**
   ```bash
   streamlit run app.py
   ```
