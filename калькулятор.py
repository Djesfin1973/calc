import math

def distance(lat1, lon1, lat2, lon2):
    R = 6371  # Радиус Земли в километрах
    dLat = math.radians(lat2-lat1)
    dLon = math.radians(lon2-lon1)
    a = math.sin(dLat/2) * math.sin(dLat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dLon/2) * math.sin(dLon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    dist = R * c  # Расстояние в километрах
    return dist

def elevation(lat1, lon1, lat2, lon2):
    dist = distance(lat1, lon1, lat2, lon2)
    h1 = 0  # Высота над уровнем моря первой точки
    h2 = 0  # Высота над уровнем моря второй точки
    # Здесь нужно получить данные о высотах точек с помощью какого-либо API или другого источника данных
    ele = abs(h2 - h1)  # Высота разницы между точками
    return ele

def line_of_sight(lat1, lon1, h1, lat2, lon2, h2):
    R = 6371  # Радиус Земли в километрах
    earth_radius = 6371.01  # Радиус Земли с поправкой на геоид
    d = distance(lat1, lon1, lat2, lon2)
    a = math.acos((R+h1) / (R+h2))
    b = math.acos((R+h1) / (R+h2))
    c = math.acos(math.cos(a) * math.cos(b) + math.sin(a) * math.sin(b) * math.cos(d/earth_radius))
    los_distance = R * c  # Расстояние прямой видимости в километрах
    return los_distance
