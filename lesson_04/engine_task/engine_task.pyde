ang = 0
inc = 0.1
rad = 20

def setup():
    size(800,400)
    noFill()
    strokeWeight(3)
    stroke('#FFFFFF')

def draw():
    global ang,inc
    '''
    rectMode(CORNER)
    fill(0x33004477)
    rect(-10,-10, width+20,height+20)
    noFill()
    '''
    background('#004477')
    rectMode(CENTER)
    ang += inc
    
    # cross section
    
    pushMatrix()
    translate(150, 200+sin(ang)*rad)
    rect(0,-30, 30,30)    # piston
    line(-15,-40, 15,-40) # ring upper
    line(-15,-35, 15,-35) # ring lower
    line(0,-30, 0,30)     # connecting rod
    popMatrix()

    pushMatrix()
    translate(200, 200+sin(ang-PI)*rad)
    rect(0,-30, 30,30)    # piston
    line(-15,-40, 15,-40) # ring upper
    line(-15,-35, 15,-35) # ring lower
    line(0,-30, 0,30)     # connecting rod
    popMatrix()
    
    pushMatrix()
    translate(250, 200+sin(ang-HALF_PI)*rad)
    rect(0,-30, 30,30)    # piston
    line(-15,-40, 15,-40) # ring upper
    line(-15,-35, 15,-35) # ring lower
    line(0,-30, 0,30)     # connecting rod
    popMatrix()

    # longitudinal section
    
    pushMatrix()
    translate(600, 200+sin(ang-HALF_PI)*rad)
    rect(0,-30, 30,30)    # piston
    line(-15,-40, 15,-40) # ring upper
    line(-15,-35, 15,-35) # ring lower
    popMatrix()
    
    pushMatrix()
    translate(600,230)
    ellipse(0,0, rad*2,rad*2)        # web
    sinval = sin(ang-HALF_PI)*rad
    cosval = cos(ang-HALF_PI)*rad
    line(cosval,sinval, 0,sinval-60) # connecting rod
    line(0,0, cosval,sinval)         # radius line
    popMatrix()
    
