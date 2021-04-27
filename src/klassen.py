class Rapper():
    """Simple representation of a Rapper"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def rap_something(self):
        """A very simple rap song"""
        print(f"Ma name is {self.name} jo jo ")


class GermanRapper(Rapper):
    """Represents aspects of a Rapper, specific to rappers from german speaking areas"""

    def __init__(self, name, age):
        """Initialize attributes of parent class."""
        """Then initialize attributes specific to german rapper """
        super().__init__(name, age)
        self.dripminister = True

    def descripte_drip(self):
        if self.dripminister:
            print("LOCO MEMBER")
        else:
            print("Whack")


shindy = GermanRapper("Shindy", 32)
shindy.rap_something()
shindy.descripte_drip()
