import random

mappyboo=[]
validtiles=[',','t','r','H','#' ]
# , is grass, t is tree, r is rock, # is path, H  is house
def genmap():
    global mappyboo
    for _ in range(100):
        mappyboo.append(',')
        print('\n')


    
def printmap():
    global mappyboo
    for i in range(0, len(mappyboo), 10):
        print(''.join(mappyboo[i:i+10]))
genmap()
printmap()