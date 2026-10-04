from sklearn.feature_extraction.text import TfidfVectorizer

class EmbeddingEngine:

    def __init__(self):

        self.vectorizer = TfidfVectorizer(
            stop_words="english"
        )

        self.matrix = None
        self.documents = []

    def fit(self,documents):
        self.documents = documents
        self.matrix = self.vectorizer.fit_transform(
            documents
        )

    def transform(self, query):
        return self.vectorizer.transform(
            [query]
        )
    