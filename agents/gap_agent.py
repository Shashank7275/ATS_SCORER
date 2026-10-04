from agno.agent import Agent

from agents.model_factory import get_fallback_models, get_model


gap_agent = Agent(

    name="Skill Gap Agent",

    model=get_model(),

    fallback_models=get_fallback_models(),

    instructions=[
        """
        Analyze the gap between the candidate's resume
        and the job description.

        Identify:

        1. Missing technical skills
        2. Missing keywords
        3. Missing project evidence
        4. Weak resume bullets
        5. Areas that could be improved

        Never recommend falsely claiming experience.
        """
    ]
)