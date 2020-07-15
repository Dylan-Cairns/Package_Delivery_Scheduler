import model

def main():
    if __name__ == "__main__":
        main()


packages_list = model.import_packages_from_CSV()
#packages_list.print_packages_list()

package1 = packages_list.get_package(5)
print(package1)

location_dictionary = model.LocationDictionary()
print(location_dictionary.get_location_id(package1.get_address()))
print(location_dictionary.get_address(19))
