size(800, 800)
grid = loadImage('grid.png')
image(grid, 0, 0)
noFill()
stroke('#FFFFFF')
strokeWeight(3)

x = 400; y = 200
w = 200; h = 200

#rect(x, y, w, h)
quad(
  x, y,
  x, y+h, 
  x+w, y+h, 
  x+w, y
)

a = 100; b = -80
stroke('#FFFF00')
quad(
  x+a, y+b,
  x+a, y+h+b, 
  x+w+a, y+h+b, 
  x+w+a, y+b
)

grido = loadImage('grid-overlay.png')
#image(grido, 0,0, 800/2,800/2)

a = 0.3; b = 0
c = 0;   d = 1.8
stroke('#FF9900')
quad(
  x*a + y*b,         x*c + y*d, 
  x*a + (y+h)*b,     x*c + (y+h)*d, 
  (x+w)*a + (y+h)*b, (x+w)*c + (y+h)*d, 
  (x+w)*a + y*b,     (x+w)*c + y*d
)

a = -1; b = 0
c = 0;  d = 1
stroke('#FF0000')
quad(
  x*a + y*b,         x*c + y*d, 
  x*a + (y+h)*b,     x*c + (y+h)*d, 
  (x+w)*a + (y+h)*b, (x+w)*c + (y+h)*d, 
  (x+w)*a + y*b,     (x+w)*c + y*d
)
'''
pushMatrix()
rotate(0.785)
image(grido, 0,0)
popMatrix()
'''
a = cos(0.785); b = -sin(0.785)
c = sin(0.785); d = cos(0.785)
stroke('#FF99FF')
quad(
  x*a + y*b,         x*c + y*d, 
  x*a + (y+h)*b,     x*c + (y+h)*d, 
  (x+w)*a + (y+h)*b, (x+w)*c + (y+h)*d, 
  (x+w)*a + y*b,     (x+w)*c + y*d
)
'''
pushMatrix()
shearY(0.381)
image(grido, 0,0)
popMatrix()
'''
a = 1;   b = 0
c = 0.4; d = 1
stroke('#FF0000')
quad(
  a*x + b*y,         c*x + d*y, 
  a*x + b*(y+h),     c*x + d*(y+h), 
  a*(x+w) + b*(y+h), c*(x+w) + d*(y+h), 
  a*(x+w) + b*y,     c*(x+w) + d*y
)
