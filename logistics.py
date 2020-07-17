import data_storage
import sort_algorithm
import package


class Logistics:
    def __init__(self):
        self.truck1 = []
        self.truck2 = []
        self.truck1_second_load = []

    def choose_trucks(self):
        package_hash_map = data_storage.import_packages_from_csv()
        all_packages = package_hash_map.get_packages_list()
        truck_1_packages = [13, 14, 15, 16, 19, 20, 2, 4, 5, 7, 34]
        truck_2_packages = [3, 6, 18, 25, 28, 32, 36, 38, 1, 29, 30, 31, 37, 40]
        # truck_1_2ndload_packages = [2, 33, 11, 8, 17, 12, 21, 4, 5, 38, 34, 24, 23, 26, 10, 22]
        for item in all_packages:
            if item.get_package_id() == 9:
                item.address = "410 S State St"
                item.city = "Salt Lake City"
                item.zip_code = 8411
                item.location_id = 19
                item.notes = "address corrected at 10:21am"
            if item.get_package_id() in truck_1_packages:
                self.truck1.append(item)
            elif item.get_package_id() in truck_2_packages:
                self.truck2.append(item)
            else: # item.get_package_id() in truck_1_2ndload_packages:
                self.truck1_second_load.append(item)


