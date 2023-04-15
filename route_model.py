def vanagon_consumption(transport_fare):
    petrol_volume = 2
    engine_oil_volume = 0.002
    radiator_water_volume = 0.003

    # This method calculates consumption based on transport fare
    petrol_consumption = transport_fare * petrol_volume
    engine_oil_consumption = transport_fare * engine_oil_volume
    radiator_water_consumption = transport_fare * radiator_water_volume

    return {
        "petrol": petrol_consumption,
        "engine oil": engine_oil_consumption,
        "radiator water": radiator_water_consumption
    }


class RouteModel:

    def __init__(self, route_name, bus_stops):
        self.route_name = route_name
        self.bus_stops = bus_stops
        self.base_fare = 100

    def calculate_fare(self, bus_stops):
        transport_fare = {}
        for i in range(len(self.bus_stops)):
            fare = self.base_fare + (i * 100)
            transport_fare[self.bus_stops[i]] = fare
        return transport_fare[bus_stops]


# TODO: NB: I actually wrote it like this below. But the interpreter claimed that the "vanagon consumption" method maybe
#  static. So it suggested i rewrite it as above. But I really dont understand why.
#  The code below is mine, but it was rearranged to the one above by the interpreter
#####################################################################################
# class RouteModel:
#
#     def __init__(self, route_name, bus_stops, base_fare):
#         self.route_name = route_name
#         self.bus_stops = bus_stops
#         self.base_fare = base_fare
#
#     def calculate_fare(self, bus_stop):
#         transport_fare = {}
#         for i in range(len(self.bus_stops)):
#             fare = self.base_fare + (i * 100)
#             transport_fare[self.bus_stops[i]] = fare
#         return transport_fare[bus_stop]
#
#     def vanagon_consumption(self, transport_fare):
#         petrol_volume = 2
#         engine_oil_volume = 0.002
#         radiator_water_volume = 0.003
#
#         # Calculate consumption based on transport fare
#         petrol_consumption = transport_fare * petrol_volume
#         engine_oil_consumption = transport_fare * engine_oil_volume
#         radiator_water_consumption = transport_fare * radiator_water_volume
#
#         return {
#             "petrol": petrol_consumption,
#             "engine oil": engine_oil_consumption,
#             "radiator water": radiator_water_consumption
#         }










