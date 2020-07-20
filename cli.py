import simulation
import datetime


# Command line interface class. This class will call the simulation class,
# run the simulation, and then allow the user to check for status as desired.
class CommandLineInterface:
    def __init__(self):
        print("Executing delivery simulation: \n")
        # create an instance of the simulation class time complexity for the simulation is O(N^2)
        self.sim = simulation.Simulation()
        self.sim.run_simulation()

        print("Criteria G1, G2, G3: Status for all packages at times 9am, 10am, and 1pm:\n")
        check_time1 = datetime.datetime(101, 1, 1, 9, 0, 00)
        self.sim.get_all_packages_status(check_time1)
        check_time2 = datetime.datetime(101, 1, 1, 10, 0, 00)
        self.sim.get_all_packages_status(check_time2)
        check_time3 = datetime.datetime(101, 1, 1, 13, 0, 00)
        self.sim.get_all_packages_status(check_time3)

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
