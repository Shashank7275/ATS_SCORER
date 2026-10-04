from agno.agent import Agent

from agents.model_factory import get_fallback_models, get_model
from model.schemas import ResumeData

document_agent = Agent(
    name="Resume Document Agent",

    model=get_model(),

    fallback_models=get_fallback_models(),

    output_schema=ResumeData,

    instructions=[
        """
        You are an expert resume parsing agent.

        Extract information from the supplied resume.

        Extract:
        - name
        - email
        - phone
        - summary
        - technical skills
        - education
        - experience
        - projects

        Do not invent information.

        If information is missing, return an empty value.
        """
    ]
)