Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math
... 
... def calculate_distance_between_balloons(distance, altitude):
...     earth_radius = 6371 # радиус земли в км
...     distance += earth_radius # учитываем расстояние до центра Земли
...     altitude += earth_radius # учитываем высоту над уровнем моря
...     angle = 2 * math.asin(distance / (2 * (earth_radius + altitude))) # вычисляем угол в радианах
...     distance_between_balloons = 2 * (earth_radius + altitude) * math.sin(angle / 2) # вычисляем расстояние между шарами
...     return distance_between_balloons
... 
... # пример использования функции для расчета расстояния между шарами на расстоянии 1000 км друг от друга на высоте 5 км
... result = calculate_distance_between_balloons(1000, 5)
... print("Расстояние между шарами:", result, "км")
