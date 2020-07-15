import csv


# Hash Map
class PackagesHashMap:
    def __init__(self):
        self.hash_map = [None] * 40

    def _get_hashkey(self, package_id):
        return (package_id - 1) % 40

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

    def get_package(self, package_id):
        hash_key = self._get_hashkey(package_id)
        if self.hash_map[hash_key] is not None:
            for key_value_pair in self.hash_map[hash_key]:
                if key_value_pair[0] == hash_key:
                    return key_value_pair[1]
        return None

    def print_packages_list(self):
        for hash_key in self.hash_map:
            for key_value_pair in hash_key:
                print(key_value_pair[1])


# Package Object
class PackageObject:
    def __init__(self, package_id, address, address_id, city='', state='', zip_code='', deadline='', mass='', notes=''):
        self.package_id = int(package_id)
        self.address = address
        self.address_id = address_id
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.mass = mass
        self.notes = notes
        self.status = 'At Hub'
    
    def get_package_id(self):
        return self.package_id

    def get_address_id(self):
        return self.package_id

    def get_address(self):
        return self.address

    def __str__(self):
        return str(self.package_id) + " " + self.address + " " + str(self.address_id) + " " + self.city \
               + " " + self.state + " " + self.zip_code + " " + self.deadline + " " + self.mass \
               + " " + self.notes + " " + self.status


# import package info from CSV and store the data in a hash map. Use the location dictionary
# class to append address IDs to each package.
def import_packages_from_CSV():
    location_dictionary = LocationDictionary()
    packages_hash_map = PackagesHashMap()
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
            temp_package = PackageObject(package_id, address, address_id, city, state, zip, deadline, mass, notes)
            packages_hash_map.add_item(temp_package)
    return packages_hash_map


def import_distances_from_CSV():
    distances_matrix = []
    with open('distances.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            temp_row = row
            del temp_row[0]
            del temp_row[0]
            distances_matrix.append(temp_row)
    return distances_matrix


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

    def get_location_id(self, address):
        for x in range(len(self.location_dictionary)):
            if self.location_dictionary[x][2] == address:
                return self.location_dictionary[x][0]
        return None

    def get_address(self, location_id):
        for x in range(len(self.location_dictionary)):
            if self.location_dictionary[x][0] == location_id:
                return self.location_dictionary[x][2]
        return None

    def print_location_dictionary(self):
        for row in self.location_dictionary:
            print('[%s]' % ', '.join(map(str, row)))


# TESTING PACKAGE LIST
# packages_list = import_packages_from_CSV()
# packages_list.print_packages_list()

# TESTING DISTANCES LIST
# distances_matrix = import_distances_from_CSV()
# for row in distances_matrix:
#    print('[%s]' % ', '.join(map(str, row)))

# TESTING LOCATION DICTIONARY
#location_dictionary = LocationDictionary()
#location_dictionary.print_location_dictionary()
#print(location_dictionary.get_address(5))
#print(packages_list.get_package(5).get_package_id)
#print(location_dictionary.get_location_id(packages_list.get_package(5).get_package_id))
