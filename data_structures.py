import csv
import package


# Hash Map
class PackagesHashTable:
    def __init__(self):
        self.hash_map = [None] * 40

    def _get_hashkey(self, package_id):
        return (package_id - 1) % 40

    # time complexity: O(1)
    def add_item(self, package_object):
        hash_key = self._get_hashkey(package_object.package_id)
        key_value_pair = [hash_key, package_object]
        if self.hash_map[hash_key] is None:
            self.hash_map[hash_key] = list([key_value_pair])
            return True
        else:
            for existing_pair in self.hash_map[hash_key]:
                if existing_pair[0] == hash_key:
                    existing_pair[1] = key_value_pair
                    return True
            self.hash_map[hash_key].append(key_value_pair)

    # time complexity: O(N) where N is the no of packages w the
    # same ID (so always O(1) for this project)
    def get_package(self, package_id):
        hash_key = self._get_hashkey(package_id)
        if self.hash_map[hash_key] is not None:
            for key_value_pair in self.hash_map[hash_key]:
                if key_value_pair[0] == hash_key:
                    return key_value_pair[1]
        return None

    # time complexity: O(N) where N is the no of packages w the
    # same ID (so always O(1) for this project)
    def get_package_by_address_id(self, address_id):
        for hash_key in self.hash_map:
            for key_value_pair in hash_key:
                temp_package = key_value_pair[1]
                if address_id == temp_package.get_location_id():
                    return temp_package
        return None

    # time complexity: O(N) where N is the no of hash keys
    # in the hash table (so 40 for this project)
    def print_packages_list(self):
        for hash_key in self.hash_map:
            for key_value_pair in hash_key:
                print(key_value_pair[1])

    # time complexity: O(N) where N is the no of packages
    # in the hash table (so 40 for this project)
    def get_packages_list(self):
        packages_list = []
        for hash_key in self.hash_map:
            for key_value_pair in hash_key:
                packages_list.append(key_value_pair[1])
        return packages_list


# import package info from CSV and store the data in a hash map. Use the location dictionary
# class to append address IDs to each package.
# time complexity: O(N) where N is the no of rows in the csv
def import_packages_from_csv():
    location_dictionary = LocationDictionary()
    packages_hash_map = PackagesHashTable()
    with open('packages.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\t')
        for row in csv_reader:
            package_id = row[0]
            address = row[1]
            address = address.replace('North', 'N').replace('South', 'S')
            address_id = location_dictionary.get_location_id(address)
            city = row[2]
            state = row[3]
            zip = row[4]
            deadline = row[5]
            mass = row[6]
            notes = row[7]
            temp_package = package.PackageObject(package_id, address, address_id, city, state, zip, deadline, mass, notes)
            packages_hash_map.add_item(temp_package)
    return packages_hash_map

# Import the distance table from the CSV
# time complexity: O(N) where N is the no of rows in the csv
def import_distances_from_csv():
    distances_matrix = []
    with open('distances.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            temp_row = row
            del temp_row[0]
            del temp_row[0]
            distances_matrix.append(temp_row)
    return distances_matrix

# Create a list which matches location IDs to an address
# time complexity: O(N) where N is the no of rows in the csv
class LocationDictionary:
    def __init__(self):
        self.location_dictionary = []
        with open('distances.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            temp_list = []
            for row in csv_reader:
                temp_list.append(row)
            for x in range(len(temp_list)):
                temp_row = [x, temp_list[x][0], temp_list[x][1]]
                temp_row[2] = temp_row[2].replace('North', 'N').replace('South', 'S')
                self.location_dictionary.append(temp_row)

    # time complexity: O(N) where N is the no of entries in the dict
    def get_location_id(self, address):
        for x in range(len(self.location_dictionary)):
            if self.location_dictionary[x][2] == address:
                return self.location_dictionary[x][0]
        return None

    # time complexity: O(N) where N is the no of entries in the dict
    def get_address(self, location_id):
        for x in range(len(self.location_dictionary)):
            if self.location_dictionary[x][0] == location_id:
                return self.location_dictionary[x][2]
        return None

    # time complexity: O(N) where N is the no of entries in the dict
    def print_location_dictionary(self):
        for row in self.location_dictionary:
            print('[%s]' % ', '.join(map(str, row)))
