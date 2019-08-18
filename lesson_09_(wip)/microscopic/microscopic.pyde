from amoeba import Amoeba

amoebas = []

def setup():
    size(800,800)
    global amoebas
    
    for i in range(8):      # number of amoeba
        amoebas.append(Amoeba(
          random(width),    # x
          random(width),    # y
          random(-0.5,0.5), # xspeed
          random(-0.5,0.5), # yspeed
          random(50,200)    # diameter
        )) 
    
def draw():
    background('#004477')
    
    for a in amoebas:
        
        # mouse interaction
        
        mouse = PVector(mouseX, mouseY-a.diameter/2)
        goto = PVector.sub(mouse, a.location)
        goto.div(10000)
        if mousePressed:
            goto.mult(-1)
        a.velocity.add(goto)
        
        # update
        
        a.velocity.limit(a.topspeed)
        a.update()
        
        # (start of the) collision detection 

        strokeWeight(1)
        stroke('#FF0000')
        noFill()
        ellipse(a.location.x, a.location.y+a.diameter/2, a.diameter, a.diameter)
        
        for b in amoebas:
            distance = dist(
                         a.location.x, a.location.y +a.diameter/2, 
                         b.location.x, b.location.y + b.diameter/2
                       )
            
            if distance < a.diameter/2 + b.diameter/2:
                goto = PVector.sub(b.location, a.location)
                goto.div(1000)
                goto.mult(-1)
                a.velocity.add(goto)
                stroke('#00FF00')
            else: 
                stroke('#FF0000')
            
             
            line(
              a.location.x, a.location.y + a.diameter/2,
              b.location.x, b.location.y + b.diameter/2
            )

# left-click to randomly add; right-click to randomly eliminate
        
def mousePressed(): 
    if mouseButton == LEFT:
        amoebas.append(Amoeba(
          random(width),    # x
          random(width),    # y
          random(-0.5,0.5), # xspeed
          random(-0.5,0.5), # yspeed
          random(50,200)    # diameter
        )) 
    
    if mouseButton == RIGHT:
        amoebas.pop()
