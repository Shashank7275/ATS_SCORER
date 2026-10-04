from agno.agent import Agent

from agents.model_factory import get_fallback_models, get_model

ats_agent = Agent(

    name="ATS Analysis Agent",

    model=get_model(),

    fallback_models=get_fallback_models(),

    instructions=[

        """
        Analyze the resume for ATS compatibility.

        Check:

        - Contact information
        - Resume sections
        - Skill section
        - Experience section
        - Project section
        - Education
        - Excessive symbols
        - Tables
        - Unusual formatting
        - Missing keywords
        - Long paragraphs
        - Weak bullet points

        Return:
        - issues
        - recommendations
        - strengths

        Do not invent facts.
        """


    ]
)