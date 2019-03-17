def setup():
    size(400,300)
    frameRate(30)
    background('#004477')
    noStroke()
    ernest = createFont('Ernest.ttf', 30)
    textFont(ernest)
    textAlign(CENTER)

playerx = 195
playery = 145
xspeed = 0
yspeed = -2 #0
lastframe = 0

def draw():
    global currframe, lastframe
    currframe = millis()
    deltatime = currframe - lastframe
    print(deltatime)
    
    global playerx, playery, xspeed, yspeed
    playerx += xspeed
    #playery += yspeed
    playery += yspeed * (deltatime/30)

    fill(0x66004477)
    rect(0,0, width,height)

    fill('#FFFFFF')
    rect(playerx, playery, 10, 10)

    if playerx > width:
        playerx = 0
    if playerx < 0:
        playerx = width
    if playery < 0:
        playery = height
    if playery > height:
        playery = 0
        
    itemx = 300
    itemy = 60
    fill('#FF0000')
    rect(itemx, itemy, 10, 10) # red item

    if (
          playerx+10 >= itemx and playerx <= itemx+10
      and playery+10 >= itemy and playery <= itemy+10
       ):
        fill('#00FF00')
        text('hit!', 373,28)
    
    if playery > 145:
        fill('#00FF00')
        text(millis(), width/2,28)
        noLoop()
    
    for i in range(ceil(random( 900 ))):
        for j in range(i):
            atan(12345*i) * tan(67890*i)
    
    lastframe = currframe

def keyTyped():
    print(key)

def keyPressed():
    global xspeed, yspeed

    if key == 'w':
        yspeed = -4
    print(keyCode)

    if keyCode == UP:
        xspeed = 0
        yspeed = -4

    elif keyCode == DOWN:
        xspeed = 0
        yspeed = 4

    elif keyCode == LEFT:
        xspeed = -4
        yspeed = 0

    elif keyCode == RIGHT:
        xspeed = 4
        yspeed = 0
        
    if (
         key == BACKSPACE or key == DELETE
         or key == ENTER  or key == ESC
         or key == TAB    or key == RETURN
       ):
        print('you pressed:')
        print('backspace, delete, enter, esc, return, or tab')
        
