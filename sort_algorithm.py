import data_structures

# this method contains the algorithm which, given a list of packages,
# chooses the order of packages for delivery. time complexity: O(N)
def choose_delivery_order(packages_list):

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
        ordered_list.append(nearest_package)
        current_location_id = nearest_package.get_location_id()
        total_mileage += lowest_distance
        unordered_list.remove(nearest_package)
    return ordered_list, total_mileage

# check the distance between two locations. time complexity: O(1)
def check_distance(current_location, check_location):
    distances_matrix = data_structures.import_distances_from_csv()
    distance = distances_matrix[current_location][check_location]
    if distance == '':
        distance = distances_matrix[check_location][current_location]
    return float(distance)




