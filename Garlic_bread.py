from Pastry import Pastry

class Garlic_bread (Pastry):
    cost=10
    calories=700
    shapes={1: "chala", 2: "circle"}

    def __init__(self):
        super().__init__()
        self.shape=""
        self.sause=False

    def chooseShape(self):
        """Shows the customer the possible shapes of bread"""
        print("Choose shape:")
        for key, shape in self.shapes.items():
            print(f"    For {shape} press {key}")
        self.shape= self.shapes[int(input())]

    def ask_for_sauce(self):
        """Ask the user if he wants sauce"""
        sauce_choice = lambda choice: True if choice == 1 else False

        try:
            choice = int(input("Do you want sauce? (1 for Yes, 2 for No): "))
            error=0
        except ValueError:
            print("Invalid input. Sauce will not be added.")
            error=1
        while error==1:
            try:
                choice = int(input("Do you want sauce? (1 for Yes, 2 for No): "))
                error = 0
            except ValueError:
                print("Invalid input. Sauce will not be added.")
                error = 1

        self.sauce = sauce_choice(choice)