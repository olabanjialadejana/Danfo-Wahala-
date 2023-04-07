from money_collection import MoneyCollection
from danfo_destination import Destination
from vanagon_bus import VanagonBus

money_collection = MoneyCollection()
destination = Destination()
vanagon_bus = VanagonBus()
bus_engine_running = True

while bus_engine_running:
    destination_choices = destination.show_destinations()
    choice = input(f"Where you dey go? ({destination_choices}): ")
    if choice == "off":
        bus_engine_running = False
    elif choice == "report":
        vanagon_bus.report()
        money_collection.report()
    else:
        location = destination.find_destination(choice)
        if vanagon_bus.is_resource_sufficient(location) \
                and money_collection.make_payment(location.transport_fare):
            vanagon_bus.go_to_destination(location)


