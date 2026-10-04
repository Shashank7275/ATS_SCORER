from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.metrics.pairwise import cosine_similarity

def semantic_similarity(resume_text,job_description):

    if not resume_text.strip() or not job_description.strip():
        return 0

    vectorizer = TfidfVectorizer(
        stop_words="english"
    )

    try:
        vector = vectorizer.fit_transform([
            resume_text,
            job_description
        ])
    except ValueError as exc:
        if "empty vocabulary" not in str(exc).lower():
            raise
        return 0

    similarity = cosine_similarity(
        vector[0:1],
        vector[1:2]
    )[0][0]

    return round(similarity * 100, 2)

