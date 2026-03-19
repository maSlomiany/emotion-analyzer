# Aplikacja webowa do analizy ładunku emocjonalnego w tekstach

W pełni responsywna aplikacja webowa oparta na architekturze uczenia maszynowego, służąca do detekcji i analizy emocji w tekstach anglojęzycznych w czasie rzeczywistym.


## O projekcie

System przyjmuje surowy tekst od użytkownika, przetwarza go z wykorzystaniem technik NLP (Natural Language Processing), a następnie klasyfikuje każde zdanie niezależnie do jednej z 6 podstawowych kategorii emocji (radość, smutek, gniew, strach, zaskoczenie) lub jako tekst neutralny. 


## Główne funkcjonalności

* **Analiza w czasie rzeczywistym:** Zastosowanie wzorca projektowego **Singleton** dla serwisu ML zapewnia ładowanie modelu do pamięci RAM tylko raz przy starcie serwera, co drastycznie skraca czas odpowiedzi.
* **NLP (spaCy):** Segmentacja zdań z zachowaniem słów kluczowych dla negacji.
* **Interaktywna wizualizacja wyników:** 
* * **Heatmapa tekstu:** Dynamiczne kolorowanie poszczególnych zdań w oparciu o wykrytą emocję.
  * **Wykres pierścieniowy:** Wygenerowany przy użyciu `Chart.js` wykres prezentujący zagregowany rozkład emocji w całej wypowiedzi.
* **Confidence Score (Wskaźnik pewności):** System wyświetla procentową pewność predykcji modelu dla każdego zdania w formie dynamicznych tooltipów.
* **Bezpieczeństwo i walidacja:** Zabezpieczenie formularzy po stronie serwera z limitem przetwarzania do 10000 znaków.

## Architektura i Technologie

**Backend & Data Science:**
* **Python 3**
* **Django** (Architektura bazująca na widokach klasowych i formularzach)
* **Scikit-Learn** (Optymalizowany model ML wyłoniony drogą walidacji krzyżowej i GridSearchCV)
* **spaCy** (Model `en_core_web_sm` zoptymalizowany pod kątem tokenizacji i lematyzacji)
* **Python Dataclasses** (Strukturyzacja przesyłanych danych bez użycia ORM)
* **Joblib** (Wydajna deserializacja artefaktów modeli z plików binarnych)

**Frontend:**
* **HTML5 / CSS3** (W pełni responsywny interfejs użytkownika RWD)
* **JavaScript & Chart.js** (Interaktywna prezentacja danych)

**Jakość oprogramowania:**
* Pytest & Pytest-Django (Automatyczne testy jednostkowe)
* Pytest-Cov (Całkowite pokrycie kodu testami: 98%)

## Struktura repozytorium
Projekt podzielony jest na dwie główne warstwy:
1. `training_scripts/` - skrypty badawcze Data Science (czyszczenie danych, ewaluacja modeli: RFC, SVC, MLP, optymalizacja hiperparametrów za pomocą Cost-Sensitive Learning i GridSearchCV).
2. `emotion_analyzer/` - główny kod aplikacji webowej Django wykorzystujący wytrenowane modele.

## Instalacja i uruchomienie lokalne

1. **Sklonuj repozytorium:**
   ```bash
   git clone [https://github.com/maSlomiany/emotion-analyzer.git](https://github.com/maSlomiany/emotion-analyzer.git)
   cd emotion-analyzer
