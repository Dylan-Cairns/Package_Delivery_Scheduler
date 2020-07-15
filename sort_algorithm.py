import data_storage


def choose_next_package(current_location_id, remaining_packages):
    location_dictionary = data_storage.LocationDictionary()
    lowest_distance = 999

    for package in remaining_packages:
        current_distance = distance_between_two_locations(current_location_id, package.get_address_id())
        if current_distance < lowest_distance:
            lowest_distance = current_distance
    print("Current location id: " + str(current_location_id) + ". current address: " +
          location_dictionary.get_address(current_location_id) +
        "\nClosest delivery : " + package.get_address() + " (location Id " +
          str(package.get_address_id()) + ") for package id: " + str(package.get_package_id())
          + ". it is " + str(lowest_distance) + " miles away.")


def distance_between_two_locations(current_location, check_location):
    distances_matrix = data_storage.import_distances_from_CSV()
    location_dictionary = data_storage.LocationDictionary()
    distance = distances_matrix[current_location][check_location]
    if distance == '':
        distance = distances_matrix[check_location][current_location]
    return float(distance)
    #print("Distance between " + location_dictionary.get_address(current_location) + " and " +
    #      location_dictionary.get_address(check_location) + ": \n" + str(distance))
