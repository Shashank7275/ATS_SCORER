from dotenv import load_dotenv
from agno.workflow import Workflow

load_dotenv()


def create_workflow():
    from agents.ats_agent import ats_agent
    from agents.document_agent import document_agent
    from agents.evaluation_agent import evaluation_agent
    from agents.gap_agent import gap_agent
    from agents.job_agent import job_agent
    from agents.matching_agent import matching_agent
    from agents.report_agent import report_agent
    from agents.resume_agent import resume_agent
    from agents.skill_agent import skill_agent

    workflow = Workflow(
        name="Agentic ATS Resume Analyzer",
        description="""
        Multi-agent AI system that analyzes resumes
        against job descriptions and generates
        ATS optimization recommendations.
        """,
        steps=[
            document_agent,
            job_agent,
            ats_agent,
            skill_agent,
            matching_agent,
            gap_agent,
            evaluation_agent,
            resume_agent,
            report_agent,
        ],
    )

    return workflow