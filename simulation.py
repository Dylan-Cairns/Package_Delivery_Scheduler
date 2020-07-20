import data_structures
import sort_algorithm
import package
import datetime


class Simulation:
    def __init__(self):
        self.package_hash_map = data_structures.import_packages_from_csv()
        self.all_packages = self.package_hash_map.get_packages_list()
        self.truck1 = []
        self.truck2 = []
        self.truck2_second_load = []
        self.total_distance = None
        self.t1_distance = None
        self.t2_distance = None
        self.t2_r2_distance = None
        self.start_time = None
        self.start_time2 = None
        self.start_time2_2 = None

    # load packages into trucks. Time complexity: O(N) where N is no of packages in the hash table
    def choose_trucks(self):
        self.truck1.clear()
        self.truck2.clear()
        self.truck2_second_load.clear()
        truck_1_packages = [13, 14, 15, 16, 19, 20, 2, 4, 5, 7, 34, 31]
        truck_2_packages = [3, 6, 18, 25, 36, 38, 1, 29, 30, 37, 40]
        for item in self.all_packages:
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
            else:
                self.truck2_second_load.append(item)

    # run a complete simulation. chooses which trucks to load packages onto,
    # sorts the loads which are on the trucks, calculates a timeline based on truck speed
    # time complexity: O(N) where N is total number of packages
    def run_simulation(self):
        self.choose_trucks()
        truck1_results = sort_algorithm.choose_delivery_order(self.truck1)
        self.truck1 = truck1_results[0]
        self.t1_distance = truck1_results[1]
        truck2_results = sort_algorithm.choose_delivery_order(self.truck2)
        self.truck2 = truck2_results[0]
        self.t2_distance = truck2_results[1]
        truck2_2_results = sort_algorithm.choose_delivery_order(self.truck2_second_load)
        self.truck2_second_load = truck2_2_results[0]
        self.t2_r2_distance = truck2_2_results[1]

        self.start_time = datetime.datetime(101, 1, 1, 8, 00, 00)
        print("\nTruck 1 depart hub: " + str(self.start_time.time()))
        self.truck1 = delivery_timeline(self.start_time, self.truck1)
        print("Truck 1 miles: " + str(self.t1_distance))

        self.start_time2 = datetime.datetime(101, 1, 1, 9, 5, 00)
        print("\nTruck 2 depart hub: " + str(self.start_time2.time()))
        self.truck2 = delivery_timeline(self.start_time2, self.truck2)

        return_distance = sort_algorithm.check_distance(self.truck2[-1].get_location_id(), 0)
        time_to_add = (return_distance * 60) / 18
        t2_return_time = self.truck2[-1].get_status().get_time() + datetime.timedelta(minutes=time_to_add)
        print("Truck 2 return to hub: " + str(t2_return_time.time()))
        self.t2_distance += return_distance
        print("Truck 2 miles (including return to hub): " + str(self.t2_distance))

        self.start_time2_2 = t2_return_time
        print("\nTruck 2 depart hub: " + str(self.start_time2_2.time()))
        self.truck2_second_load = delivery_timeline(self.start_time2_2, self.truck2_second_load)
        print("Truck 2 second run miles: " + str(self.t2_r2_distance))
        self.total_distance = self.t1_distance + self.t2_distance + self.t2_r2_distance
        print("\nTotal combined miles for all deliveries: " + str(self.total_distance) + "\n\n")

    # Time complexity: O(1)
    def get_package_status(self, package_id, check_time):
        loading_time = None
        temp_package = self.package_hash_map.get_package(package_id)
        delivery_time = temp_package.get_status().get_time()
        truck_number = None
        # check which truck the package is on
        if temp_package in self.truck1:
            loading_time = self.start_time
            truck_number = 1
        elif temp_package in self.truck2:
            loading_time = self.start_time2
            truck_number = 2
        elif temp_package in self.truck2_second_load:
            loading_time = self.start_time2_2
            truck_number = 2
        if check_time > delivery_time:
            print("packageID: " + str(package_id) + " delivered at " + str(delivery_time.time()))
        elif delivery_time > check_time > loading_time:
            print("packageID: " + str(package_id) + " " + str(check_time.time()) + ": in route on truck number " + str(truck_number))
        elif check_time < loading_time:
            print("packageID: " + str(package_id) + " " + str(check_time.time()) + ": at hub")

    # time complexity: O(N) where N is no of packages in the hash table
    def get_all_packages_status(self, check_time):
        for package in self.all_packages:
            self.get_package_status(package.get_package_id(), check_time)


# given a list of packages, generates a timeline based on the given truck speed of 18mph.
# time complexity: O(N) where N is no of packages in the given list.
def delivery_timeline(start_time, truckload):
    current_time = start_time
    current_location = 0
    updated_list = []
    for item in truckload:
        distance = sort_algorithm.check_distance(current_location, item.get_location_id())
        time_to_add = (distance*60)/18
        current_time += datetime.timedelta(minutes=time_to_add)
        current_location = item.get_location_id()
        status = package.Status(current_time, "delivered")
        item.update_status(status)
        updated_list.append(item)
        print("packageID: " + str(item.package_id) + " || locationID " + str(item.get_location_id())
               + " || Deadline: " + item.deadline + " || Status: " + str(item.status))
    return updated_list
