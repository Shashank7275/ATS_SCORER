from pydantic import BaseModel, Field

from typing import List

class ResumeData(BaseModel):
    name : str = ""
    email : str = ""
    phone : str = ""

    summary : str = ""

    skills : List[str] = Field(default_factory=list)
    education : List[str] = Field(default_factory=list)
    experience : List[str] = Field(default_factory=list)
    projects : List[str] = Field(default_factory=list)


class JobData(BaseModel):
    title : str = ""

    required_skills : List[str] = Field(default_factory=list)
    preferred_skills : List[str] = Field(default_factory=list)

    responsibilities : List[str] = Field(default_factory=list)
    keywords : List[str] = Field(default_factory=list)

class MatchResult(BaseModel):
    matched_skills: List[str] = Field(default_factory=list)
    missing_skills: List[str] = Field(default_factory=list)
    matched_keywords: List[str] = Field(default_factory=list)




class ATSResult(BaseModel):
    formatting_score:float = 0
    section_score: float = 0
    readability_score:float = 0
    issues: List[str] = Field(default_factory=list)

class FinalReport(BaseModel):

    ats_score: float
    keyword_score: float
    skill_score: float
    semantic_score: float
    formatting_score: float

    matched_skills : List[str]
    missing_skills : List[str]

    recommendations: List[str]
    optimized_resume : str

    