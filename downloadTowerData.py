import numpy as np
from pandas import read_csv

#I had waffles for breakfast

def downloadTowerData(filename, latt_pos = 3, long_pos = 4):
    
    """
    Date:
        2/22/2021
    Purpose: 
        this function reads the csv file of tower locations and extracts the coordinates.
    inputs: 
        filename: filename as string or location and file name to get to csv file.
        latt_pos: the column in csv where lattitude data is stored.
        long_pos: the column in csv file where longitude data is stored.
    """
    
    data = np.array(read_csv(filename)).T
    lattitudes = data[latt_pos]
    longitudes = data[long_pos]

    x, y = np.array(lattitudes).astype(float), np.array(longitudes).astype(float)
    locations = np.array([x, y]).T
    return locations



    
# In[ ]: 

if __name__ == "__main__":

    # this is just an example so you can ignore it! it will not be uploaded when you do an import so no worries! 
    # this example plots the positions of the towers for the given csv file.
    import matplotlib.pyplot as plt
    
    positions = downloadTowerData('TowersRVN479554GVQ144174.csv', latt_pos = 3, long_pos = 4)
    x, y = positions.T
    plt.title('Towers')
    plt.plot(x, y, 'bo')
    plt.show()
        
    
