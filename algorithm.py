import datetime


class Algorithm:
    def __init__(self):
        pass

    # Time complexity: O(N^2)
    def nearest_neighbor(self, truck, package, distance, hour, minute):
        item = None
        item_list = []
        optimized_route = []
        algo_time = datetime.datetime(1, 1, 1, hour, minute)
        stop_algo = 0

    # Grab the package info and put it into a list
        for items in truck.storage:
            item_list.append(package.search_package(items))

    # Label packages as 'Out for delivery'
    # Also corrects the delivery info for package #9
        for items in item_list:
            items[8] = "OUT FOR DELIVERY"
            if items[0] == "9":
                items[1] = "410 S State St"
                items[4] = "84111"

    # Find the shortest route between the current position and the next position
    # Once that is found, deliver the package and label it as such
        current_location = truck.current_pos
        # Start of the nearest neighbor algorithm
        while len(item_list) is not 0 and stop_algo is 0:
            current_best_route = 100.0  # These are set to a high number so they are easily overwritten
            best_route = 100.0

            for item in item_list:
                route = self.get_route(current_location, distance.list_to_string(item[1]), distance)
                if route > current_best_route:
                    pass  # Ignore it since it is not optimal
                elif route < current_best_route:
                    current_best_route = route  # Override the current best route
                if current_best_route < best_route:
                    best_route = current_best_route  # Best route is the most optimal route

            current_location = item[1]
            # Pass time
            minutes_passed = best_route / truck.speed
            truck.increment_time(minutes_passed)

            # Stop delivering packages if we have reached the target time
            if truck.time > algo_time:
                stop_algo = 1
            else:
                item[8] = "DELIVERED"
                item[9] = "%d : %d : %d" % (truck.time.hour, truck.time.minute, truck.time.second)
                item_list.remove(item)  # Package is now delivered
                truck.distance_travelled += best_route
                optimized_route.append(best_route)

        if len(item_list) is 0:  # If there are no more packages, its time to head back to the hub
            route = self.get_route(current_location, "4001 South 700 East", distance)
            truck.distance_travelled += route
            minutes_passed = route / truck.speed
            truck.increment_time(minutes_passed)

            truck.return_time = truck.time
            truck.current_pos = "4001 South 700 East"
            truck.route.append(optimized_route)

    # Takes the row and column and returns the distance between the points
    # Time complexity: O(N^2)
    @staticmethod
    def get_route(row, column, distance):
        x = int(distance.get_row(distance.list_to_string(row)))
        y = int(distance.get_row(column))
        route = distance.list[x][y]
        return float(route)
