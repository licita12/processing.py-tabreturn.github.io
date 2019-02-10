size(600,600)
background('#004477')
fill('#FFFFFF')
noStroke()
#img = loadImage('progressively_jittery_quads.png')
#image(img, 0,0)

col = 0
row = 0
jitter = 0

for i in range(1,65):
    quad(
      50+col+random(-jitter, jitter), 50+row+random(-jitter, jitter),       # top-left
      50+col+45+random(-jitter, jitter), 50+row+random(-jitter, jitter),    # top-right 
      50+col+45+random(-jitter, jitter), 50+row+45+random(-jitter, jitter), # bottom-right
      50+col+random(-jitter, jitter), 50+row+45+random(-jitter, jitter)     # bottom-left
    )
    col += 65
    
    if i%8 == 0:
        col = 0
        row += 65
    
    jitter += 0.3
