import pandas as pd
import random
import requests
from batouche.functions import *

def load_postal_code(file_path):

    postal_codes = {}

    with open(file_path, encoding="ISO-8859-1") as fp:
        line = fp.readline()
        while line:
            pc = line[13:18]
            street = line[102:132].strip()
            if street != "":
                if pc in postal_codes:
                    postal_codes[pc].append(street)
                else:
                    postal_codes[pc] = []
                    postal_codes[pc].append(street)
            line = fp.readline()

    return postal_codes

def address_to_coordinates(address):

    r = requests.get('https://api.digitransit.fi/geocoding/v1/search?text='+address+'&layers=address')
    if r.status_code == 200:
        response = r.json()
        lon = response["features"][0]["geometry"]["coordinates"][0]
        lat = response["features"][0]["geometry"]["coordinates"][1]
        return lon, lat
    else:
        return None

def normalize(x_list, x_min, x_max):

    to_return = []
    for x in x_list:
        to_return.append((x - x_min)/(x_max - x_min))

def build_data_set(mobility_ds, postal_codes):

    with open("/Users/oussama/Downloads/5G/5G_tahtiluokka_1.json") as f:
        five_g_1 = json.load(f)

    with open("/Users/oussama/Downloads/5G/5G_tahtiluokka_2.json") as f:
        five_g_2 = json.load(f)

    with open("/Users/oussama/Downloads/5G/5G_tahtiluokka_3.json") as f:
        five_g_3 = json.load(f)

    cache = {}
    data_set = []
    data = pd.read_csv(mobility_ds, sep=";")
    df = pd.DataFrame(data, columns=['DATE', 'LKM', 'KOTIPOSTINRO', 'POSTINRO'])
    df = df.head(50)
    error_count = 0
    for index, row in df.iterrows():
        source_pc = str(row['KOTIPOSTINRO'])
        destination_pc = str(row['POSTINRO'])
        date = row['DATE']
        lkm = row['LKM']

        if len(source_pc) < 5:
            padding = '0' * (5 - len(source_pc))
            source_pc = padding + source_pc

        if len(destination_pc) < 5:
            padding = '0' * (5 - len(destination_pc))
            destination_pc = padding + destination_pc

        if source_pc not in postal_codes or destination_pc not in postal_codes:
            error_count += 1
        else:
            pass

            source_address = random.choice(postal_codes[source_pc])
            destination_address = random.choice(postal_codes[destination_pc])

            if source_address in cache:
                lon_s, lat_s = cache[source_address]
            else:
                lon_s, lat_s = address_to_coordinates(source_address)
                cache[source_address] = lon_s, lat_s

            if destination_address in cache:
                lon_d, lat_d = cache[destination_address]
            else:
                lon_d, lat_d = address_to_coordinates(destination_address)
                cache[destination_address]  = lon_d, lat_d

            count_s = count_couvrage(five_g_1, lon_s, lat_s)
            count_s += count_couvrage(five_g_2, lon_s, lat_s)
            count_s += count_couvrage(five_g_3, lon_s, lat_s)
            e_s = count_s/lkm

            count_d = count_couvrage(five_g_1, lon_d, lat_d)
            count_d += count_couvrage(five_g_2, lon_d, lat_d)
            count_d += count_couvrage(five_g_3, lon_d, lat_d)
            e_d = count_d/lkm
            
            day = to_day_of_week(date)

            data_set.append([lon_s, lat_s, day, e_s])
            data_set.append([lon_d, lat_d, day, e_d])

    dsf = pd.DataFrame(data_set, columns=['Lon', 'Lat', 'Day', 'E'])

    dsf.to_csv("data.csv")

            # print(postal_codes[source_pc], postal_codes[destination_pc])

if __name__ == "__main__":
    postal_codes = load_postal_code("BAF_20211113.dat")
    build_data_set("/Users/oussama/Downloads/elisa_liikkuvuus_dataset.csv", postal_codes)
