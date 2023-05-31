from route_model import RouteModel


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







