import pandas as pd
from math import sin, cos, sqrt, atan2, radians


df = pd.read_excel("aeroportos.xlsx")


def getCordenadas(iata):
    iata = str(iata).upper()
    aeroporto = df[df['iata_code'] == iata]
    latitude = aeroporto['latitude_deg'].values[0]
    longitude = aeroporto['longitude_deg'].values[0]
    return [latitude, longitude]


def distance_haversine(cordenadas1, cordenadas2):
    lat1 = float(cordenadas1[0])
    lon1 = float(cordenadas1[1])

    lat2 = float(cordenadas2[0])
    lon2 = float(cordenadas2[1])

    R = 6371.0  # raio da Terra em quilômetros
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance  # em km


def distancia_aeroportos(iata1, iata2):
    coordenadas1 = getCordenadas(iata1)
    coordenadas2 = getCordenadas(iata2)

    distancia = distance_haversine(coordenadas1, coordenadas2)
    return distancia


print(distancia_aeroportos('ssa', 'gyn'))

