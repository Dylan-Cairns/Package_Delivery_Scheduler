import data_storage
import sort_algorithm
import package
import logistics


def main():
    if __name__ == "__main__":
        main()

# load package data from CSV
packages_list = data_storage.import_packages_from_csv()

# TESTING SORT ALGORITHM
# short_list = []
# for x in range(0,26):
#     temp_package = packages_list.get_package(x)
#     short_list.append(temp_package)
# for package in short_list:
#     print(package)
# sort_algorithm.choose_delivery_order(short_list)

logistics = logistics.Logistics()
logistics.load_trucks()
truck1 = logistics.truck1
truck2 = logistics.truck2
print("Truck 1")
sort_algorithm.choose_delivery_order(truck1)
print("Truck 2")
sort_algorithm.choose_delivery_order(truck2)
