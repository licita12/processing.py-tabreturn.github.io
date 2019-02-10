size(800,800)
noFill()
stroke('#FFFFFF')
strokeWeight(3)
grid = loadImage('grid.png')
image(grid, 0, 0)
grido = loadImage('grid-overlay.png')

x = 400; y = 200
w = 200; h = 200
rect(x,y, w,h)

pushMatrix()
translate(100,-80)
rotate(0.785)
shearY(0.4)
image(grido, 0,0)
stroke('#FFFF00')
rect(x,y, w,h)
popMatrix()

stroke('#FF0000')
rect(0,0, 100,100)

'''
pushMatrix()
translate(100, -80)
scale(1, 0.5)
rotate(0.785)
shearX(0.2)
shearY(0.4)
image(grid, 0, 0)
rect(x, y, w, h)
popMatrix()

rect(x+10, y+10, w, h)
