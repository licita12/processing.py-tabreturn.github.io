size(800,800)
grid = loadImage('grid.png')
image(grid, 0, 0)


# guides (for screenshot)
strokeWeight(2)
stroke('#0099FF')
fill('#0099FF')

line(400,200, 300,300)
ellipse(300,300, 8,8)
line(400,600, 500,500)
ellipse(500,500, 8,8)

line(600,400, 420,300)
ellipse(420,300, 8,8)
line(600,250, 550,150)
ellipse(550,150, 8,8)

line(600,250, 650,150)
ellipse(650,150, 8,8)
line(600,400, 780,300)
ellipse(780,300, 8,8)

noFill()
stroke('#FFFFFF')
strokeWeight(3)

beginShape()
vertex(100,100)
vertex(200,100)
vertex(200,200)
vertex(100,200)
endShape()

beginShape()
vertex(400,200) # starting (upper) anchor point
bezierVertex(
  300,300, # control point for the starting anchor point
  500,500, # control point for the second (lower) anchor point
  400,600  # second (lower) anchor point coordinates
)
endShape()

beginShape()
vertex(600,400)
bezierVertex(420,300, 550,150, 600,250)
bezierVertex(650,150, 780,300, 600,400)
endShape()
'''
beginShape()
vertex(100,600)
vertex(200,500)
vertex(300,600)
vertex(200,700)
vertex(100,600)
endShape()
'''
fill('#6633FF')
beginShape()
vertex(100,600)
bezierVertex(100,545, 145,500, 200,500)
bezierVertex(255,500, 300,545, 300,600)
bezierVertex(300,655, 255,700, 200,700)
bezierVertex(145,700, 100,655, 100,600)
beginContour()
vertex(180,580)
vertex(180,620)
vertex(220,620)
vertex(220,580)
endContour()
endShape()
