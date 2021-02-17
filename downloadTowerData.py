import random
#you need to pass it something for the argument, but it doesn't use whatever you pass it
def downloadTowerData(filename):
    N = 10
    i=0
    loc=[]
    while i < N:
        y = random.random()
        x = random.random()
        coord = [x,y]
        loc.append(coord)
        i=i+1
    return(loc)