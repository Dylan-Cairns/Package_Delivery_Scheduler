# Hash Map oh yea
class HashMap:
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


# Package Object
class PackageObject:
    def __init__(self, package_id, deadline, mass, address = None):
        self.package_id = package_id
        self.address = address
        self.deadline = deadline
        self.mass = mass
        print('package created')


    def __str__(self):
        return str(self.package_id) + " " + self.deadline + " " + str(self.mass)


# Address Object
class AddressObject:
    def __init__(self, address, city, state, zip_code):
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code


package1 = PackageObject(1, '5pm', 5)
hash_map = HashMap()
print(hash_map.add_item(package1))
print(hash_map.get_item(package1.package_id))
