import re

def clean_text(text: str) ->str:

    text = text.replace("\x00", " ")

    text = re.sub(r"\s+", "",text)

    return text.strip()

def normalize(text:str) -> str:

    text =text.lower()

    text = re.sub(r"[a-z0-9+#^.\-]", " ", text)

    text = re.sub(r"\s+", " ",text)

    return text.strip()