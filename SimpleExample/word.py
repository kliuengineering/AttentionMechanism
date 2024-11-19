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
"""


from observer import Subject


class Word(Subject):
    def __init__(self, text: str):
        super().__init__()
        self._text = text
        self._data_changed = False

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value
        self._data_changed = True
        self.notify()

    def has_changed(self):
        return self._data_changed

    def reset_change_flag(self):
        self._data_changed = False
