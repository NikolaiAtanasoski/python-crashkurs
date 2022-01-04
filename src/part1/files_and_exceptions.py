class SimpleAdder:
    """super simple two number adder"""

    @staticmethod
    def add_numbers(number1, number2):
        # try:
        return int(number1) + int(number2)

    def main(self):
        is_running = True
        number1 = 0
        number2 = "q"
        while is_running:
            try:
                print("please add two numbers for me to add")
                number1 = input("number1: ")
                number2 = input("number2: ")
                result = self.add_numbers(int(number1), int(number2))
                print(result)
            except ValueError:
                if number1 in ["q", "quit"] or number2 in ["q", "quit"]:
                    print("bye!")
                    break
                print("there seems to be an invalid number")


if __name__ == "__main__":
    adder = SimpleAdder()
    adder.main()
