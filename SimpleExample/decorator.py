"""
Authours: 
    - Jasleen Kaur
    - Kevin Liu
    - Ma Toan Bach
"""
"""
About decorator.py:
    Implements the Decorator Pattern classes. 
    It includes the WordDecorator abstract class and 
    the AttentionWordDecorator concrete class, 
    which adds additional functionality (e.g., attention weights) 
    to Word objects without modifying their original structure.
"""


from abc import ABC, abstractmethod
from word import Word


# << interface >>, abstract decorator
class WordDecorator(ABC):
    def __init__(self, word: Word):
        self._word = word

    @abstractmethod
    def get_text(self):
        pass


# concrete decorator A
# adds the weight parameter for intelligence
class AttentionWordDecorator(WordDecorator):
    def __init__(self, word: Word, weight: float):
        super().__init__(word)
        self.weight = weight

    def get_text(self):
        return self._word.text
