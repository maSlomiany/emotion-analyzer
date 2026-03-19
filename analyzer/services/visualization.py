#Mapa kolorków

class VisualizationService:
    EMOTION_COLORS ={
        'joy': "#77d88d",       # Zielony
        'sadness': "#0079fa",   # Niebieski
        'anger': '#dc3545',     # Czerwony
        'fear': "#764bc7",      # Fioletowy
        'surprise': "#ffe187",  # Żółty
        'neutral': "#b7b7b7"    # Szary
    }
    
    @staticmethod
    def get_color_for_emotion(emotion: str) -> str:
        return VisualizationService.EMOTION_COLORS.get(emotion.lower(), '#000000')
    
    @staticmethod
    def get_legend() -> dict:
        return VisualizationService.EMOTION_COLORS