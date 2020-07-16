import data_storage
import sort_algorithm
import package


class Logistics:
    def __init__(self):
        self.truck1 = []
        self.truck2 = []

    def load_trucks(self):
        package_hash_map = data_storage.import_packages_from_csv()
        all_packages = package_hash_map.get_packages_list()
        truck_2_packages = [3, 6, 9, 14, 16, 18, 20, 25, 28, 32, 36, 38]
        for item in all_packages:
            if item.get_package_id() not in truck_2_packages and len(self.truck1) < 16:
                self.truck1.append(item)
            else:
                self.truck2.append(item)

    def get_truck1(self):
        return self.truck1

    def get_truck2(self):
        return self.truck2


