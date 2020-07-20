import simulation
import datetime


# Command line interface class. All methods are O(1)
class CommandLineInterface:
    def __init__(self):
        print("Executing delivery simulation: \n")
        self.sim = simulation.Simulation()
        self.sim.run_simulation()

    # Time complexity O(1)
    def menu(self):
        choice = None
        while choice != 4:
            show_menu_text()
            choice = int(input())
            print(choice)
            if choice == 1:
                pkg_id = int(input("Enter a package id: "))
                try:
                    print(self.sim.package_hash_map.get_package(pkg_id))
                except:
                    print("invalid input\n")
                    continue
            elif choice == 2:
                pkg_id = int(input("Enter a package id: "))
                print("Enter a time. Input 4 digits to represent hour and minute,\n"
                      "with the hour and minute digits separated by a space. \n"
                      "(Example 09 30 for 9:30am): ")
                hour, minute = input().split()
                hour = int(hour)
                minute = int(minute)
                try:
                    time_variable = datetime.datetime(101, 1, 1, hour, minute, 00)
                    self.sim.get_package_status(pkg_id, time_variable)
                except:
                    print("invalid input\n")
                    continue
            elif choice == 3:
                print("Enter a time. Input 4 digits to represent hour and minute,\n"
                      "with the hour and minute digits separated by a space. \n"
                      "(Example 09 30 for 9:30am): ")
                hour, minute = input().split()
                hour = int(hour)
                minute = int(minute)
                try:
                    time_variable = datetime.datetime(101, 1, 1, hour, minute, 00)
                    self.sim.get_all_packages_status(time_variable)
                except:
                    print("invalid input\n")
                    continue
            if choice == 4:
                print("Goodbye")
                exit()

# Time complexity O(1)
def show_menu_text():
    print("Choose from the following options:\n" +
          "1. Look up a package\n" +
          "2. Look up a package status at a given time\n" +
          "3. Get status of all packages at a given time\n" +
          "4. Exit")
