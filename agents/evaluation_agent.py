from agno.agent import Agent

from agents.model_factory import get_fallback_models, get_model

evaluation_agent = Agent(

    name="Resume Evaluation Agent",

    model =get_model(),

    fallback_models=get_fallback_models(),

    instructions=[
        """
        Evaluate the analysis produced by the previous agents.

        Explain:

        - strongest parts
        - weakest parts
        - missing skills
        - keyword gaps
        - resume improvement areas

        Keep the evaluation evidence-based.
        """
    ]
)