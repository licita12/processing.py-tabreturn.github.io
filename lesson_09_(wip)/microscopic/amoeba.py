class Amoeba:
    
    def __init__(self, x, y, xspeed, yspeed, diameter):
        
        # instance variables
        
        self.location = PVector(x,y)
        self.velocity = PVector(xspeed, yspeed)
        self.topspeed = self.velocity.mag()
        self.diameter = float(diameter)
        self.wobbleradii = []
        
        for i in range(4):
            self.wobbleradii.append( PVector(
              random(-xspeed*diameter/5, xspeed*diameter/5),
              random(-yspeed*diameter/5, yspeed*diameter/5)
            ))
            
        self.t = 0.0
        
        # nucleus color
        
        nucleusfills = ['#FF0000','#FF9900','#FFFF00','#00FF00','#0099FF','#6633FF']
        self.nucleus = [
          self.diameter/200*int(random(-5,5)), # y-coord
          self.diameter/random(1.5, 2.5),      # x-coord
          self.diameter/random(2.5, 3),        # width & height
          nucleusfills[ int(random(len(nucleusfills))) ]
        ]
    
    # methods
    
    def ellips(self, x, y, t):
        x = x * cos(t)
        y = y * sin(t)
        return [x,y]
    
    def update(self):
        
        # nucleus

        fill(self.nucleus[3])
        noStroke()
        ellipse(
          self.location.x+self.nucleus[0],
          self.location.y+self.nucleus[1],
          self.nucleus[2],
          self.nucleus[2]
        )
        
        # shape
        
        fill(0x880099FF)
        stroke('#FFFFFF')
        strokeWeight(3)
        self.location += self.velocity
        self.t += 0.05
        d = self.diameter
        r = d/2.0
        c = r*0.552
        e = []
        
        for i in self.wobbleradii:
            xy = self.ellips(i.x, i.y, self.t)
            e.append( PVector(xy[0], xy[1]) )
            
        beginShape()
        vertex(
          self.location.x+0, self.location.y+0
        )
        bezierVertex(
          self.location.x+c+e[0].x, self.location.y+e[0].y,
          self.location.x+r+e[1].x, self.location.y+r-c+e[1].x,
          self.location.x+r, self.location.y+r
        )
        bezierVertex(
          self.location.x+r+e[1].x*-1, self.location.y+r+c+e[1].y*-1,
          self.location.x+c+e[2].x, self.location.y+d+e[2].y,
          self.location.x, self.location.y+d
        )
        bezierVertex(
          self.location.x-c+e[2].x*-1, self.location.y+d+e[2].y*-1,
          self.location.x-r+e[3].x, self.location.y+r+c+e[3].y,
          self.location.x-r, self.location.y+r
        )
        bezierVertex(
          self.location.x-r+e[3].x*-1, self.location.y+r-c+e[3].y*-1,
          self.location.x-c+e[0].x*-1, self.location.y+e[0].y*-1,
          self.location.x, self.location.y
        )
        endShape()
        
        # control points visualized
        
        stroke('#FF0000')
        strokeWeight(2)
        line(
          self.location.x+c+e[0].x, self.location.y+e[0].y, 
          self.location.x-c+e[0].x*-1, self.location.y+e[0].y*-1
        )
        line(
          self.location.x+r+e[1].x, self.location.y+r-c+e[1].y, 
          self.location.x+r+e[1].x*-1, self.location.y+r+c+e[1].y*-1
        )
        line(
          self.location.x+c+e[2].x, self.location.y+d+e[2].y,
          self.location.x-c+e[2].x*-1, self.location.y+d+e[2].y*-1
        )
        line(
          self.location.x-r+e[3].x, self.location.y+r+c+e[3].y,
          self.location.x-r+e[3].x*-1, self.location.y+r-c+e[3].y*-1
        )
        
