import csv
import datetime


class Status:
    def __init__(self, timestamp=None, message='At Hub'):
        self.timestamp = timestamp
        # defaultvalues =  datetime(101,1,1,00,00,00)
        self.message = message

    def get_time(self):
        return self.timestamp

    def get_message(self):
        return self.message

    def __str__(self):
        return str(self.timestamp) + ": " + self.message


# Package Object
class PackageObject:
    def __init__(self, package_id, address, location_id, city='', state='', zip_code='', deadline='', mass='',
                 notes=''):
        self.package_id = int(package_id)
        self.address = address
        self.location_id = location_id
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.mass = mass
        self.notes = notes
        self.status = Status()

    def get_package_id(self):
        return self.package_id

    def get_location_id(self):
        return self.location_id

    def get_address(self):
        return self.address

    def get_status(self):
        return self.status

    def update_status(self, new_status):
        self.status = new_status

    # def __str__(self):
    #     return str(self.package_id) + " " + self.address + " " + str(self.location_id) + " " + self.city \
    #            + " " + self.state + " " + self.zip_code + " " + self.deadline + " " + self.mass \
    #            + " " + self.notes + " " + str(self.status)

    def __str__(self):
        return str(self.package_id) + " " + str(self.location_id) \
               + " " + self.deadline + " " + self.notes + " " + str(self.status)