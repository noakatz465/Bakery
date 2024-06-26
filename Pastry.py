class Pastry:
    allMoneyReceived=0
    def __init__(self):
        self.name=""
        self.flourType=""

    flour_type={1: "white", 2: "whole_wheat", 3: "spelt"}
    pastries = {1: "pizza", 2: "garlic bread"}

    def chooseFlourType(self):
        """Shows the customer the possible types of flour"""
        print("Choose flour type:")
        for key,flourType in self.flour_type.items():
            print(f"    For {flourType} press {key}")
        self.flour_type=self.flour_type[int(input())]

    def choosePastryName(self):
        """Shows the customer the possible pastries"""
        print("Choose pastry:")
        for key, pastry in self.pastries.items():
            print(f"    For {pastry} press {key}")
        try:
            self.name=self.pastries[int(input())]
            error=0
        except ValueError:
            print("Error! The key you selected does not a number")
            error=1
        except KeyError:
            print("Error! The key you selected does not exist")
            error = 1
        while error==1:
            try:
                self.name = self.pastries[int(input())]
                error = 0
            except ValueError:
                print("Error! The key you selected does not a number")
                error = 1
            except KeyError:
                print("Error! The key you selected does not exist")
                error=1