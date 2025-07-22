from abc import ABC, abstractmethod


class Character(ABC):
    """Your docstring for Character Class"""
    def __init__(self, first_name, is_alive=True):
        """Your docstring for Constructor"""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Your docstring for die Method"""
        pass


class Stark(Character):
    """Your docstring for Stark Class"""
    def die(self):
        """Your docstring for die Method"""
        self.is_alive = False
