# -*- coding: utf-8 -*-


def kNN(points, k = 1):
    """
    By: Group 2 for CMSE 802 
    Date: 2/17/21
    Function: Calculate k-NN graph.
    """
    import numpy as np
    import networkx as nx
    from sklearn.neighbors import NearestNeighbors
    
    points = np.array(points) #change to numpy array
    
    # get shape of vectors of positions and do shape check to validate it is correct shape.
    row, col = points.shape[0], points.shape[1]
    if col != 2: #should be (N x 2) array
        points = points.T
    N = points.shape[0]

    G = nx.Graph() #intiialize graph
    G.add_nodes_from(list(range(N))) #add all vertices to graph
    
    #find distances and indices of points that are k-NN using sklearn package
    nbrs = NearestNeighbors(n_neighbors=k+1, algorithm='ball_tree').fit(points)
    distances, indices = nbrs.kneighbors(points)
    
    #add all edges to graph based on k nearest neighbor condition
    for edge_set in indices: #go through list of nearest neighbors for point
        for index_of_vertex in edge_set[1:]: #go through those neighbors (skipping self as first)
            edge = [edge_set[0], index_of_vertex] #define the edge
            G.add_edge(edge[0], edge[1]) #add the edge
    
    return G


    
# In[ ]: 


if __name__ == "__main__":

    
    import numpy as np
    import networkx as nx
    import matplotlib.pyplot as plt
        


    def generate_towers(N):
        import numpy as np
        x = np.random.uniform(0, 1, N)
        y = np.random.uniform(0, 1, N)
        points = np.array([x,y]).T
        return points 

    points = generate_towers(50)
    
    G = kNN(points, k = 5)
    
    node_pos = {}
    for v in G.nodes():
        node_pos[v] = points[v,:]
    
    fig, ax = plt.subplots()
    nx.draw(G,node_pos, node_size = 20)
    limits = plt.axis('on')
    ax.tick_params(left = True, bottom = True,labelleft=True, labelbottom=True)
    plt.show()
    

