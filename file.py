import csv
from hash import Hash


class Package:
    def __init__(self):
        self.package_hash = Hash()

    # Load package data into the hash table
    # Time complexity: O(N^2)
    def load_package_data(self, filename):
        with open(filename) as csv_file:
            read_csv = csv.reader(csv_file, delimiter=',')
            for rows in read_csv:
                if rows[7] == "Delayed on flight---will not arrive to depot until 9:05 am" or "Wrong address listed":
                    rows.append("DELAYED")  # Marks delayed packages as DELAYED
                else:
                    rows.append("AT THE HUB")  # If the packages are not delayed, they are at the HUB
                rows.append("NOT DELIVERED")  # No packages have been delivered yet, so they are marked as such
                self.package_hash.insert(int(rows[0]), rows)
        return self.package_hash

    # Finds a specific package via package ID
    # Time complexity: O(1)
    def search_package(self, package_id):
        return self.package_hash.search(package_id)

    # Prints out all packages
    # Time complexity: O(N)
    def get_all_packages(self):
        num = 1
        while num < 41:
            print self.search_package(num)
            num += 1


class Distance:
    def __init__(self):
        self.list = []

    # Load the distance data into a 2D array (list of lists)
    # Time complexity: O(N^2)
    def load_distance_data(self, filename):
        with open(filename) as csv_file:
            read_csv = csv.reader(csv_file, delimiter=',')
            for rows in read_csv:
                self.list.append(rows)
        return self.list

    # Prints the list of addresses and their distance from each other
    # Time complexity: O(1)
    def get_distance_data(self):
        print(self.list)

    # Grabs the row number for the street name
    # Time complexity: O(N)
    def get_row(self, string):
        row_num = 0
        for row in self.list:
            if row[0] == string:
                return row_num
            else:
                row_num += 1

    # Converts a list element to a string
    # Time complexity: O(N)
    @staticmethod
    def list_to_string(input_string):
        string = ''
        for element in input_string:
            string += element
        return string
