class calculator:
    """calculator class that is able to do calculations (addition, multiplication, sub-
traction, division) of vector with a scalar."""

    def __init__(self, vector):
        """Initialize with a list of floats"""
        self.vector = vector

    def __add__(self, object) -> None:
        self.vector = [x + object for x in self.vector]
        print(self.vector)

    def __mul__(self, object) -> None:
        self.vector = [x * object for x in self.vector]
        print(self.vector)

    def __sub__(self, object) -> None:
        self.vector = [x - object for x in self.vector]
        print(self.vector)

    def __truediv__(self, object) -> None:
        if object == 0:
            print("Error: Division by 0.")
            return
        self.vector = [x / object for x in self.vector]
        print(self.vector)
