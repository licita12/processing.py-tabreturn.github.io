# https://en.wikipedia.org/wiki/Finder_(software)

size(300,300)
background('#004477')
strokeCap(PROJECT)

def face(x,y,gap):
    
    # right half
    fill('#0099FF')
    noStroke()
    rect(x,0, width,y)
    rect(x+gap,0, width,height)
    
    # center line
    stroke('#000000')
    strokeWeight(9)
    line(x,0, x,y)
    line(x,y, x+gap,y)
    line(x+gap,y, x+gap,width)
    
    # mouth
    mouthy = height-(height-y)/2
    line(x,mouthy, x+gap*2,mouthy)
    
    # eyes
    line(x-gap/2,y/2, x-gap/2,y/2-10)
    line(x+gap/2,y/2, x+gap/2,y/2-10)

face( random(50,width-50), random(50,height-50), random(20,40) )
