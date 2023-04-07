class DanfoDestination:
    """This class models each destination"""
    def __init__(self, destination_name, petrol, engine_oil, radiator_water, transport_fare):
        self.destination_name = destination_name
        self.transport_fare = transport_fare
        self.bus_requirements = {
            "petrol": petrol,
            "engine_oil": engine_oil,
            "radiator_water": radiator_water
        }


class Destination:
    """This class models the destinations and
    corresponding requirements for the Vanagon bus to get there"""
    def __init__(self):
        self.destination = [
            DanfoDestination(destination_name="okokomaiko", engine_oil=10, radiator_water=10, petrol=25),
            DanfoDestination(destination_name="ikorodu", engine_oil=5, radiator_water=7, petrol=15),
            DanfoDestination(destination_name="lekki", engine_oil=12, radiator_water=15, petrol=35),
            DanfoDestination(destination_name="ayobo", engine_oil=13, radiator_water=17, petrol=40),
            DanfoDestination(destination_name="gbagada", engine_oil=5, radiator_water=4, petrol=10),
            DanfoDestination(destination_name="agege", engine_oil=8, radiator_water=8, petrol=17),

        ]

    def show_destinations(self):
        """This method returns a list of destinations for the bus"""
        options = ""
        for destination in self.destination:
            options += f"{destination.destination_name}/"
        return options

    def find_destination(self, passenger_destination):
        """This method searches the list of destinations by name.
        It returns a destination if it exists or returns None if otherwise"""
        for destination in self.destination:
            if destination.destination_name == passenger_destination:
                return destination
        print(f"Sorry, I no dey go {passenger_destination}. Alaye ma wole oo 😡😡😡")
