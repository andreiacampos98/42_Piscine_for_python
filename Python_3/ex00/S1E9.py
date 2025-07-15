from abc import ABC, abstractmethod


class Character(ABC):
    """Your docstring for Class"""
    def __init__(self, first_name):
        self.first_name = first_name
        self.is_alive = True

    @abstractmethod
    def die():
        pass


class Stark(Character):
    """Your docstring for Class"""
    def die():
        is_alive = False

