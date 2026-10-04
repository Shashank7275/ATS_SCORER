import os
import tempfile

import streamlit as st
from dotenv import load_dotenv

from parser.pdf_parser import extract_pdf_text
from parser.docx_parser import extract_docx_text

from evaluation.keyword_score import keyword_match
from evaluation.semantic_score import semantic_similarity
from evaluation.ats_score import calculate_ats_score

from agents.document_agent import document_agent
from agents.job_agent import job_agent
from agents.matching_agent import matching_agent
from agents.gap_agent import gap_agent
from agents.resume_agent import resume_model
from agents.model_factory import DEFAULT_MODEL_ID, FALLBACK_MODEL_ID


load_dotenv()


st.set_page_config(
    page_title="Agentic ATS Analyzer",
    page_icon="🤖",
    layout="wide"
)


st.title("🤖 Agentic AI ATS Resume Analyzer")

st.caption(
    "GenAI + RAG + Multi-Agent AI + NLP"
)


# ------------------------------------------------
# SIDEBAR
# ------------------------------------------------

st.sidebar.header("Configuration")

model_name = os.getenv("MODEL_NAME", DEFAULT_MODEL_ID)
fallback_model_name = os.getenv("FALLBACK_MODEL_NAME", FALLBACK_MODEL_ID)
st.sidebar.info(
    f"Primary Gemini model: {model_name}\nFallback: {fallback_model_name}"
)


# ------------------------------------------------
# UPLOAD
# ------------------------------------------------

resume_file = st.file_uploader(
    "Upload Resume",
    type=["pdf", "docx"]
)


job_description = st.text_area(
    "Paste Job Description",
    height=300
)


analyze = st.button(
    "🚀 Analyze Resume",
    type="primary"
)


# ------------------------------------------------
# ANALYSIS
# ------------------------------------------------

if analyze:

    if not resume_file:

        st.error("Please upload a resume.")

        st.stop()


    if not job_description.strip():

        st.error(
            "Please enter a job description."
        )

        st.stop()


    try:
        with st.spinner(
            "AI agents are analyzing your resume..."
        ):

            suffix = os.path.splitext(
                resume_file.name
            )[1]


            with tempfile.NamedTemporaryFile(
                delete=False,
                suffix=suffix
            ) as temp:

                temp.write(
                    resume_file.read()
                )

                temp_path = temp.name


            # -----------------------------
            # DOCUMENT PARSING
            # -----------------------------

            if suffix.lower() == ".pdf":

                resume_text = extract_pdf_text(
                    temp_path
                )

            else:

                resume_text = extract_docx_text(
                    temp_path
                )


            # -----------------------------
            # DOCUMENT AGENT
            # -----------------------------

            resume_result = document_agent.run(
                resume_text
            )

            resume_data = resume_result.content


            # -----------------------------
            # JOB AGENT
            # -----------------------------

            jd_result = job_agent.run(
                job_description
            )

            job_data = jd_result.content


            # -----------------------------
            # KEYWORD SCORE
            # -----------------------------

            keywords = []

            if hasattr(
                job_data,
                "keywords"
            ):

                keywords = job_data.keywords


            keyword_result = keyword_match(
                resume_text,
                keywords
            )


            # -----------------------------
            # SEMANTIC SCORE
            # -----------------------------

            semantic_score = semantic_similarity(
                resume_text,
                job_description
            )


            # -----------------------------
            # MATCHING AGENT
            # -----------------------------

            matching_prompt = f"""

            RESUME:

            {resume_text}


            JOB DESCRIPTION:

            {job_description}


            Analyze the match.

            """

            match_result = matching_agent.run(
                matching_prompt
            )


            # -----------------------------
            # GAP AGENT
            # -----------------------------

            gap_prompt = f"""

            RESUME:

            {resume_text}


            JOB DESCRIPTION:

            {job_description}


            MATCHING ANALYSIS:

            {match_result.content}

            Find skill and keyword gaps.

            """

            gap_result = gap_agent.run(
                gap_prompt
            )


            # -----------------------------
            # RESUME AGENT
            # -----------------------------

            resume_prompt = f"""

            ORIGINAL RESUME:

            {resume_text}


            JOB DESCRIPTION:

            {job_description}


            MATCHING ANALYSIS:

            {match_result.content}


            GAP ANALYSIS:

            {gap_result.content}


            Create an ATS-friendly improved resume.

            Do not invent information.

            """

            optimized_result = resume_model.run(
                resume_prompt
            )
    except Exception as exc:
        error_details = str(exc)
        if "403" in error_details or "PERMISSION_DENIED" in error_details:
            st.error(
                "Google denied access to the Gemini API project. Create a new Gemini API key in "
                "Google AI Studio (new keys are authorization keys), set it as GOOGLE_API_KEY or "
                "GEMINI_API_KEY in .env, then restart the app. If a fresh key still gets 403, "
                "the project must be enabled by its Google Cloud administrator or Google support."
            )
        elif (
            "429" in error_details
            or "RESOURCE_EXHAUSTED" in error_details
            or "quota" in error_details.lower()
        ):
            st.error(
                "Gemini API quota is exhausted for this project/model. This is not an API key "
                "error. Wait for the quota to reset, enable billing or a higher usage tier, or "
                "set MODEL_NAME in .env to a model with available quota. Check usage at "
                "https://ai.dev/rate-limit."
            )
        else:
            st.error(
                "Gemini model request failed. Check your API key and access permissions. "
                f"Details: {error_details}"
            )
        st.stop()


    # ------------------------------------------------
    # DASHBOARD
    # ------------------------------------------------

    st.success(
        "Analysis completed successfully!"
    )


    st.divider()


    col1, col2, col3, col4 = st.columns(4)


    col1.metric(
        "Keyword Match",
        f"{keyword_result['score']}%"
    )


    col2.metric(
        "Semantic Match",
        f"{semantic_score}%"
    )


    # Initial formatting estimate
    formatting_score = 85


    skill_score = keyword_result["score"]


    final_score = calculate_ats_score(

        keyword_result["score"],

        skill_score,

        semantic_score,

        formatting_score
    )


    col3.metric(
        "ATS Score",
        f"{final_score}/100"
    )


    col4.metric(
        "Formatting",
        f"{formatting_score}%"
    )


    # ------------------------------------------------
    # MATCHES
    # ------------------------------------------------

    st.subheader(
        "🔎 Keyword Analysis"
    )


    c1, c2 = st.columns(2)


    with c1:

        st.markdown(
            "### ✅ Matched"
        )

        for item in keyword_result["matched"]:

            st.write(
                f"✓ {item}"
            )


    with c2:

        st.markdown(
            "### ❌ Missing"
        )

        for item in keyword_result["missing"]:

            st.write(
                f"• {item}"
            )


    # ------------------------------------------------
    # AGENT ANALYSIS
    # ------------------------------------------------

    st.subheader(
        "🤖 Agent Analysis"
    )


    with st.expander(
        "Resume-JD Matching"
    ):

        st.write(
            match_result.content
        )


    with st.expander(
        "Skill Gap Analysis"
    ):

        st.write(
            gap_result.content
        )


    # ------------------------------------------------
    # OPTIMIZED RESUME
    # ------------------------------------------------

    st.subheader(
        "✨ AI Optimized Resume"
    )


    st.markdown(
        optimized_result.content
    )