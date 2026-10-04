from utils.text_cleaning import normalize

def keyword_match(resume_text, keywords):
    resume = normalize(resume_text)

    matched = []
    missing = []

    for keyword in keywords:
        key = normalize(keyword)

        if key in resume:
            matched.append(keyword)

        else:
            missing.append(keyword)

    total = len(keywords)

    score = (
        len(matched) / total * 100
        if total
        else 0
    )

    return {
        "score":round(score,2),
        "matched":matched,
        "missing":missing
    }