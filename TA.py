import pandas as pd
import networkx as nx
import math

def lee_datos(G,origen):
    archivo = pd.ExcelFile('ciudades.xlsx')
    linea = pd.read_excel(archivo)
    ciudades = list(linea.set_index('CODIGO').values)

    genera_grafo(ciudades,origen,G)

def calc_dist(partida,llegada):
    return math.sqrt((llegada[1]-partida[1])**2 + (llegada[2]-partida[2])**2)

def genera_grafo(ciudades,origen,grafo):
    ciud_completa = []
    
    for partida in ciudades: 
        for llegada in ciudades:
            ciud = [] 
            if partida[0] != llegada[0]:
                ciud.append(partida[0])
                ciud.append(llegada[0])
                dist = calc_dist(partida,llegada)
                ciud.append(dist)
                ciud_completa.append(ciud)
         
g = nx.Graph()
origen = input("Ingrese la ciudad de origen: ")
lee_datos(g,origen)