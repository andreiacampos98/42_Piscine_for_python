import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """The functions generate a random id"""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """A class Student is created with name, surname and active=True.
    A login and an id is also definied. When we define the login and id we put
    init=False to not allow pass the parameter when we create an object.
    Field makes the function is called everytime
    that we instantiate a new object."""
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(default_factory=generate_id, init=False)

    def __post_init__(self):
        """The login is build with the first letter of name and the surname"""
        self.login = f"{self.name[0].upper()}{self.surname.lower()}"
