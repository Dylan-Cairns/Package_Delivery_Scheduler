import data_storage
import package

def choose_delivery_order(packages_list):
    location_dictionary = data_storage.LocationDictionary()
    current_location_id = 0
    unordered_list = packages_list.copy()
    ordered_list = []
    total_mileage = 0.0
    while len(ordered_list) < len(packages_list):
        lowest_distance = 9999
        nearest_package = None
        for package in unordered_list:
            if package not in ordered_list:
                current_distance = check_distance(current_location_id, package.get_location_id())
                if current_distance < lowest_distance:
                    lowest_distance = current_distance
                    nearest_package = package
        # print("Current location id: " + str(current_location_id) + ". current address: " +
        #       location_dictionary.get_address(current_location_id) +
        #       "\nClosest delivery : " + nearest_package.get_address() + " (location Id " +
        #       str(nearest_package.get_location_id()) + ") for package id: " + str(nearest_package.get_package_id())
        #       + ". it is " + str(lowest_distance) + " miles away.")
        ordered_list.append(nearest_package)
        current_location_id = nearest_package.get_location_id()
        total_mileage += lowest_distance
        unordered_list.remove(nearest_package)
    # print("delivery route: \n")
    # for package in ordered_list:
    #     print(package)
    print("total mileage: " + str(total_mileage))
    return ordered_list


def choose_next_package(current_location_id, packages_list):
    location_dictionary = data_storage.LocationDictionary()
    lowest_distance = 999
    nearest_package = None
    for package in packages_list:
        current_distance = check_distance(current_location_id, package.get_location_id())
        if current_distance < lowest_distance:
            lowest_distance = current_distance
            nearest_package = package
    # print("Current location id: " + str(current_location_id) + ". current address: " +
    #       location_dictionary.get_address(current_location_id) +
    #     "\nClosest delivery : " + nearest_package.get_address() + " (location Id " +
    #       str(nearest_package.get_location_id()) + ") for package id: " + str(nearest_package.get_package_id())
    #       + ". it is " + str(lowest_distance) + " miles away.")
    return nearest_package


def check_distance(current_location, check_location):
    distances_matrix = data_storage.import_distances_from_csv()
    distance = distances_matrix[current_location][check_location]
    if distance == '':
        distance = distances_matrix[check_location][current_location]
    # print("current location ID: " + str(current_location) + " next location: " + str(check_location) + " distance: "
    #       + str(distance))
    return float(distance)
