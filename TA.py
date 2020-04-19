import math as mx
import random


def pairDistance_Cities(coords):
    alldistanceGenerated = {}
    for i, (x1, y1) in enumerate(coords):
        for j, (x2, y2) in enumerate(coords):
            dx, dy = x1 - x2, y1 - y2
            dist = mx.sqrt(dx * dx + dy * dy)
            alldistanceGenerated[i, j] = dist
    return alldistanceGenerated


def total_Distance_Road(pair_distance, tour):
    total = 0
    num_cities = len(tour)
    for i in range(num_cities):
        j = (i + 1) % num_cities
        city_i = tour[i]
        city_j = tour[j]
        total += pair_distance[city_i, city_j]
    return total


def all_pairs(size, shuffle=random.shuffle):
    r1 = [*range(size)]
    r2 = [*range(size)]
    if shuffle:
        shuffle(r1)
        shuffle(r2)
    for i in r1:
        for j in r2:
            yield i, j


def generate_RandomRoutes(route):
    for i, j in all_pairs(len(route)):
        if i != j:
            randomRoute = route[:]
            if i < j:
                randomRoute[i:j + 1] = reversed(route[i:j + 1])
            else:
                randomRoute[i + 1:] = reversed(route[:j])
                randomRoute[:j] = reversed(route[i + 1:])
            if randomRoute != route:
                randomRoute.insert(0, 0)
                randomRoute += [0]
                yield randomRoute


def shuffle_FirstRoute(route_Size):
    route = [*range(1, route_Size)]
    random.shuffle(route)
    route.insert(0, 0)
    route.append(0)
    return route


def HillClimbing_Algorithm(first_Route, random_Routes, dataSolution_Route, maximum_Iteration):
    topRoute = first_Route
    best_score = dataSolution_Route(topRoute)
    count = 1
    while count < maximum_Iteration:
        move_made = False
        for childRoute in random_Routes(topRoute[1:len(topRoute) - 1]):
            if count >= maximum_Iteration:
                break
            child_Score = dataSolution_Route(childRoute)
            count += 1
            if child_Score > best_score:
                topRoute = childRoute
                best_score = child_Score
                move_made = True
                break

        if not move_made:
            break

    return count, best_score, topRoute


def read_coords():
    coord_file = open("infoCities.txt", "r")
    citiesName = []
    coords = []
    for line in coord_file:
        x = line.split("-")
        a = x[0]
        b = x[1]
        aux = b.strip().split(",")
        x = aux[0]
        y = aux[1]
        coords.append((float(x), float(y)))
        citiesName.append(a)
    return citiesName, coords


citiesName, coords = read_coords()

pair_distance = pairDistance_Cities(coords)
first_Route = shuffle_FirstRoute(len(coords))
print("Ruta generada: ")
print(first_Route)
for value in first_Route:
    print(citiesName[value])
dataSolution_Route = lambda tour: -total_Distance_Road(pair_distance, tour)
print("Distancia primera ruta generada: ")
print(abs(dataSolution_Route(first_Route)))
print("*****************************************************")
evaluations_count, total_Distance_OptimalRoute, optimalRoute = HillClimbing_Algorithm(first_Route, generate_RandomRoutes, dataSolution_Route, 20)
print("Distancia primera ruta generada: ")
print(abs(total_Distance_OptimalRoute))
print("Ruta generada: ")
print(optimalRoute)
for value in optimalRoute:
    print(citiesName[value])
