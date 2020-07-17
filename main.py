import data_storage
import sort_algorithm
import package
import logistics
import timer
import datetime


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
logistics.choose_trucks()
truck1 = logistics.truck1
truck2 = logistics.truck2
truck1_second_load = logistics.truck1_second_load
print("Truck 1")
truck1 = sort_algorithm.choose_delivery_order(truck1)
print("Truck 2")
truck2 = sort_algorithm.choose_delivery_order(truck2)
print("Truck 1 load 2")
truck1_second_load = sort_algorithm.choose_delivery_order(truck1_second_load)

start_time = datetime.datetime(101,1,1,8,00,00)
print("Truck 1")
timer.delivery_timeline(start_time, truck1)

start_time2 = datetime.datetime(101,1,1,8,00,00)
print("Truck 2")
timer.delivery_timeline(start_time2, truck2)

start_time3 = datetime.datetime(101,1,1,9,30,00)
print("Truck 3")
timer.delivery_timeline(start_time3, truck1_second_load)

