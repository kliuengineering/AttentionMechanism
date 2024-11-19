"""
Authours: 
    - Jasleen Kaur
    - Kevin Liu
    - Ma Toan Bach
"""
"""
About attention_calculator.py: 
    Contains the AttentionCalculator class, 
    which uses different strategies to calculate attention weights for 
    each word based on the given context. It acts as 
    a bridge between the strategies and the decorated words.
"""


from typing import List
from word import Word
from decorator import AttentionWordDecorator # type: ignore
from strategy import AttentionStrategy


class AttentionCalculator:
    def __init__(self, strategy: AttentionStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: AttentionStrategy):
        self._strategy = strategy

    def calculate_weights(self, words: List[Word], context: str) -> List[AttentionWordDecorator]:
        decorated_words = []
        for word in words:
            weight = self._strategy.calculate_weight(word, context)
            decorated_word = AttentionWordDecorator(word, weight)
            decorated_words.append(decorated_word)
        return decorated_words
