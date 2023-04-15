import route_model


class VanagonBus:
    """This class models the engine and
    working requirements of the Volkswagen Vanagon bus"""
    def __init__(self):
        self.bus_requirements = {
            "petrol": 500,
            "engine_oil": 70,
            "radiator_water": 100,
        }

    def report(self):
        """This method prints a report of engine resources"""
        print(f"petrol: {self.bus_requirements['petrol']}l")
        print(f"engine oil: {self.bus_requirements['engine_oil']}l")
        print(f"radiator water: {self.bus_requirements['radiator_water']}l")

    def move_to_destination(self, transport_fare):
        """This method deducts the vanagon bus requirements (petrol, engine oil,
        and radiator water as each trip is completed"""
        consumption = route_model.vanagon_consumption(transport_fare)
        for item in self.bus_requirements:
            if consumption[item] > self.bus_requirements[item]:
                print(f"Insufficient {item} to go there.")
                return False
            else:
                self.bus_requirements[item] -= consumption[item]
                print("O wa oooooo. Oya bole, O loyun, O ponmo ooo. Aunty e smart up jare!!!!😠😠😠😠 ")



