size(500,500)
noStroke()
background('#004477')

bands = [
  '#FF9900', # orange
  '#6633FF', # violet
  '#0099FF', # blue
  '#FF0000', # red
  '#FFFF00', # yellow
  '#00FF00', # green
]

# INSTRUCTIONS
'''# move violet
violet = bands[_]
bands.append(violet)
bands.remove(violet)'''

'''# move blue
blueindex = bands.index('_______')
bands.insert(4, bands.pop(blueindex))'''

'''# switch orange and red
bands.insert(bands.index('_______'), bands.___(_))'''

# SOLUTIONS
# move violet
violet = bands[1]
bands.append(violet)
bands.remove(violet)

# move blue
blueindex = bands.index('#0099FF')
bands.insert(4, bands.pop(blueindex))

# switch orange and red
bands.insert(bands.index('#FF9900'), bands.pop(1))

'''
fill(bands[0]); rect(0,100, width,50)
fill(bands[1]); rect(0,150, width,50)
fill(bands[2]); rect(0,200, width,50)
fill(bands[3]); rect(0,250, width,50)
fill(bands[4]); rect(0,300, width,50)
fill(bands[5]); rect(0,350, width,50)
'''
for i,v in enumerate(bands):
    fill(v)
    rect(0,100+(50*i), width,50)
