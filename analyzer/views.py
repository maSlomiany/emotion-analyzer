from django.shortcuts import render
from django.views.generic import FormView
from collections import Counter
from .forms import TextInputForm
from .services.emotion_analysis import EmotionAnalysisService
from .services.visualization import VisualizationService

class AnalyzeView(FormView):
    template_name = 'home.html'
    form_class = TextInputForm
    success_url = '/'

    def form_valid(self, form):
        text = form.cleaned_data['text']
        
        # 1. Analiza tekstu
        analyzer_service = EmotionAnalysisService()
        analysis_result = analyzer_service.analyze_text(text)
        
        # 2. Przygotowanie danych do wykresu
        emotions_list = [s.emotion for s in analysis_result.sentences]
        counts = Counter(emotions_list)
        
        sorted_emotions = sorted(counts.keys())
        
        # Przygotowujemy listy dla Chart.js
        chart_labels = [e.capitalize() for e in sorted_emotions]
        chart_data = [counts[e] for e in sorted_emotions]
        chart_colors = [VisualizationService.get_color_for_emotion(e) for e in sorted_emotions]
        
        # 3. Przekazujemy wszystko do szablonu
        return render(self.request, self.template_name, {
            'form': form,
            'result': analysis_result,
            # Dane dla wykresu:
            'chart_labels': chart_labels,
            'chart_data': chart_data,
            'chart_colors': chart_colors
        })