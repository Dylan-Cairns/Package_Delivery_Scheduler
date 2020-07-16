import package
import datetime
import sort_algorithm

def delivery_timeline(start_time, truckload):
    current_time = start_time
    current_location = 0
    updated_list = []
    for item in truckload:
        distance = sort_algorithm.check_distance(current_location, item.get_location_id())
        time_to_add = (distance*60)/18
        current_time += datetime.timedelta(minutes=time_to_add)
        status = package.Status(current_time, "delivered")
        item.update_status(status)
        updated_list.append(item)
    for item in updated_list:
        print(item)