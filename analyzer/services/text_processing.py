import spacy
import re

class TextProcessingService:
    def __init__(self):
        # Ładowanie modelu spaCy
        try:
            # Wyłączamy ciężkie komponenty, ale musimy dodać 'sentencizer' ręcznie
            self.nlp = spacy.load("en_core_web_sm", disable=['parser', 'ner'])
            self.nlp.add_pipe('sentencizer')
        except OSError:
            # Fallback jeśli nie ma modelu - używamy pustego modelu angielskiego
            from spacy.lang.en import English
            self.nlp = English()
            self.nlp.add_pipe('sentencizer')

    def tokenize_to_sentences(self, text: str) -> list:
        """Dzieli tekst na zdania."""
        doc = self.nlp(text)
        return [sent.text.strip() for sent in doc.sents if sent.text.strip()]

    def clean_text_for_model(self, text: str) -> str:
        """Przygotowuje tekst dla modelu ML (to samo co w treningu)."""
        text = str(text).lower()
        text = re.sub(r'https?://\S+|www\.\S+', '', text)
        text = re.sub(r'<.*?>', '', text)
        text = re.sub(r'\[.*?\]', '', text)
        text = re.sub(r'[^a-zA-Z\s?!]', '', text)
        text = re.sub(r'\s+', ' ', text).strip()
        
        doc = self.nlp(text)
        clean_tokens = []
        for token in doc:
            if not token.is_stop or token.lemma_ in ['not', 'no', 'never', 'nothing']:
                clean_tokens.append(token.lemma_)
        return " ".join(clean_tokens)