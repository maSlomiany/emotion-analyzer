#Ladujemy model i stosujemy wzorzec Singleton, zeby nie ładowac modelu przy kazdym kliknięciu

import joblib
import os
from django.conf import settings
from .text_processing import TextProcessingService
from .visualization  import VisualizationService
from analyzer.data_classses import Sentence, AnalysisOutput

class EmotionAnalysisService:
    _instance = None
    
    # Singleton pattern
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(EmotionAnalysisService, cls).__new__(cls)
            cls._instance._load_models()
            cls._instance.text_processor = TextProcessingService()
        return cls._instance

    def _load_models(self):
        #Ładuje modele z katalogu ml_models
        BASE_DIR = settings.BASE_DIR
        MODELS_DIR = os.path.join(BASE_DIR, 'ml_models')
        
        print("Ładowanie modeli ML do pamięci")
        self.model = joblib.load(os.path.join(MODELS_DIR, 'emotion_model.joblib'))
        self.vectorizer = joblib.load(os.path.join(MODELS_DIR, 'tfidf_vectorizer.joblib'))
        self.le = joblib.load(os.path.join(MODELS_DIR, 'label_encoder.joblib'))
        print("Modele załadowane")
    
    def analyze_text(self, text: str) -> AnalysisOutput:
        #Główna metoda orkiestrująca analizę
        #1. Podział na zdania
        raw_sentences = self.text_processor.tokenize_to_sentences(text)
        analyzed_sentences = []

        #2. Analiza każdego zdania
        for raw_sent in raw_sentences:
            # Preprocessing pod model
            clean_sent = self.text_processor.clean_text_for_model(raw_sent)
    
            emotion = "neutral"
            confidence = 0.0
            
            if len(clean_sent) > 1:
                # Wektoryzacja
                vec_sent = self.vectorizer.transform([clean_sent])
                # Predykcja
                pred_numeric = self.model.predict(vec_sent)[0]
                emotion = self.le.inverse_transform([pred_numeric])[0]
                
                # Symulacja confidence
                if hasattr(self.model, "predict_proba"):
                    confidence = max(self.model.predict_proba(vec_sent)[0])
                else:
                    confidence = 1.0
            
            # 3. Mapowanie koloru
            color = VisualizationService.get_color_for_emotion(emotion)
            
            # Tworzenie obiektu danych
            sentence_obj = Sentence(
                text=raw_sent,
                emotion=emotion,
                confidence=round(confidence * 100, 1),
                color=color
            )
            analyzed_sentences.append(sentence_obj)

        # 4. Zwrócenie zagregowanego wyniku
        return AnalysisOutput(
            original_text=text,
            sentences=analyzed_sentences,
            legend=VisualizationService.get_legend()
        )