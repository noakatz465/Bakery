import random

class Money:
    def __init__(self):
        self.profit = 0
        self.receipt_number = random.randint(1000, 10000)

    def report(self):
        """Prints the current profit"""
        print(f"The amount of money received so far: {self.profit} ILS")

    def payment(self, cost):
        """Takes the money for payment from the user"""
        self.profit += cost
        pay = 0
        try:
            pay = int(input("To pay by credit press 1, by cash press 2"))
            error = 0
        except ValueError:
            print("Error! The key you selected does not exist")
            error = 1
        while error == 1 or (pay != 1 and pay != 2):
            try:
                pay = int(input("To pay by credit press 1, by cash press 2"))
            except ValueError:
                print("Error! The key you selected does not exist")
                pay = int(input("To pay by credit press 1, by cash press 2"))
        print("Payment successfully received! Thank you for buying from us 🥳❤️")
        receipt_file = "receipt.txt"
        with open(receipt_file, "a") as receipt_file:
            receipt_file.write(f"Receipt Number: {self.receipt_number}\n")
            receipt_file.write(f"Payment Received: {cost} ILS\nPayment Method: {'Credit' if pay == '1' else 'Cash'}\n\n")
        print(f"Receipt saved as {receipt_file}")
        self.receipt_number+=1