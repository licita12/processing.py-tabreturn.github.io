# This is a recreation of:
# "Composition II in Red, Blue, and Yellow"
# Piet Mondrian [Public domain] 

size(480,480)
background('#004477')
noSmooth()
noStroke()

# red square
fill('#FF8800'); rect(0,0,width,350)
blendMode(SUBTRACT)
fill('#008800'); rect(0,0,width,350)
'''
# white bottom edge
blendMode(ADD)
fill('#FF0000'); rect(105,350,375,130)
fill('#00BB00'); rect(105,350,375,130)
fill('#000088'); rect(105,350,375,130) 

# yellow corner
blendMode(DARKEST) # or MULTIPLY
fill('#FFFF00'); rect(435,0,45,height)

# white right edge squares
blendMode(BLEND) # or ADD/LIGHTEST
noStroke()
fill('#FFFFFF'); rect(435,350,45,54)
rect(0,0,105,144); rect(0,167,105,183)

# blue corner
blendMode(SCREEN)
fill('#0088FF'); rect(0,350,105,height)

# unwanted circle 
blendMode(LIGHTEST)
fill('#0099FF'); ellipse(70,414,120,120)
# can't make the circle vanish?
# are you sure the previous blend is correct?

# thinner lines
blendMode(SUBTRACT)
stroke('#FFFFFF')
strokeWeight(11); line(105,0,105,height)
line(0,350,width,350); line(434,350,434,height)

strokeWeight(23)
strokeCap(SQUARE)

# thicker line upper-left
blendMode(MULTIPLY)
stroke('#00FFFF'); line(0,155,100,155)

# thicker line lower-right
blendMode(DIFFERENCE)
stroke('#FFFF00'); line(440,415,width,415)
