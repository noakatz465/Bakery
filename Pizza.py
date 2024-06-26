from Pastry import Pastry

class Pizza (Pastry):
    extras={
        1: "olives",
        2: "tomatoes",
        3: {1:"green olives", 2:"black olives"},
        4: "bulgarian_cheese"
    }
    costs= {"s": 30, "m": 45, "l": 60}
    calories={"s": 1000, "m": 1500, "l": 2000}

    def __init__(self):
        super().__init__()
        self.name="pizza"
        self.size=""
        self.my_extras=[]
        self.cost=0
        self.calories=0
        #self.flour_type=Pastry.flour_type

    def addExtras(self):
        """Shows the customer the possible pizza toppings"""
        print("Choose extras:")

        def generate_extras():
            for key, extra in self.extras.items():
                press = 0
                try:
                    press = int(input(f"    for {extra} press 1, next press 0"))
                    error = 0
                except ValueError:
                    print("Please enter 1 or 0")
                    error = 1

                while error == 1 or (press != 0 and press != 1):
                    try:
                        press = int(input(f"    for {extra} press 1, next press 0"))
                        error = 0
                    except ValueError:
                        print("Please enter 1 or 0")
                        error = 1

                if press != 0:
                    yield extra

        # Using the generator to create the list of extras
        self.my_extras = list(generate_extras())

    def chooseSize(self):
        """Shows the customer the possible pizza sizes"""
        print("Choose size:")
        for size,cost in self.costs.items():
            print(f"    {size}: {cost} ILS")
        selectedSize=input()
        while selectedSize!='s' and selectedSize!='m' and selectedSize!='l':
            print("Error! The key you selected does not exist")
            for size, cost in self.costs.items():
                print(f"    {size}: {cost} ILS")
            selectedSize=input()
        self.size=selectedSize
        self.cost=self.costs[self.size]