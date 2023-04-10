class Conductor:
    CURRENCY = "₦"

    NOTE_VALUES = {
        "faiba ('₦10')": 10,
        "muri/shandi ('₦20')": 20,
        "wazo ('₦50')": 50,
        "figo ('₦500')": 500,
        "one thousand ('₦1000')": 1000,
    }

    def __init__(self):
        """Attributes of conductor"""
        self.daily_profit = 0
        self.customer_payment = 0

    def report_profit(self):
        """This method prints a report
        of money made by a conductor"""
        print(f"Profit: {self.CURRENCY}{self.daily_profit}")

    def receive_payment(self):
        """This method returns the total amounting value of bus fare
        received from a passenger"""
        print("Owo mi da? 😠")
        for note in self.NOTE_VALUES:
            self.customer_payment += int(input(f"{note} melo: ")) * self.NOTE_VALUES[note]
        return self.customer_payment

    def payment_status(self, transport_fare):
        """This method returns True when payment os accepted,
        or False if insufficient"""
        self.receive_payment()
        if self.customer_payment >= transport_fare:
            change = round(self.customer_payment - transport_fare, 2)
            if change > 0:
                print(f"Gba change {self.CURRENCY}{change} e.")
            self.daily_profit += transport_fare
            self.customer_payment = 0
            return True
        else:
            print("Iyalaya e. Koshi danu. The conductor has thrown "
                  "you off the moving bus 😡😡😡 for not having enough cash."
                  " Hope you are not injured sha?")
            self.customer_payment = 0
            return False
