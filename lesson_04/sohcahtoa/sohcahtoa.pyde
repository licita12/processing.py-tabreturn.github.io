theta = QUARTER_PI
radius = 1
s = 200 # scale variable

def setup():
    size(600,600)
    noFill()
    stroke('#FFFFFF')
    strokeWeight(3)

def draw():
    global theta
    '''
    fill(0x33004477)
    rect(-10,-10, width+20,height+20)
    '''
    background('#004477')
    translate(width/2, height/2)
    diameter = radius*s*2
    ellipse(0,0, diameter,diameter)
    x = cos(theta)
    y = sin(theta)
    print(
      round(x,1),
      round(y,1)
    )
    line(0, 0, x*s, y*s*-1)
    # sine motion
    ellipse(-width/2+40, y*s*-1, 10, 10)
    # cosine motion
    ellipse(x*s, -height/2+40, 10, 10)
    # sine & cosine motion
    ellipse(x*s, y*s*-1, 10, 10)
    theta += 0.05
    
    # xeyes
    '''
    atan2 returns a float between π and -π
            π
            |
    -π/2 ---+--- π/2
            |
            0
    '''
    # left eye
    leftx = 180
    lefty = 255
    leftr = atan2(
      y*s*-1 + lefty*-1, 
      x*s + leftx*-1
    )
    pushMatrix()
    translate(leftx,lefty)
    rotate(leftr)
    ellipse(0,0, 40,40)
    ellipse(8,0, 10,10)
    popMatrix()
    
    # right eye
    rightx = 250
    righty = 255
    rightr = atan2(
      y*s*-1 + righty*-1, 
      x*s + rightx*-1
    )
    pushMatrix()
    translate(rightx,righty)
    rotate(rightr)
    ellipse(0,0, 40,40)
    ellipse(8,0, 10,10)
    popMatrix()
    
    # hypotenuse
    stroke('#0099FF')
    ydiff = y*s*-1 + righty*-1
    xdiff = x*s + rightx*-1
    line(
      rightx, righty,
      rightx+xdiff, righty+ydiff
    )
    stroke('#FFFFFF')
    
