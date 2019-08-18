# build a (very basic) 3d engine? numpy could be useful for matrices?
# https://en.wikipedia.org/wiki/3D_projection
# https://www.scratchapixel.com/lessons/3d-basic-rendering/computing-pixel-coordinates-of-3d-point/mathematics-computing-2d-coordinates-of-3d-points

def setup():
    size(600,600, P3D)
    global img
    img = loadImage('rainbow.gif')

r = 0

def draw():
    global r
    
    background('#004477')
    stroke('#FFFFFF')
    strokeWeight(3)
    fill('#FF0000')
    translate(width/2, height/2, 400)
    rotateX(r)
    #rotateY(r)
    #rotateZ(r)
    noFill()

    
    fill('#00FF00')
    rect(0,0,100,100)
    
    pushMatrix()
    translate(40,0)
    sphere(20)
    popMatrix()
    
    pushMatrix()
    translate(0,0,5)
    scale(0.2,0.2,0.2)
    beginShape()
    texture(img)
    textureWrap(CLAMP)
    vertex(-100, -100, -100, -100)
    vertex( 100, -100, -100, -100)
    vertex(   0,    0,  100)
    '''
    vertex( 100, -100, -100)
    vertex( 100,  100, -100)
    vertex(   0,    0,  100)

    vertex( 100, 100, -100)
    vertex(-100, 100, -100)
    vertex(   0,   0,  100)

    vertex(-100,  100, -100)
    vertex(-100, -100, -100)
    vertex(   0,    0,  100)
    '''
    endShape()
    popMatrix()
    
    beginShape()
    vertex(-100, -100, -100)
    vertex( 100, -100, -100)
    vertex(   0,    0,  100)

    vertex( 100, -100, -100)
    vertex( 100,  100, -100)
    vertex(   0,    0,  100)

    vertex( 100, 100, -100)
    vertex(-100, 100, -100)
    vertex(   0,   0,  100)

    vertex(-100,  100, -100)
    vertex(-100, -100, -100)
    vertex(   0,    0,  100)
    endShape()

    
    noFill()
    box(40)
    r += 0.01
    
