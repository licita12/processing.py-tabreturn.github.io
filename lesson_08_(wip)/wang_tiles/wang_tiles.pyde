# https://en.wikipedia.org/wiki/Wang_tile#/media/File:Wang_11_tiles.svg
# https://py.processing.org/reference/get.html
# https://py.processing.org/reference/hex.html

size(800,800)
background('#004477')

r = '#FF0000'
g = '#00FF00'
b = '#0099FF'
y = '#FFFF00'
empty = '#000000'

tiles = [
 ['00.gif',r,b,r,b],
 ['01.gif',r,b,r,y],
 ['02.gif',r,b,g,b],
 ['03.gif',r,b,g,y],
 ['04.gif',r,y,r,b],
 ['05.gif',r,y,r,y],
 ['06.gif',r,y,g,b],
 ['07.gif',r,y,g,y],
 ['08.gif',g,b,r,b],
 ['09.gif',g,b,r,y],
 ['10.gif',g,b,g,b],
 ['11.gif',g,b,g,y],
 ['12.gif',g,y,r,b],
 ['13.gif',g,y,r,y],
 ['14.gif',g,y,g,b],
 ['15.gif',g,y,g,y]
]

def getNeighbors(x, y, tilesize):
    s = tilesize
    north = get(x*s+s/2, y*s-2)
    north = '#' + hex(north, 6)
    west = get(x*s-2, y*s+s/2)
    west = '#' + hex(west, 6)
    return [north, west]

def placeTile(x, y, tilesize, tileimage):
    img = loadImage(tileimage)
    image(img, x*tilesize, y*tilesize, tilesize, tilesize)

def selectMatches(north, west):
    matches = []
    
    if north == empty and west == empty:
        matches = tiles
    else:
        for i in tiles:
            if north == empty and west == i[4]:
                matches.append(i)
            elif north == i[1] and west == empty:
                matches.append(i)
            elif north == i[1] and west == i[4]:
                matches.append(i)
    
    return matches

def selectRandom(imagearray):
    randomindex = int(random(len(imagearray)))
    return imagearray[randomindex]

col = 0
row = 0
wh = 40 # tile width and height
total = width/wh * width/wh

for i in range(1, total+1):
    neighbors = getNeighbors(col, row, wh)
    matches = selectMatches(neighbors[0], neighbors[1])
    tile = selectRandom(matches)
    tileimage = tile[0]
    placeTile(col, row, wh, tileimage)

    if i%(width/wh) == 0:
        row += 1
        col = 0
    else:
        col += 1
