def setup():
    size(300,138)
    frameRate(12)

def draw(): 
    background('#004477')
    nyan = loadImage('nyancat-spritesheet.gif')
    xpos = (frameCount % 5) * 300 * -1
    image(nyan, xpos,0)
    
