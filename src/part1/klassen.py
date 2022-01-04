class Rapper():
    """Simple representation of a Rapper"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def whoami(self):
        """Prints out who the rapper is"""
        print(f"{self.name.title()}, {self.age}")

    def rap_something(self):
        """A very simple rap song"""
        print(f"Ma name is {self.name} jo jo ")


class GermanRapper(Rapper):
    """Represents aspects of a Rapper, specific to rappers from german speaking areas"""

    def __init__(self, name, age):
        """Initialize attributes of parent class."""
        """Then initialize attributes specific to german rapper """
        super().__init__(name, age)
        self.drip = 100

    def describe_drip(self):
        """Describes Drip level"""
        drip_prefix = "WHACK DRIP"
        if self.drip >= 100:
            drip_prefix = "LOCO MEMBER DRIP"
        elif self.drip >= 50:
            drip_prefix = "OK Drip "

        print(f"{drip_prefix}: {self.drip}")

    def rap_something(self):
        """A simple rap in german"""
        print(f"Du hast {self.name} gemacht? Mashallah mach nochmal ")


shindy = GermanRapper("Shindy", 32)
dmx = Rapper("DMX", 40)
# shindy.rap_something()
# shindy.describe_drip()

rapper_list = [shindy, dmx]

for rapper in rapper_list:
    rapper.whoami()
    rapper.rap_something()
