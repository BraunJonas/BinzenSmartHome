from abc import ABC, abstractmethod


class Actor(ABC):

    @abstractmethod
    def activateNightMode(self):
        pass

