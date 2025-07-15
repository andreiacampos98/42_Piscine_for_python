from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Class representing a King inheriting from Baratheon and Lannister"""
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)

    def get_eyes(self):
        return self.eyes

    def set_eyes(self, eyes):
        self.eyes = eyes

    def get_hairs(self):
        return self.hairs

    def set_hairs(self, hairs):
        self.hairs = hairs