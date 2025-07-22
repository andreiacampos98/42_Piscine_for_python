class calculator:
    """Calculator class with static methods for vector operations"""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Returns the dot product (scalar product) of two vectors."""
        result = 0
        for x, y in zip(V1, V2):
            result += x * y
        print(f"Dot product is {result}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """
        Adds two vectors element-wise.
        """
        result = []
        for x, y in zip(V1, V2):
            result.append(x+y)
        print(f"Add Vector is {result}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """
        Subtracts the second vector from the first element-wise.
        """
        result = []
        for x, y in zip(V1, V2):
            result.append(x-y)
        print(f"Sous Vector is {result}")
