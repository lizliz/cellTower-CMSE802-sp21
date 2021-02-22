
# coding: utf-8

# In[ ]:


##----Group 3------# old code
#import numpy as np
#from random import randrange
##Colouring Stub function
#def GreedyGraphColoring(graph, M):
#    #take an empty array
#    #for each node in graph, randomly assign a color 
#    #color is integer in our case    
#    colour_map = []
#    for node in graph:
#        colour_map.append(np.random.randint(0,M))
#                          
#    return colour_map
  



from random import randrange
import numpy as np
import networkx as nx
#Colouring Stub function
def GreedyGraphColoring(graph, M=3):

    G = graph
    #d = nx.coloring.equitable_color(G, num_colors=M)
    #s = nx.algorithms.coloring.equitable_coloring.is_equitable(G, d)
    #s = nx.greedy_color(G, num_colors=M)
    colour_map = nx.greedy_color(graph, strategy='largest_first', interchange=False)
    data = list(colour_map.items())
    an_array = np.array(data)
    colour_map = an_array[:,1]
                          
    return colour_map

