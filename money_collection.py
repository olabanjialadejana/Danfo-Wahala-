class MoneyCollection:
    CURRENCY = "₦"

    NOTE_VALUES = {
        "faiba": 10,
        "muri/shandi": 20,
        "wazo": 50,
        "ten faiba": 100,
        "twenty faiba": 200,
        "figo": 500,
        "one thousand": 1000,
    }

    def __init__(self):
        """Attributes of money collection"""
        self.profit = 0
        self.money_received = 0

    def report(self):
        """This method prints a report
        of money made by the conductors"""
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_cash(self):
        """This method returns the bus fare collected from a passenger"""
        print("Owo mi da? 😠")
        for note in self.NOTE_VALUES:
            self.money_received += int(input(f"How many {note}:")) * self.NOTE_VALUES[note]
        return self.money_received

    def make_payment(self, transport_fare):
        """This method returns True when payment os accepted, or False if insufficient"""
        self.process_cash()
        if self.money_received >= transport_fare:
            change = round(self.money_received - transport_fare, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += transport_fare
            self.money_received = 0
            return True
        else:
            print("Iyalaya e. Koshi danu. The conductor has thrown "
                  "you off the moving bus 😡😡😡. Hope you are not injured sha?")
            self.money_received = 0
            return False
