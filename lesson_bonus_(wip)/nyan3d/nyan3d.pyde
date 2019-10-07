# https://en.wikipedia.org/wiki/3D_projection#Perspective_projection

def setup():
    size(600,600)
    noFill()
    strokeWeight(3)

a1 = [ 0.0,   0.0,   50.0 ] # the 3D position of a point A that is to be projected
a2 = [ 0.0,   100.0, 50.0 ]
a3 = [ 100.0, 100.0, 50.0 ]
a4 = [ 100.0, 0.0,   50.0 ]
a5 = [ 50.0,  50.0,  125.0]

c =  [ 0.0,  0.0,  200.0 ]  # the 3D position of a point C representing the camera
e =  [ 0.0,   0.0, 140.0 ]  # the display surface's position relative to the camera pinhole C

t = 0.02 # z rotation


def project(a,c,e):
    d = [ a[0] - c[0], a[1] - c[1], a[2] - c[2] ]
    b = [ (e[2]/d[2]*d[0]) + e[0], (e[2]/d[2]*d[1]) + e[1] ]
    return [ b[0], b[1] ]


def rotatex(a, t):
    # DO THESE WITH A MATRIX INSTEAD
    a = [
      a[0],
      a[1]*cos(t) - a[2]*sin(t),
      a[1]*sin(t) + a[2]*cos(t)
    ]
    return a 
    
def rotatey(a, t):
    a = [
      a[2]*sin(t) + a[0]*cos(t),
      a[1],
      a[2]*cos(t) - a[0]*sin(t)
    ]
    return a

def rotatez(a, t):
    a = [
      a[0]*cos(t) - a[1]*sin(t),
      a[0]*sin(t) + a[1]*cos(t),
      a[2]
    ]
    return a

def draw():

    background('#FFFFFF')
    
    global a1,a2,a3,a4,a5
    
    stroke('#FF0000')
    pushMatrix()
    translate(100, 100)
    point(a1[0], a1[1])
    point(a2[0], a2[1])
    point(a3[0], a3[1])
    point(a4[0], a4[1])
    # cap
    line(a5[0],a5[1], a1[0],a1[1])
    line(a5[0],a5[1], a2[0],a2[1])
    line(a5[0],a5[1], a3[0],a3[1])
    line(a5[0],a5[1], a4[0],a4[1])
    # base
    line(a1[0],a1[1], a2[0],a2[1])
    line(a2[0],a2[1], a3[0],a3[1])
    line(a3[0],a3[1], a4[0],a4[1])
    line(a4[0],a4[1], a1[0],a1[1])
    popMatrix()
    
    stroke('#0000FF')
    pushMatrix()
    translate(width-100, height-100)
    p1 = project(a1,c,e)
    p2 = project(a2,c,e)
    p3 = project(a3,c,e)
    p4 = project(a4,c,e)
    p5 = project(a5,c,e)
    point( p1[0], p1[1])
    point( p2[0], p2[1])
    point( p3[0], p3[1])
    point( p4[0], p4[1])
    point( p5[0], p5[1])
    # cap
    line(p5[0],p5[1], p1[0],p1[1])
    line(p5[0],p5[1], p2[0],p2[1])
    line(p5[0],p5[1], p3[0],p3[1])
    line(p5[0],p5[1], p4[0],p4[1])
    # base
    line(p1[0],p1[1], p2[0],p2[1])
    line(p2[0],p2[1], p3[0],p3[1])
    line(p3[0],p3[1], p4[0],p4[1])
    line(p4[0],p4[1], p1[0],p1[1])
    popMatrix()

    a1 = rotatex(a1, t)
    a2 = rotatex(a2, t)
    a3 = rotatex(a3, t)
    a4 = rotatex(a4, t)
    a5 = rotatex(a5, t)
    a1 = rotatey(a1, t)
    a2 = rotatey(a2, t)
    a3 = rotatey(a3, t)
    a4 = rotatey(a4, t)
    a5 = rotatey(a5, t)
    a1 = rotatez(a1, t)
    a2 = rotatez(a2, t)
    a3 = rotatez(a3, t)
    a4 = rotatez(a4, t)
    a5 = rotatez(a5, t)

# CHALLENGE: fill in facets (use the z-coord to determine which side is foremost)
