"""
Authours: 
    - Jasleen Kaur
    - Kevin Liu
    - Ma Toan Bach
"""
"""
About strategy.py:
    Defines the Strategy interfaces and concrete strategy implementations. 
    It includes the AttentionStrategy abstract class and concrete 
    strategies like KeywordMatchingStrategy and LengthBasedStrategy for 
    calculating attention weights.
"""

from abc import ABC, abstractmethod
from word import Word


# << interface >> Strategy
class AttentionStrategy(ABC):
    @abstractmethod
    def calculate_weight(self, word:Word, context:str) -> float:
        pass


# Concrete strategy A
class KeywordMatchingStrategy(AttentionStrategy):
    def calculate_weight(self, word, context):
        return 1.0 if word.text.lower() in context.lower().split() else 0.1
    

# Concrete strategy B
class LengthBasedStrategy(AttentionStrategy):
    def calculate_weight(self, word, context):
        return len(word.text) / max( len(w) for w in context.split() )