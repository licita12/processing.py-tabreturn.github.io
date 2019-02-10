size(800,800)
grid = loadImage('grid.png')
beziers = loadImage('beziers.png')
image(grid, 0, 0)
image(beziers, 0, 0)
noFill()
stroke('#FFFFFF')
strokeWeight(3)

# top-left

beginShape()
vertex(185,110)
bezierVertex(110,210, 340,240, 270,330)
endShape()

# top-right

beginShape()
vertex(466,120)
bezierVertex(458,280, 700,280, 650,125)
endShape()

# bottom-left

beginShape()
vertex(260,460)
bezierVertex(215,720, 65,460, 330,570)
endShape()

# bottom-right

beginShape()
vertex(490,625)
bezierVertex(580,740, 710,620, 600,520)
bezierVertex(490,410, 660,390, 680,505)
endShape()
