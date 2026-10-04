# 📄 ATS Resume Score Analyzer

An AI-powered **ATS Resume Score Analyzer** built with **Python and Streamlit**.

Users can upload their resume and enter a short **job description**. The application analyzes the resume against the job description and provides an **ATS compatibility score**, missing keywords, skills, and improvement suggestions.

## 🚀 Features

- 📤 Upload Resume (PDF)
- 📝 Enter Job Description
- 📊 ATS Score Analysis
- 🔑 Keyword & Skill Matching
- ❌ Missing Keywords Detection
- 💡 Resume Improvement Suggestions
- ⚡ Simple Streamlit UI
- ☁️ Deployable on Render

## 🛠️ Tech Stack

- Python
- Streamlit
- PyPDF
- NLP / AI
- LangChain
- LLM API

## 📁 Project Structure

```text
ATS-Resume-Analyzer/
│
├── app.py
├── requirements.txt
├── .env
├── README.md
│
├── utils/
│   ├── resume_parser.py
│   ├── ats_analyzer.py
│   └── utils.py
│
└── data/
```

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/ATS-Resume-Analyzer.git
cd ATS-Resume-Analyzer
```

Create virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## 🔐 Environment Variables

Create a `.env` file:

```env
GOOGLE_API_KEY=your_api_key
```

Never upload your `.env` file to GitHub.

Add it to `.gitignore`:

```text
.env
.venv/
__pycache__/
```

## ▶️ Run Locally

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

## ☁️ Deploy on Render

1. Push the project to GitHub.
2. Create a new **Web Service** on Render.
3. Connect your GitHub repository.
4. Set the build command:

```bash
pip install -r requirements.txt
```

5. Set the start command:

```bash
streamlit run app.py --server.port $PORT --server.address 0.0.0.0
```

6. Add your API key in **Render Environment Variables**.

## 🔄 How It Works

```text
Resume PDF
    ↓
Text Extraction
    ↓
Job Description
    ↓
Keyword & Skill Analysis
    ↓
ATS Scoring
    ↓
Missing Keywords
    ↓
Improvement Suggestions
```

## 📊 Example Output


ATS Score: 82/100

Matched Skills:
✓ Python
✓ Machine Learning
✓ SQL
✓ Pandas

Missing Skills:
• Docker
• AWS
• FastAPI

Suggestions:
• Add measurable project achievements
• Include missing technical skills
• Improve keyword matching
```

## 🎯 Goal

The goal of this project is to help job seekers quickly understand how well their resume matches a specific job description and improve their chances of passing ATS screening.

## 👨‍💻 Author

**Shashank Singh**

GitHub: https://github.com/Shashank7275
