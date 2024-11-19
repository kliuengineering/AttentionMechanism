"""
Authours: 
    - Jasleen Kaur
    - Kevin Liu
    - Ma Toan Bach
"""
"""
About aggregator.py:
    Implements the WeightedAggregator class, 
    which acts as an observer in the Observer Pattern. 
    It aggregates the weighted words, sorts them based on 
    their attention scores, and updates the output whenever 
    it is notified of changes by the Word subjects.
"""


from observer import Observer
from typing import List
from word import Word
from attention_calculator import AttentionCalculator


class WeightedAggregator(Observer):
    def __init__(self, words: List[Word], attention_calculator: AttentionCalculator, context: str):
        self.words = words
        self.attention_calculator = attention_calculator
        self.context = context
        self.aggregated_output = ""
        # Attach observer to words
        for word in self.words:
            word.attach(self)
        self.aggregate()

    def update(self):
        print("Word data changed. Re-aggregating...")
        self.aggregate()

    def aggregate(self):
        weighted_words = self.attention_calculator.calculate_weights(self.words, self.context)
        # Sort words based on weight (highest first)
        weighted_words.sort(key=lambda w: w.weight, reverse=True)
        # Concatenate words based on their weights
        self.aggregated_output = ' '.join([w.get_text() for w in weighted_words])
        self.display()

    def display(self):
        print(f"Aggregated Output: {self.aggregated_output}")
