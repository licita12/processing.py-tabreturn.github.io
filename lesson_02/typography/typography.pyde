size(500, 500)
background('#004477')
fill('#FFFFFF')
stroke('#0099FF')
strokeWeight(3)

razor = 'Never attribute to malice that which is adequately explained by stupidity.'

text(razor, 0,50)

textSize(20)
text(razor, 0,100)

print( PFont.list() )
timesroman = createFont('Times-Roman', 20)
textFont(timesroman)
text(razor, 0,150)

textLeading(10)
text(razor, 0,200, 250,100)

textAlign(RIGHT)
text(razor, 0,250, 250,100)

textAlign(LEFT)
hanlons = '- Hanlon\'s'
razor = 'razor'
text(hanlons + ' ' + razor, 0,350)
line(
  textWidth(hanlons), 0,
  textWidth(hanlons), height
)
