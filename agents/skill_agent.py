from agno.agent import Agent

from agents.model_factory import get_fallback_models, get_model

skill_agent = Agent(

    name="Skull Agent",

    model=get_model(),

    fallback_models=get_fallback_models(),

    instructions=[
        """
        You are a technical skill extraction specialist.

        Identify:

        - Programming languages
        - Machine learning skills
        - Deep learning skills
        - NLP skills
        - GenAI skills
        - Cloud skills
        - Databases
        - Frameworks
        - DevOps tools

        Return a clean categorized list.
        """


    ]
)