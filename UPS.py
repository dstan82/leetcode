def range_vehicles (vehicles, start, end):
    return sum(vehicles[start:end])


vehicles = [5, 6, 4, 4, 2, 1]

print(range_vehicles(vehicles, 1,3))