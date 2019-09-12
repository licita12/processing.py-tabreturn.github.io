# https://en.wikipedia.org/wiki/Parametric_equation

def setup():
    size(800,800)
    background('#004477')
    strokeWeight(3)

def porabola(x):
    return x*x

def circle(t):
    x = cos(t)
    y = sin(t)
    return [x,y]

def ellips(t):
    x = 2 * cos(t)
    y = 1 * sin(t)
    return [x,y]

def lissajous(t,A,B,a,b):
    # ratio of a/b determines curve
    # so a=2,b=1 same as a=10,b=5
    x = A * cos(a*t)
    y = B * sin(b*t)
    return [x,y]

x = -300.0
y = 0.0
t = 0.0

def draw():
    global x,y,t
    t += 0.01
    
    translate(width/2, height/2)
    stroke('#0099FF')
    line(width/2*-1,0,  width/2,0)
    line(0,height/2*-1, 0,height/2)
    stroke('#FFFFFF')
    
    '''
    y = porabola(x)
    x += 1
    point(x,y)
    '''
    '''
    xy = circle(t)
    x = xy[0] * 100
    y = xy[1] * 100
    point(x,y)
    '''
    '''
    xy = ellips(t)
    x = xy[0] * 100
    y = xy[1] * 100
    point(x,y)
    '''
    '''
    xy = lissajous(t,1,1,3,2)
    x = xy[0] * 100
    y = xy[1] * 100
    t += 0.01
    point(x,y)
    '''

    # windows mystify screensaver
    xy1 = lissajous(t,2,1,3,1)
    x1 = xy1[0] * 100
    y1 = xy1[1] * 100
    xy2 = lissajous(t,1,5,5,3)
    x2 = xy2[0] * 100
    y2 = xy2[1] * 100
    xy3 = lissajous(t,7,3,1,1)
    x3 = xy3[0] * 100
    y3 = xy3[1] * 100
    
    fill(0x66004477)
    rect(-width/2,-height/2, width,height)
    colorMode(HSB,360,100,100)
    stroke(x,100,100)
    x += 1
    if x > 360: 
        x = 0
        
    line(x1,y1, x2,y2)
    line(x2,y2, x3,y3)
    line(x3,y3, x1,y1)
