import pandas as pd
import networkx as nx
import math
import random


def calc_dist(city1, city2):
    return math.sqrt((city2[1] - city1[1]) ** 2 + (city2[2] - city1[2]) ** 2)


class Route:
    cities = []

    def __init__(self, cities):
        self.cities = cities
        listAux = cities[1:len(cities)]
        random.shuffle(listAux)
        cities[1:len(cities)] = listAux[0:len(cities)]

    def changingRoute(self, citiesNew):
        for index in range(len(citiesNew)):
            self.cities[index] = citiesNew[index]

    def getCities(self):
        return self.cities

    def swapCities(self, pos1, pos2):
        aux = self.cities[pos1]
        self.cities[pos1] = self.cities[pos2]
        self.cities[pos2] = aux

    def getTotalDistance(self):
        citiesSize = len(self.cities)
        totalDistance = 0
        for index in range(citiesSize):
            if index < citiesSize - 1:
                totalDistance += calc_dist(self.cities[index], self.cities[index + 1])
        totalDistance += calc_dist(self.cities[citiesSize - 1], self.cities[0])
        return totalDistance


def obtainAdjacentRoute(route):
    x1 = 0
    x2 = 0
    while x1 == x2:
        x1 = int(len(route.getCities()) * random.uniform(0, 1))
        x2 = int(len(route.getCities()) * random.uniform(0, 1))
        if x1 == 0 or x2 == 0:
            x1 = 0
            x2 = 0
    route.swapCities(x1, x2)
    return route


def findShortestRoute(route):
    iterationCounter = 0
    while iterationCounter < 2:
        adyacent = obtainAdjacentRoute(Route(data_Read()))
        print(adyacent.getTotalDistance())
        print(route.getTotalDistance())
        if adyacent.getTotalDistance() <= route.getTotalDistance():
            iterationCounter = 0
            print(route.getCities())
            print(adyacent.getCities())
            route.changingRoute(adyacent.getCities())
            print(route.getCities())
        else:
            iterationCounter += 1
        print(route.getCities())
        print(route.getTotalDistance())
    return route


def data_Read():
    excel_file = 'ciudades.xlsx'
    data = pd.read_excel(excel_file)
    cities = list(data.set_index('CODIGO').values)

    return cities


data_Read()
route = Route(data_Read())
routeaux = Route(data_Read())
route2 = obtainAdjacentRoute(routeaux)
findShortestRoute(route)
