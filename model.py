import csv

# Hash Map
class PackagesHashMap:
    def __init__(self):
        self.hash_map = [None] * 40

    def _get_hashkey(self, package_id):
        return package_id % 40

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

    def get_item(self, package_id):
        hash_key = self._get_hashkey(package_id)
        if self.hash_map[hash_key] is not None:
            for key_value_pair in self.hash_map[hash_key]:
                if key_value_pair[0] == hash_key:
                    return key_value_pair[1]
        return None

    def print_packages_list(self):
        for hashvalue in self.hash_map:
            for key_value_pair in hashvalue:
                print(key_value_pair[1])


# Package Object
class PackageObject:
    def __init__(self, package_id, address, city='', state='', zip_code='', deadline='', mass='', notes=''):
        self.package_id = int(package_id)
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.mass = mass
        self.notes = notes
        self.status = 'At Hub'
        #print('package created')


    def __str__(self):
        return str(self.package_id) + " " + self.address + " " + self.city + " " + self.state \
               + " " + self.zip_code + " " + self.deadline + " " + self.mass + " " + self.notes \
               + " " + self.status


#import package info from CSV

def import_packages_from_CSV():
    packages_hash_map = PackagesHashMap()
    with open('packages.csv', 'r') as csv_file:
        readCSV = csv.reader(csv_file, delimiter='\t')
        for row in readCSV:
            package_id = row[0]
            address = row[1]
            city = row[2]
            state = row[3]
            zip = row[4]
            deadline = row[5]
            mass = row[6]
            notes = row[7]
            temp_package = PackageObject(package_id, address, city, state, zip, deadline, mass, notes)
            packages_hash_map.add_item(temp_package)
    return packages_hash_map


# package1 = PackageObject(1, '5pm', 5)
# hash_map = PackagesHashMap()
# print(hash_map.add_item(package1))
# print(hash_map.get_item(package1.package_id))

packages_list = import_packages_from_CSV()
packages_list.print_packages_list()
