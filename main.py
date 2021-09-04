# Caleb Lugo #001217681
from truck import Truck
from algorithm import Algorithm
from file import Package, Distance

# Global variables
PACKAGE_FILE = "PackageFile.csv"
DISTANCE_FILE = 'DistanceTable.csv'

# Init trucks and their packages
# Manually load packages into each truck
truck1 = Truck()  # Truck1 handles packages with delays
truck1.storage = [6, 11, 12, 17, 19, 21, 22, 23, 24, 25, 26]
truck2 = Truck()  # Truck 2 handles packages with specific delivery instructions and strict delivery times
truck2.storage = [1, 3, 13, 14, 40, 16, 18, 20, 29, 30, 31, 34, 36, 37, 38, 15]
truck3 = Truck()  # Truck 3 handles the package with the wrong address and any extras
truck3.storage = [2, 4, 5, 7, 8, 9, 10, 27, 28, 32, 33, 35, 39]

# Init package and distance data
package = Package()
distance = Distance()
package.load_package_data(PACKAGE_FILE)
distance.load_distance_data(DISTANCE_FILE)

# Main program
# Time complexity: O(N^3)
# This is the time complexity for the entire program
if __name__ == '__main__':

    algorithm = Algorithm()
    program = 1

    print "************************************************"
    print "* Welcome to the WGUPS Delivery menu!          *"
    print "* Package #9 has the wrong address! The        *"
    print "* address will be corrected at 10:20AM         *"
    print "* We will now begin the delivery process       *"
    print "************************************************"

    # Program runs on a while loop that takes input
    # Program will continuously run as long as the user does not enter 9
    while program is not 0:
        print "*************************************************"
        print "* To deliver packages, enter 1                  *"
        print "* To view package status, enter 2               *"
        print "* To check truck mileage and time, enter 3      *"
        print "* To check packages at a specific time, enter 4 *"
        print "* To close the program, enter 9                 *"
        print "*************************************************"
        menu_input = input()

        # Runs the nearest neighbor algorithm for all trucks
        # Hour 17 = 5:00PM, the algo will run to the end of the day by default
        if menu_input is 1:
            # Package is reloaded in case the user runs the algo multiple times
            # in the same session, truck data is also reset
            package.load_package_data(PACKAGE_FILE)
            truck1.set_time(9, 5, 0)
            truck1.distance_travelled = 0.0
            truck1.return_time = None
            truck2.set_time(8, 0, 0)
            truck2.distance_travelled = 0.0
            truck2.return_time = None
            algorithm.nearest_neighbor(truck2, package, distance, 17, 0)
            algorithm.nearest_neighbor(truck1, package, distance, 17, 0)

            truck3.distance_travelled = 0.0
            truck3.return_time = None
            # Truck 3 will depart when truck 1 returns to the HUB
            if truck1.return_time is not None:
                truck3.set_time(truck1.time.hour, truck1.time.minute, truck1.time.second)
                algorithm.nearest_neighbor(truck3, package, distance, 17, 0)
            print "* Finished! *"

        # Returns all the package data
        if menu_input is 2:
            print package.get_all_packages()

        # Returns the trucks travel distance and finish time
        if menu_input is 3:
            print "*************************************************"
            print "* Truck 1 travelled %f miles *" % truck1.distance_travelled
            print "* Truck 2 travelled %f miles *" % truck2.distance_travelled
            print "* Truck 3 travelled %f miles *" % truck3.distance_travelled
            total_distance = truck1.distance_travelled + truck2.distance_travelled + truck3.distance_travelled
            print "* Total distance travelled: %f *" % total_distance
            print "*************************************************"
            print "* Truck 1 returned at %s *" % truck1.return_time
            print "* Truck 2 returned at %s *" % truck2.return_time
            print "* Truck 3 returned at %s *" % truck3.return_time
            print "*************************************************"

        # Runs the nearest neighbor algorithm for all trucks with a specific time goal
        if menu_input is 4:
            print "*************************************************"
            print "* Enter an hour (24H Format)                    *"
            print "*************************************************"
            hour_input = input()
            print "*************************************************"
            print "* Enter minute(s)                               *"
            print "*************************************************"
            minute_input = input()
            # Package is reloaded in case the user runs the algo multiple times
            # in the same session, truck data is also reset
            package.load_package_data(PACKAGE_FILE)
            truck1.set_time(9, 5, 0)
            truck1.distance_travelled = 0.0
            truck1.return_time = None
            truck2.set_time(8, 0, 0)
            truck2.distance_travelled = 0.0
            truck2.return_time = None
            algorithm.nearest_neighbor(truck2, package, distance, hour_input, minute_input)
            algorithm.nearest_neighbor(truck1, package, distance, hour_input, minute_input)

            truck3.distance_travelled = 0.0
            truck3.return_time = None
            # Truck 3 will depart when truck 1 returns to the HUB
            if truck1.return_time is not None:
                truck3.set_time(truck1.time.hour, truck1.time.minute, truck1.time.second)

                algorithm.nearest_neighbor(truck3, package, distance, hour_input, minute_input)
            print "* Finished! *"
            print "* Package status at %d : %d *" % (hour_input, minute_input)
            package.get_all_packages()

        # Exits the program
        if menu_input is 9:
            print "*************************************************"
            print "* Goodbye!                                      *"
            print "*************************************************"
            program = 0
