from conductor import Conductor
from danfo_destination import Destination
from vanagon_bus import VanagonBus

money_collection = Conductor()
destinations = Destination()
vanagon_bus = VanagonBus()
bus_engine_running = True

while bus_engine_running:
    destination_choices = destinations.show_destinations()
    choice = input(f"Where you dey go? ({destination_choices}): ")
    if choice == "off":
        bus_engine_running = False
    elif choice == "report":
        vanagon_bus.report()
        money_collection.report_profit()
    else:
        location = destinations.find_destination(choice)
        if vanagon_bus.is_resource_sufficient(location) \
                and money_collection.payment_status(location.transport_fare):
            vanagon_bus.go_to_destination(location)


