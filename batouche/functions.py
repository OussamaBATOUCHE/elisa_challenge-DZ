import time
from shapely.geometry import shape, Point
import json
import pandas as pd


def to_day_of_week(date):
    """
    From day of month to day of week
    ex: to_day_of_week('20-11-2021') = 6 / type = int
    """
    date = pd.Timestamp(date)
    return date.dayofweek+1


def to_season(date):
    """
    From day of month to saison
    ex: to_saison('20-11-2021') = 4 / type = int
    1='winter'
    2='spring'
    3='summer'
    4='autumn'    
    """
    date = pd.Timestamp(date)
    if date.month in [1, 2, 3]:
        return 1
    if date.month in [4, 5, 6]:
        return 2
    if date.month in [7, 8, 9]:
        return 3
    if date.month in [10, 11, 12]:
        return 4


# print(to_saison('20-7-2021'))

def count_couvrage(polygons_json, lon=-122.7924463, lat=45.4519896):
    """
    Check if a location Longitude/Latitude is inside a polygon
    """

    js = polygons_json

    # Set new counter
    count = 0

    # construct point based on lon/lat returned by geocoder
    point = Point(lon, lat)
    # start_all = time.time()
    # check each polygon to see if it contains the point
    for feature in js['features']:
        polygon = shape(feature['geometry'])
        if polygon.contains(point):
            count += 1
            # print('Found containing polygon:', feature)

    # print(time.time() - start_all)
    return count


# point_inside_polygon(
#     polygons_json_path='/u/53/batouca1/unix/Downloads/Elisa Junction Challenge Materials-20211119T182547Z-001/Elisa Junction Challenge Materials/5G/5G_tahtiluokka_1.json')
