from agno.agent import Agent

from agents.model_factory import get_fallback_models, get_model

from model.schemas import JobData

job_agent = Agent(

    name = "Job Description Agent",

    model=get_model(),

    fallback_models=get_fallback_models(),

    output_schema=JobData,

    instructions=[
        """
        You are an expert job description analyzer.

        Analyze the supplied job description.

        Extract:

        1. Job title
        2. Required skills
        3. Preferred skills
        4. Responsibilities
        5. Important keywords

        Do not invent requirements.
        """
    ]
)