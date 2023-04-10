class DanfoRoute:
    """A blueprint for creating and updating routes within Lagos"""
    def __init__(self, route, bus_stops, interval_minutes):
        self.route = route
        self.bus_stops = bus_stops
        self.interval_minutes = interval_minutes

    def add_bus_stop(self, bus_stop_name):
        """This function adds bus stops to a danfo route"""
        self.bus_stops.append(bus_stop_name)

    def remove_bus_stop(self, bus_stop_name):
        """This function removes bus stops to a danfo route"""
        if bus_stop_name in self.bus_stops:
            self.bus_stops.remove(bus_stop_name)
        else:
            print(f"{bus_stop_name} not found")

    def list_bus_stops(self):
        """This function lists all bus stops along a danfo route"""
        number_of_bus_stops = 0
        for bus_stops in self.bus_stops:
            number_of_bus_stops += 1
            print(f"{number_of_bus_stops}. {bus_stops}")
        return number_of_bus_stops

    def find_bus_stop(self, bus_stop):
        """This function returns True if a bus stop
        exists along a route and False if it doesn't exist"""
        if bus_stop in self.bus_stops:
            return True
        else:
            return False

    def route_distance(self):
        number_of_bus_stops = self.list_bus_stops()
        distance = number_of_bus_stops * self.interval_minutes
        print(f"Total distance on {self.route} is {distance}Km")








