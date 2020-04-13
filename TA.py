import pandas as pd
import networkx as nx
import math
import random


def calc_dist(city1, city2):
    return math.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)


class Route:
    cities = []

    def __init__(self, cities):
        self.cities = cities
        random.shuffle(cities)

    def changingRoute(self, cities):
        for index in cities:
            self.cities[index] = cities

    def getCities(self):
        return self.cities

    def swapCities(self, pos1, pos2):
        aux = self.cities[pos1]
        self.cities[pos1] = self.cities[pos2]
        self.cities[pos2] = self.cities[pos1]

    def getTotalDistance(self):
        citiesSize = len(self.cities)
        totalDistance = 0
        for index in citiesSize:
            if index < citiesSize - 1:
                totalDistance += calc_dist(self.cities[index], self.cities[index + 1])
        totalDistance += calc_dist(self.cities[citiesSize - 1], self.cities[0])
        return totalDistance


class HillClimbing:
    def findShortestRoute(self, route):
        iterationCounter = 0
        while iterationCounter < 100:
            adyacent = self.obtainAdjacentRoute(Route(route))
            if adyacent.getTotalDistance() <= route.getTotalDistance():
                route = Route(adyacent)
            else:
                iterationCounter += 1
        return route

    def obtainAdjacentRoute(self, route=Route()):
        x1, x2 = 0
        while x1 == x2:
            x1 = len(self.getCities()) * random.uniform(0, 1)
            x2 = len(self.getCities()) * random.uniform(0, 1)
        city1 = self.getCities()[x1]
        city2 = self.getCities()[x2]
        self.swapCities(city1, city2)
        return route


def data_Read():
    excel_file = 'ciudades.xlsx'
    data = pd.read_excel(excel_file)
    cities = list(data.set_index('CODIGO').values)
    print(cities)


data_Read()
