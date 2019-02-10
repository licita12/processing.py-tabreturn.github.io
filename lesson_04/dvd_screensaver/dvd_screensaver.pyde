x = 0
xspeed = 2
y = 0
yspeed = random(1,5)
logo = None

def setup():
    global logo
    size(800,600)
    logo = loadImage('dvd-logo.png')

def draw():
    global x, y, xspeed, yspeed
    background('#000000')
    '''
    fill(0x11000000)
    rect(-10,-10, width+20,height+20)
    '''
    x += xspeed
    y += yspeed
    image(logo, x,y)
    
    if y+45 > height:
        yspeed *= -1
    if x+100 > width:
        xspeed *= -1
    if y < 0:
        yspeed *= -1
    if x < 0:
        xspeed *= -1
