from agno.agent import Agent

from agents.model_factory import get_fallback_models, get_model

matching_agent = Agent(

    name="Resume Job Matching Agent",

    model=get_model(),

    fallback_models=get_fallback_models(),

    instructions=[
         """
        Compare the resume against the job description.

        Identify:

        - Matching skills
        - Missing skills
        - Matching experience
        - Missing keywords
        - Relevant projects

        Never claim that the candidate has a skill
        unless it exists in the supplied resume.
        """
    ]
)