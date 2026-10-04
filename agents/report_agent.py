from agno.agent import Agent

from agents.model_factory import get_fallback_models, get_model


report_agent = Agent(

    name="Final Report Agent",

    model=get_model(),

    fallback_models=get_fallback_models(),

    instructions=[
        """
        Create a final ATS analysis report.

        Include:

        ATS Score
        Keyword Score
        Skill Score
        Semantic Score
        Formatting Score

        Matched Skills

        Missing Skills

        Important Keywords

        Recommendations

        Resume Improvement Summary
        """
    ]
)