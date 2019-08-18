class Amoeba:

    def __init__(self, x, y, xspeed, yspeed, diameter):
        
        # instance variables
        
        self.location = PVector(x, y)
        self.velocity = PVector(xspeed, yspeed)
        self.topspeed = self.velocity.mag()
        self.wobblex = random(xspeed*diameter/20, xspeed*diameter/20)
        self.wobbley = random(yspeed*diameter/20, yspeed*diameter/20)
        self.diameter = float(diameter)
        self.t = 0.0
        
        # nucleus color
        
        nucleusfills = ['#FF0000','#FF9900','#FFFF00','#00FF00','#0099FF','#6633FF']
        self.nucleus = [
          self.diameter/200*int(random(-5,5)), # y-coord
          self.diameter/random(1.5, 2.5),      # x-coord
          self.diameter/random(2.5, 3),        # width & height
          nucleusfills[ int(random(len(nucleusfills))) ]
        ]
        
    def ellips(self, x, y, t):
        x = x * cos(t)
        y = y * sin(t)
        return [x,y]
        
    def update(self):
        self.location.add(self.velocity)
        
        # nucleus
        
        fill(self.nucleus[3])
        noStroke()
        ellipse(
          self.location.x+self.nucleus[0],
          self.location.y+self.nucleus[1],
          self.nucleus[2],
          self.nucleus[2]
        )
        
        # cell
        
        fill(0x880099FF)
        stroke('#FFFFFF')
        strokeWeight(3)
        v1 = self.ellips(1, 2, self.t)
        v1x = v1[0] * self.wobblex
        v1y = v1[1] * self.wobbley
        v2 = self.ellips(2, 3, self.t)
        v2x = v2[0] * self.wobblex
        v2y = v2[1] * self.wobbley
        v3 = self.ellips(5, 2, self.t)
        v3x = v3[0] * self.wobblex
        v3y = v3[1] * self.wobbley
        v4 = self.ellips(2, 2, self.t)
        v4x = v4[0] * self.wobblex
        v4y = v4[1] * self.wobbley
        self.t += 0.05
        d = self.diameter
        r = self.diameter/2.0
        c = self.diameter/2/100*60
        beginShape()
        vertex(
          self.location.x+0, self.location.y+0
        )
        bezierVertex(
          self.location.x+c+v1x, self.location.y+0+v1y,
          self.location.x+r+v2x, self.location.y+r-c+v2y, 
          self.location.x+r, self.location.y+r
        )
        bezierVertex(
          self.location.x+r+v2x*-1, self.location.y+r+c+v2y*-1,
          self.location.x+c+v3x, self.location.y+d+v3y,
          self.location.x+0, self.location.y+d
        )
        bezierVertex(
          self.location.x+-c+v3x*-1, self.location.y+d+v3y*-1,
          self.location.x+-r+v4x, self.location.y+r+c+v4y,
          self.location.x+-r, self.location.y+r
        )
        bezierVertex(
          self.location.x+-r+v4x*-1, self.location.y+r-c+v4y*-1,
          self.location.x+-c+v1x*-1, self.location.y+0+v1y*-1,
          self.location.x+0, self.location.y+0
        )
        endShape()
        
        # control points visualized
        '''
        stroke('#FF0000')
        strokeWeight(1)
        line(
          self.location.x+c+v1x, self.location.y+0+v1y, 
          self.location.x+-c+v1x*-1, self.location.y+0+v1y*-1
        )
        line(
          self.location.x+r+v2x, self.location.y+r-c+v2y, 
          self.location.x+r+v2x*-1, self.location.y+r+c+v2y*-1
        )
        line(
          self.location.x+c+v3x, self.location.y+d+v3y,
          self.location.x+-c+v3x*-1, self.location.y+d+v3y*-1
        )
        line(
          self.location.x+-r+v4x, self.location.y+r+c+v4y,
          self.location.x+-r+v4x*-1, self.location.y+r-c+v4y*-1
        )
        '''
        
