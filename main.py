import data_storage
import sort_algorithm


def main():
    if __name__ == "__main__":
        main()


# load package data from CSV
packages_list = data_storage.import_packages_from_CSV()
# create distance matrix from CSV
distances_matrix = data_storage.import_distances_from_CSV()

# packages_list.print_packages_list()

location_dictionary = data_storage.LocationDictionary()
location_dictionary.print_location_dictionary()

# print(sort_algorithm.distance_between_two_locations(5,12))
short_list = []
for x in range(1,6):
    temp_package = packages_list.get_package(x)
    short_list.append(temp_package)
for package in short_list:
    print(package)

sort_algorithm.choose_next_package(10, short_list)


