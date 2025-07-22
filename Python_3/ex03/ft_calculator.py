class calculator:
    """calculator class that is able to do calculations (addition,
    multiplication, sub-traction, division) of vector with a scalar."""

    def __init__(self, vector):
        """Initialize with a list of floats"""
        self.vector = vector

    def __add__(self, object) -> None:
        """Adds a scalar to each element of the vector."""
        self.vector = [x + object for x in self.vector]
        print(self.vector)

    def __mul__(self, object) -> None:
        """ Multiplies each element of the vector by a scalar."""
        self.vector = [x * object for x in self.vector]
        print(self.vector)

    def __sub__(self, object) -> None:
        """Subtracts a scalar from each element of the vector."""
        self.vector = [x - object for x in self.vector]
        print(self.vector)

    def __truediv__(self, object) -> None:
        """Divides each element of the vector by a scalar."""
        if object == 0:
            print("Error: Division by 0.")
            return
        self.vector = [x / object for x in self.vector]
        print(self.vector)
