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


# print(to_day_of_week('20-11-2021'))


def point_inside_polygon(lon=-122.7924463, lat=45.4519896, polygons_json_path='5G_tahtiluokka_3.json'):
    """
    Check if a location Longitude/Latitude is inside a polygon
    """
    # depending on your version, use: from shapely.geometry import shape, Point

    # load GeoJSON file containing sectors
    with open(polygons_json_path) as f:
        js = json.load(f)

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
