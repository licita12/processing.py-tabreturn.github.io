y = 1

def setup():
    size(500,500)
    noFill()
    stroke('#FFFFFF')
    strokeWeight(3)

def draw():
    global y
    background('#004477')
    '''
    fill(0x11004477)
    rect(0-10,0-10, width+20,height+20)
    noFill()
    '''
    y += 1
    print(y)
    ellipse(height/2,y, 47,47)
    
    '''
    if frameCount % 100 == 0:
        saveFrame()
