from typing import List, Tuple

import spacy


class POCTagger:
    def __init__(self):
        self._nlp = spacy.load('en')

    def __call__(self, text: str) -> List[Tuple[str, str]]:
        doc = self._nlp(text)
        return [(tok.text, tok.pos_) for tok in doc]