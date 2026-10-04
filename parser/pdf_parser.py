import pymupdf


def extract_pdf_text(file_path: str) -> str:
    document = pymupdf.open(file_path)

    text = ""

    for page in document:
        text+= page.get_text()

    document.close()

    return text