def calculate_ats_score(
        keyword_score,
        skill_score,
        semantic_score,
        formatting_score
):


    score = (

        keyword_score * 0.30 +

        skill_score * 0.30 +

        semantic_score * 0.25 +

        formatting_score * 0.15

    )

    return round(score, 2)
    