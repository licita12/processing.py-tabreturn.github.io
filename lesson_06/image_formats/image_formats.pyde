size(100,100)
background('#FFFFFF')
noStroke()
fill('#FF0000')

for i in range(0,height,10):
    rect(0,i, width,5)

saveFrame('bands') # tiff
saveFrame('bands.gif')
saveFrame('bands.jpg')
saveFrame('bands.png')
saveFrame('bands.tga')
