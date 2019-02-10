# pi constants
print(PI)
print(TWO_PI)
print(TAU)
print(HALF_PI)
print(QUARTER_PI)

# converting between radians and degrees
print(45 * (PI/180))    # or radians(45)
print(0.785 * (180/PI)) # or degrees(0.785)

# clock

def setup():
    size(600,600)
    noFill()
    stroke('#FFFFFF')
    
def draw():
    background('#004477')
    translate(width/2, height/2)
    strokeWeight(3)
    ellipse(0,0, 350,350)
    
    rotate(-HALF_PI)

    h = TAU/12 * hour()
    pushMatrix()
    rotate(h)
    strokeWeight(10)
    line(0,0, 100,0)
    popMatrix()
    
    m = TAU/60 * minute()
    pushMatrix()
    rotate(m)
    strokeWeight(5)
    line(0,0, 130,0)
    popMatrix()

    s = TAU/60 * second()
    pushMatrix()
    rotate(s)
    strokeWeight(2.5)
    line(0,0, 130,0)
    popMatrix()
