from rag.embeddings import EmbeddingEngine

from rag.vector_store import VectorStore

from rag.knowledge_base import load_knowledge

class RAGRetriever:

    def __init__(self):

        documents = load_knowledge

        self.engine = EmbeddingEngine()

        self.engine.fit(documents)

        self.store = VectorStore(
            self.engine
        )

    def retrieve(self, query):
        return self.store.search(
            query,
            top_k=3
        )