size(800,850)
background('#004477')

grid = loadImage('grid.png')
image(grid, 0, 0)
logo = loadImage('apple.png')
image(logo, 0, 0)

# bands

noStroke()
band_height = 99
fill('#61BB46')
rect(0,190, width,band_height)
fill('#FDB827')
rect(0,190+band_height*1, width,band_height)
fill('#F5821F')
rect(0,190+band_height*2, width,band_height)
fill('#E03A3E')
rect(0,190+band_height*3, width,band_height)
fill('#963D97')
rect(0,190+band_height*4, width,band_height)
fill('#009ddc')
rect(0,190+band_height*5, width,band_height+10)

# apple

x1  = 400;  x2  = 185;  x3  = 58 ;  x4  = 260;  x5  = 400
y1  = 752;  y2  = 745;  y3  = 480;  y4  = 190;  y5  = 225
x1i = None; x2i = 280;  x3i = 65 ;  x4i = 160;  x5i = 330
y1i = None; y2i = 830;  y3i = 560;  y4i = 190;  y5i = 225
x1o = 320;  x2o = 115;  x3o = 40 ;  x4o = 320;  x5o = None
y1o = 752;  y2o = 682;  y3o = 265;  y4o = 190;  y5o = None

fill('#FFFFFF')
beginShape()
vertex(0,0)
vertex(0,height)
vertex(width,height)
vertex(width,0)
beginContour()
vertex(x1,y1)
bezierVertex(x1o,y1o, x2i,y2i, x2,y2)
bezierVertex(x2o,y2o, x3i,y3i, x3,y3)
bezierVertex(x3o,y3o, x4i,y4i, x4,y4)
bezierVertex(x4o,y4o, x5i,y5i, x5,y5)
bezierVertex(width-x5i,y5i, width-x4o,y4o, width-x4,y4)
bezierVertex(width-x4i,y4i, width-x3o,y3o, width-x3,y3)
bezierVertex(width-x3i,y3i, width-x2o,y2o, width-x2,y2)
bezierVertex(width-x2i,y2i, width-x1o,y1o, width-x1,y1)
endContour()
endShape()

ellipse(772,420, 328,335)

# apple guidelines
'''
stroke('#0099FF')
strokeWeight(3)
noFill()

beginShape()
vertex(x1,y1)
bezierVertex(x1o,y1o, x2i,y2i, x2,y2)
bezierVertex(x2o,y2o, x3i,y3i, x3,y3)
bezierVertex(x3o,y3o, x4i,y4i, x4,y4)
bezierVertex(x4o,y4o, x5i,y5i, x5,y5)
bezierVertex(width-x5i,y5i, width-x4o,y4o, width-x4,y4)
bezierVertex(width-x4i,y4i, width-x3o,y3o, width-x3,y3)
bezierVertex(width-x3i,y3i, width-x2o,y2o, width-x2,y2)
bezierVertex(width-x2i,y2i, width-x1o,y1o, width-x1,y1)
endShape()

ellipse(772,420, 328,335)

line(x1,y1, x1o,y1o)
line(x2,y2, x2i,y2i); line(x2,y2, x2o,y2o)
line(x3,y3, x3i,y3i); line(x3,y3, x3o,y3o)
line(x4,y4, x4i,y4i); line(x4,y4, x4o,y4o)
line(x5,y5, x5i,y5i)
line(width-x1,y1, width-x1o,y1o)
line(width-x2,y2, width-x2i,y2i); line(width-x2,y2, width-x2o,y2o)
line(width-x3,y3, width-x3i,y3i); line(width-x3,y3, width-x3o,y3o)
line(width-x4,y4, width-x4i,y4i); line(width-x4,y4, width-x4o,y4o)
line(width-x5,y5, width-x5i,y5i)

fill('#0099FF')
rectMode(CENTER)
rect(x1,y1 ,5,5); rect(width-x1,y1 ,5,5)
rect(x2,y2 ,5,5); rect(width-x2,y2 ,5,5)
rect(x3,y3 ,5,5); rect(width-x3,y3 ,5,5)
rect(x4,y4 ,5,5); rect(width-x4,y4 ,5,5)
rect(x5,y5 ,5,5); rect(width-x5,y5 ,5,5)
ellipse(x1o,y1o ,8,8); ellipse(width-x1o,y1o ,8,8)
ellipse(x2i,y2i ,8,8); ellipse(width-x2i,y2i ,8,8)
ellipse(x2o,y2o ,8,8); ellipse(width-x2o,y2o ,8,8)
ellipse(x3i,y3i ,8,8); ellipse(width-x3i,y3i ,8,8)
ellipse(x3o,y3o ,8,8); ellipse(width-x3o,y3o ,8,8)
ellipse(x4i,y4i ,8,8); ellipse(width-x4i,y4i ,8,8)
ellipse(x4o,y4o ,8,8); ellipse(width-x4o,y4o ,8,8)
ellipse(x5i,y5i ,8,8); ellipse(width-x5i,y5i ,8,8)
'''
# leaf

x1  = 375; x2  = 533
y1  = 200; y2  = 10
x1i = 478; x2i = 430
y1i = 185; y2i = 25
x1o = 370; x2o = 538
y1o =  95; y2o = 115

fill('#61BB46')
beginShape()
vertex(x1,y1)
bezierVertex(x1o,y1o, x2i,y2i, x2,y2)
bezierVertex(x2o,y2o, x1i,y1i, x1,y1)
endShape()

# leaf guidelines
'''
stroke('#0099FF')
strokeWeight(3)
noFill()

beginShape()
vertex(x1,y1)
bezierVertex(x1o,y1o, x2i,y2i, x2,y2)
bezierVertex(x2o,y2o, x1i,y1i, x1,y1)
endShape()

line(x1,y1, x1o,y1o)
line(x2,y2, x2i,y2i)
line(x2,y2, x2o,y2o)
line(x1,y1, x1i,y1i)

fill('#0099FF')
rectMode(CENTER)
rect(x1,y1 ,5,5)
rect(x2,y2 ,5,5)
ellipse(x1i,y1i ,8,8)
ellipse(x1o,y1o ,8,8)
ellipse(x2i,y2i ,8,8)
ellipse(x2o,y2o ,8,8)
'''
# registered trademark

noFill()
stroke('#000000')
strokeWeight(5.5)
ellipse(715,748, 70,70)

fill('#000000')
textSize(58)
text('R', 698,769)
