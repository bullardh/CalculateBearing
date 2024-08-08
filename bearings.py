# Description: Calculates bearings on a map and determines the direction of a location in
#              relation to another location.

import math


def calc_bearing(latitude1, longitude1, latitude2, longitude2):
    """
    Calculates the bearing based off of two points with the given latitudes and longitudes.
    :param latitude1: Location1's latitude information
    :param longitude1: Location1's longitude information
    :param latitude2: Location2's latitude information
    :param longitude2: Location2's longitude information
    :return: bearing information
    """
    dLon = (longitude2 - longitude1)
    x = math.cos(math.radians(latitude2)) * math.sin(math.radians(dLon))
    y = math.cos(math.radians(latitude1)) * math.sin(math.radians(latitude2)) - math.sin(math.radians(latitude1)) * math.cos(math.radians(latitude2)) * math.cos(math.radians(dLon))
    bearing = math.atan2(x, y)   # use atan2 to determine the quadrant
    bearing = math.degrees(bearing)

    return bearing


def calc_nsew(lat, long, lat_b, long_b):
    """
    Calculates the direction of location2, in relation to location1.
    :param lat: Location1's latitude
    :param long: Location1's longitude
    :param lat_b: Location2's latitude
    :param long_b: Location2's longitude
    :return: the direction of Location2 in relation to Location1
    """
    points1 = ["north", "north east", "east", "south east", "south", "south west", "west", "north west"]
    bearing = calc_bearing(lat, long, lat_b, long_b)
    bearing += 22.5
    bearing = bearing % 360
    bearing = int(bearing / 45)      # values 0 to 7
    NSEW = points1[bearing]

    return NSEW


if __name__ == '__main__':
    # River Bottoms 40.3188° N, 111.6452° W
    lat1 = 40.3188
    long1 = 111.6452
    # Rock Canyon Cave 40.2674° N, 111.6067° W
    lat2 = 40.2674
    long2 = 111.6067

    points = calc_nsew(lat1, long1, lat2, long2)
    cal_bear = calc_bearing(lat1, long1, lat2, long2)
    print(f'"The Rock Canyon Cave is " + {points} + " of the River Bottoms"')
    print(f'"Actually bearing of " {cal_bear} "')


    # River Bottoms 40.327459, -111.632306
    lat1 = 40.327459
    long1 = -111.632306
    # Luna Trail 40.320533, -111.634047
    lat2 = 40.320533
    long2 = -111.634047

    points = calc_nsew(lat1, long1, lat2, long2)
    calbear = calc_bearing(lat1, long1, lat2, long2)
    print(f'The Luna Trail is {points} of the River Bottoms')
    print(f'Actually bearing of {calbear}')
