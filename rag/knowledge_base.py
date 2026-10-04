from pathlib import Path

BASE_DIR = Path(
    "data/knowledge_base"
)

def load_knowledge():

    documents = []

    for file in BASE_DIR.glob("*.txt"):

        text = file.read_text(
            encoding="utf-8"
        )

        documents.append(text)

    return documents