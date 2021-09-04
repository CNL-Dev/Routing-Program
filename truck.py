import datetime


class Truck:
    def __init__(self):
        self.speed = 0.3  # 18MPH = 0.3 Mile per minute
        self.storage = [None] * 16
        self.current_pos = "4001 South 700 East"  # At the HUB
        self.route = []
        self.distance_travelled = 0.0
        self.time = datetime.datetime
        self.departure_time = None
        self.return_time = None

    # Add a package to the trucks storage
    # Time complexity: O(1)
    def add_package(self, package):
        self.storage.append(package)

    # Removes a package from the truck storage
    # Time complexity: O(1)
    def remove_package(self, package):
        self.storage.pop(package)

    # Sets the time for the truck
    # Time complexity: O(1)
    def set_time(self, hour, minute, second):
        self.time = datetime.datetime(1, 1, 1, hour, minute, second)
        self.departure_time = self.time

    # Increments the time for the truck
    # Time complexity: O(1)
    def increment_time(self, time):
        increment = self.time + datetime.timedelta(minutes=time)
        self.time = increment

    # Gets the current time for the truck
    # Time complexity: O(1)
    def get_return_time(self):
        return self.return_time
