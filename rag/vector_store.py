from sklearn.metrics.pairwise import cosine_similarity


class VectorStore:

    def __init__(self, embedding_engine):

        self.embedding_engine = embedding_engine


    def search(self, query, top_k=3):

        query_vector = (
            self.embedding_engine.transform(query)
        )

        scores = cosine_similarity(
            query_vector,
            self.embedding_engine.matrix
        )[0]

        indexes = scores.argsort()[::-1][:top_k]

        results = []

        for index in indexes:

            results.append({
                "text":
                    self.embedding_engine.documents[index],

                "score":
                    float(scores[index])
            })

        return results