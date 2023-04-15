import random
import route_model
from conductor import Conductor
from vanagon_bus import VanagonBus
from routes import routes_data
from route_model import RouteModel

conductor = Conductor()
vanagon_bus = VanagonBus()
bus_engine_running = True

routes_database = []
for route in routes_data:
    route_name = route["route_name"]
    bus_stops = route["bus-stops"]
    route_list = RouteModel(route_name, bus_stops)
    routes_database.append(route_list)

# current_route = random.choice(routes_database)
# print(current_route.route_name)
# print(current_route.bus_stops)


while bus_engine_running:
    current_route = random.choice(routes_database)
    print(f"Bus Route is {current_route.route_name}\n"
          f"Available bus stops are: {current_route.bus_stops}")
    choice = input("Where you dey go?: ")
    if choice == "off":
        bus_engine_running = False
    elif choice == "report":
        vanagon_bus.report()
        conductor.report_profit()
    else:
        if choice in current_route.bus_stops:
            print("Oya enter!!!")
            # customer_payment = conductor.receive_payment()
            # print(customer_payment)
            # print(current_route.calculate_fare(bus_stops=choice))
            if conductor.payment_status(current_route.calculate_fare(choice)):
                vanagon_bus.move_to_destination(current_route.calculate_fare(choice))


        else:
            print("Sorry, Mi o Lo!!!")

