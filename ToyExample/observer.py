"""
Authours: 
    - Jasleen Kaur
    - Kevin Liu
    - Ma Toan Bach
"""
"""
About observer.py
    Contains the basis classes for the Observer Pattern, 
    specifically the Observer and Subject abstract classes. 
    These classes direct the notification mechanism 
    between subjects (observables) and observers when changes occur.
"""


from abc import ABC, abstractmethod
from typing import List


# << interface >> Subscriber
class Observer(ABC):
    @abstractmethod
    def update(self):
        pass


# Publisher, "has a" subscriber
class Subject(ABC):
    def __init__(self):
        self._observers: List[Observer] = []

    def attach(self, observer:Observer) -> int:
        ErrCode = 1
        if observer not in self._observers:
            self._observers.append(observer)
            ErrCode = 0
        # returns 1 if the subscriber already exists
        return ErrCode  

    def detach(self, observer:Observer) -> int:
        ErrCode = 1
        if observer in self._observers:
            self._observers.remove(observer)
            ErrCode = 0
        # returns 1 if the subscriber DNE
        return ErrCode
    
    def notify(self) -> int:
        ErrCode = 1
        try:
            for itr in self._observers:
                itr.update()
            ErrCode = 0
        except:
            pass
        # returns 1 if not iterable
        return ErrCode

