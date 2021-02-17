
#----Group 3------#
import numpy as np
from random import randrange
#Colouring Stub function
def GreedyGraphColoring(graph, M):
    #take an empty array
    #for each node in graph, randomly assign a color  
    colour_map = []
    for node in graph:
        colour_map.append(np.random.uniform(0,M))
                          
    return colour_map
    