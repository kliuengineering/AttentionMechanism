"""
Authours: 
    - Jasleen Kaur
    - Kevin Liu
    - Ma Toan Bach
"""
"""
About word.py:
    Defines the Word class, representing individual words in the system. 
    The Word class implements the Subject interface from the Observer Pattern, 
    so allowing it to notify observers when its state changes.

    We have re-opened this class (although not the best practice) to fit the trained
    model logics inside here. We do not want to make the code base more complicated
    for this project.
"""


from observer import Subject
from embeddings import Embeddings
import numpy as np


# concrete subjects from the observer pattern
class Word(Subject):
    # Class-level attribute (basically static variable in C++) to hold embeddings
    embeddings = None  

    def __init__(self, text: str):
        super().__init__()
        self._text = text
        self._data_changed = False
        if Word.embeddings is None:
            # Initialize embeddings with the path to our GloVe model file
            Word.embeddings = Embeddings('glove.6B.50d.txt')
        self.embedding = self.get_embedding()

    def get_embedding(self):
        return Word.embeddings.get_embedding(self._text)

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value
        self._data_changed = True
        self.embedding = self.get_embedding()
        self.notify()

    def has_changed(self):
        return self._data_changed

    def reset_change_flag(self):
        self._data_changed = False
