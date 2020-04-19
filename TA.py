import math as mx
import random


def pairDistance_Cities(coords):
    matrix = {}
    for i, (x1, y1) in enumerate(coords):
        for j, (x2, y2) in enumerate(coords):
            dx, dy = x1 - x2, y1 - y2
            dist = mx.sqrt(dx * dx + dy * dy)
            matrix[i, j] = dist
    return matrix


def total_Distance_Road(all_distance_generated, tour):
    total = 0
    num_cities = len(tour)
    for i in range(num_cities):
        j = (i + 1) % num_cities
        city_i = tour[i]
        city_j = tour[j]
        total += all_distance_generated[city_i, city_j]
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


def HillClimbing_Algorithm(init_function, move_operator, objective_function, max_evaluations):
    best = init_function
    best_score = objective_function(best)

    evaluations_count = 1

    while evaluations_count < max_evaluations:
        move_made = False
        for next in move_operator(best[1:len(best) - 1]):
            if evaluations_count >= max_evaluations:
                break

            next_score = objective_function(next)
            evaluations_count += 1
            if next_score > best_score:
                best = next
                best_score = next_score
                move_made = True
                break

        if not move_made:
            break

    return evaluations_count, best_score, best


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

all_distance_generated = pairDistance_Cities(coords)
first_Route = shuffle_FirstRoute(len(coords))
print("Ruta generada: ")
print(first_Route)
for value in first_Route:
    print(citiesName[value])
dataSolution_Route = lambda tour: -total_Distance_Road(all_distance_generated, tour)
print("Distancia primera ruta generada: ")
print(dataSolution_Route(first_Route))
print("*****************************************************")
evaluations_count, total_Distance_OptimalRoute, optimalRoute = HillClimbing_Algorithm(first_Route, generate_RandomRoutes, dataSolution_Route, 20)
print("Distancia primera ruta generada: ")
print(total_Distance_OptimalRoute)
print("Ruta generada: ")
print(optimalRoute)
for value in optimalRoute:
    print(citiesName[value])
