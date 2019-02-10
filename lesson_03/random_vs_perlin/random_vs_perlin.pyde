size(900,600)
background('#004477')
noFill()
strokeWeight(3)

translate(0,20)

randomSeed(2)
beginShape()
for i in range(0,width+15,15):
    y = random(0,height/2)
    #vertex(i,y)
    stroke('#FFFFFF')
    ellipse(i,y, 3,3)
    stroke('#0099FF')
endShape()

noiseSeed(2)
ni = 0.1
beginShape()
for i in range(0,width+15,15):
    y = map(noise(ni), 0,1, height/2,height)
    #vertex(i,y)
    stroke('#FFFFFF')
    ellipse(i,y, 3,3)
    stroke('#0099FF')
    ni += 0.1
endShape()
