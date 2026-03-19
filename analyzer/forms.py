from django import forms

#Formularz
class TextInputForm(forms.Form):
    text = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control', 
            'placeholder': 'Wpisz tekst w języku angielskim do analizy...',
            'rows': 6
        }),
        label="Tekst do analizy",
        max_length=10000, #max 10k znaków
        help_text="Maksymalnie 10 000 znaków."
    )