from amoeba import Amoeba

def setup():
    size(800,800)

amoebas = []

for i in range(8):      # number of amoeba
    amoebas.append( Amoeba(
      random(900),      # x
      random(900),      # y
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
        a.velocity.limit(a.topspeed)
        a.update()
        
        # collision detection
        
        for b in amoebas:
            distance = dist(
                         a.location.x, a.location.y + a.diameter/2, 
                         b.location.x, b.location.y + b.diameter/2
                       )
            
            if distance < a.diameter/2 + b.diameter/2:
                goto = PVector.sub(b.location, a.location)
                goto.div(1000)
                goto.mult(-1)
                a.velocity.add(goto)
            
            # collisions visualized
            
            strokeWeight(1)
            noFill()
            
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
        
        # colliders visualized
        
        noFill()
        stroke('#FF0000')
        ellipse(a.location.x, a.location.y+a.diameter/2, a.diameter, a.diameter)

# a-key to add an amoeba; d-key to remove one
        
def keyReleased():
    
    print(keyCode)
    
    if keyCode == 65:
        amoebas.append( Amoeba(
        random(900),      # x
        random(900),      # y
        random(-0.5,0.5), # xspeed
        random(-0.5,0.5), # yspeed
        random(50,200)    # diameter
        )) 

    elif keyCode == 68 and len(amoebas) > 0:
        amoebas.pop()
