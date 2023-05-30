import random
from conductor import Conductor
from vanagon_bus import VanagonBus
from routes import routes_data
from route_model import RouteModel

conductor = Conductor()
vanagon_bus = VanagonBus()
bus_engine_running = True

routes_database = []
for route_name, bus_stops in routes_data.items():
    route_list = RouteModel(route_name, bus_stops)
    routes_database.append(route_list)

while True:
    current_route = random.choice(routes_database)
    print(f"Bus Route is {current_route.route_name}\n"
          f"Available bus stops are: {current_route.bus_stops}")
    choice = input("Where are you going?: ")
    if choice == "off":
        bus_engine_running = False
    elif choice == "report":
        vanagon_bus.report()
        conductor.report_profit()
    else:
        if choice in current_route.bus_stops:
            fare = current_route.calculate_fare(choice)
            for item in vanagon_bus.bus_requirements:
                if vanagon_bus.bus_requirements[item] > current_route.trip_consumption(fare)[item]:
                    print("Oya enter!!!")
                    conductor.payment_status(fare)
                    vanagon_bus.bus_requirements[item] -= current_route.trip_consumption(fare)[item]
                    break
        else:
            print("Sorry, I no dey go")



    if not bus_engine_running:
        break








