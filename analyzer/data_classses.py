from dataclasses import dataclass
from typing import List, Dict

@dataclass
class Sentence:
    "Reprezentuje pojedyncze zdanie wraz z jego analizą"
    text: str
    emotion: str
    confidence: float
    color: str

@dataclass
class AnalysisOutput:
    "Kontener na wyniki analizy całego tekstu"
    original_text: str
    sentences: List[Sentence]
    legend: Dict[str, str]