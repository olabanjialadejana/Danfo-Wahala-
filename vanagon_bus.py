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

    def is_resources_enough(self, bus_stop):
        index_position = RouteModel.bus_stops.index(bus_stop)
        transport_fare = (index_position + 1) * RouteModel.base_fare
        petrol_volume = 0.001
        engine_oil_volume = 0.002
        radiator_water_volume = 0.003

        # Calculate consumption based on transport fare
        petrol_consumption = transport_fare * petrol_volume
        engine_oil_consumption = transport_fare * engine_oil_volume
        radiator_water_consumption = transport_fare * radiator_water_volume

        consumption = {
            "petrol": petrol_consumption,
            "engine oil": engine_oil_consumption,
            "radiator water": radiator_water_consumption,
        }


    def move_to_destination(self, bus_stop):
        """This method deducts the vanagon bus requirements (petrol, engine oil,
        and radiator water as each trip is completed"""
        consumption = RouteModel.vanagon_consumption(RouteModel.calculate_fare(bus_stop))
        for item in self.bus_requirements:
            self.bus_requirements[item] -= consumption[item]
        print("O wa oooooo. Oya bole, O loyun, O ponmo ooo. Aunty e smart up jare!!!!😠😠😠😠 ")



