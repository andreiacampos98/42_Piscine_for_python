from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """
    Class representing a King, inheriting attributes and behaviors
    from both Baratheon and Lannister families.
    """
    def __init__(self, first_name, is_alive=True):
        """
        Initializes a King instance with given name and alive status.
        """
        super().__init__(first_name, is_alive)

    def get_eyes(self):
        """
        Returns the king's eye color.
        """
        return self.eyes

    def set_eyes(self, eyes):
        """
        Sets the king's eye color.
        """
        self.eyes = eyes

    def get_hairs(self):
        """
        Returns the king's hair color.
        """
        return self.hairs

    def set_hairs(self, hairs):
        """
        Sets the king's hair color.
        """
        self.hairs = hairs
