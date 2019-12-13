size(500,380)
background('#004477')
noFill()
stroke('#FFFFFF')
strokeWeight(3)

h = 50
translate(100,40)

# 0-dimensional
bands = 6
rect(0,0, 40,h*bands)

# 1-dimensional
bands = [
  '#FF0000',
  '#FF9900',
  '#FFFF00',
  '#00FF00',
  '#0099FF',
  '#6633FF'
]

for i,band in enumerate(bands):
    fill(band)
    rect(0,i*h, 40,h)

# 2-dimensional
bands = [
  [ 100, 0, 0   ],
  [ 100, 60, 0  ],
  [ 100, 100, 0 ],
  [ 0, 100, 0   ],
  [ 0, 60, 100  ],
  [ 40, 20, 100 ]
]

print( bands[1][1] )    # display 60

colorMode(RGB, 100)

for i,band in enumerate(bands):
    r = band[0]
    g = band[1]
    b = band[2]
    #sum = r + g + b
    #avg = sum / 3
    #fill(avg, avg, avg)
    #rect(0,i*h, sum,h)
    fill('#FF0000')
    rect(0,i*h, r,h)
    fill('#00FF00')
    rect(0+r,i*h, g,h)
    fill('#0099FF')
    rect(0+r+g,i*h, b,h)

# 3-dimensional
bands = [
  [ [ 100, 0, 0   ], 'red'    ],
  [ [ 100, 60, 0  ], 'orange' ],
  [ [ 100, 100, 0 ], 'yellow' ],
  [ [ 0, 100, 0   ], 'green'  ],
  [ [ 0, 60, 100  ], 'blue'   ],
  [ [ 40, 20, 100 ], 'violet' ]
]

print( bands[1][0][1] ) # display 60

# labels
bands = [
  [100, 0, 0, 'red'],
  [100, 60, 0, 'orange'],
  [100, 100, 0, 'yellow'],
  [0, 100, 0, 'green'],
  [0, 60, 100, 'blue'],
  [40, 20, 100, 'violet']
]

for i,band in enumerate(bands):
    fill('#FFFFFF')
    textAlign(RIGHT)
    text(band[3], -20,i*h+30)
    
