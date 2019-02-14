# This sketch makes use of:
# "Mona Lisa" by Leonardo da Vinci [Public domain]

size(1000,720)
background('#004477')
noFill()
monalisa = loadImage('mona-lisa.png')
image(monalisa, 0,0)

halfwidth = width/2
coltotal = 50.0                  # number of cells per row
cellsize = halfwidth/coltotal    # width/height of each cell
rowtotal = ceil(height/cellsize) # cells per column
col = 0
row = 0

for i in range( int(coltotal*rowtotal) ):
    
    x = int(col*cellsize) 
    y = int(row*cellsize)
    col += 1
    
    if col >= coltotal:
        col = 0
        row += 1
    
    #rect(x,y, cellsize,cellsize)
        
    # amplitude-modulated
    
    x = int(x+cellsize/2)
    y = int(y+cellsize/2)
    pixel = get(x,y)
    b = brightness(pixel)
    amp = 10*b/200.0
    noStroke()
    fill('#FFFFFF')
    ellipse(x+halfwidth,y, amp,amp)
    
    # pixelated 
    '''
    pixel = get(x,y)
    noStroke()
    fill(pixel)
    rect(x+halfwidth,y, cellsize,cellsize)
    '''
    
    # ascii
    '''
    x = int(x+2)
    y = int(y+cellsize)
    b = brightness( get(x,y) )

    # color ramp .:-=+*#%@
    if b < 255/10:
        glyph = ' '
    elif b < 255/9:
        glyph = '.'
    elif b < 255/8:
        glyph = ':'
    elif b < 255/7:
        glyph = '-'
    elif b < 255/6:
        glyph = '='
    elif b < 255/5:
        glyph = '+'
    elif b < 255/4:
        glyph = '*'
    elif b < 255/3:
        glyph = '#'
    elif b < 255/2:
        glyph = '%'
    elif b < 255/1:
        glyph = '@'
    
    fill('#FFFFFF')
    text(glyph, x+halfwidth,y)
    '''
    
