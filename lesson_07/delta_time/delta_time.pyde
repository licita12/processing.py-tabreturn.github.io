# This sketch makes use of the font:
# "Ernest" (https://www.dafont.com/ernest.font)
# by Marc Andre "mieps" Misman

fps = 30

def setup():
    size(200,100)
    strokeCap(PROJECT)
    frameRate(fps)
    background('#004477')
    ernest = createFont('Ernest.ttf', 30)
    textFont(ernest)

currframe = 0
lastframe = millis()
x = 0    

def draw():
    global currframe, lastframe, x
    currframe = millis()
    deltatime = (currframe-lastframe) / 1000.0 * fps
    #print(deltatime)
    
    stroke('#0099FF')
    line(x,0, x,height)
    x += 1 * deltatime
    
    if x > width:
        textAlign(CENTER)
        text(millis(), width/2,58)
        noLoop()
    
    for i in range( ceil(random(2000)) ):
        for j in range(i):
            atan(12345*i) * tan(67890*i)
    
    lastframe = currframe
    
def keyPressed():
    stroke('#FF0000')
    x = millis()/8000.0*width
    line(x,0, x,height)
    
    
    
