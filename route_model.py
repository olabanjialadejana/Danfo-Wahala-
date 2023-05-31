from routes import routes_data
import random


class RouteModel:
    def __init__(self, route_name, bus_stops):
        self.route_name = route_name
        self.bus_stops = bus_stops
        self.base_fare = 100

    def calculate_fare(self, bus_stop):
        index_position = self.bus_stops.index(bus_stop)
        transport_fare = (index_position + 1) * self.base_fare
        return transport_fare

    def trip_consumption(self, transport_fare):
        petrol_volume = 0.001
        engine_oil_volume = 0.002
        radiator_water_volume = 0.003

        # Calculate consumption based on transport fare
        petrol_consumption = transport_fare * petrol_volume
        engine_oil_consumption = transport_fare * engine_oil_volume
        radiator_water_consumption = transport_fare * radiator_water_volume

        return {
            "petrol": petrol_consumption,
            "engine_oil": engine_oil_consumption,
            "radiator_water": radiator_water_consumption,
        }







