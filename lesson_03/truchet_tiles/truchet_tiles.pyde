size(600,600)
background('#004477')
noFill()
stroke('#FFFFFF')
strokeWeight(3)

#arc(0,0, 50,50, 0,PI/2)
#arc(50,50, 50,50, PI,PI+PI/2)

col = 0
row = 0

for i in range(1,145):
    #print( int(random(2)) == 1 )
    
    if int(random(2)) == 1:
        arc(col,row, 50,50, 0,PI/2)
        arc(col+50,row+50, 50,50, PI,PI+PI/2)
    else:
        arc(col+50,row, 50,50, PI/2,PI)
        arc(col,row+50, 50,50, PI+PI/2,2*PI)
        
    col += 50
    
    if i%12 == 0:
        row += 50
        col = 0

'''
# original truchet
col = 0
row = 0
rot = 1

fill('#FFFFFF')
noStroke()

for i in range(1,145):
    #r = int( random(1,4) )
    rot += 1
    if rot > 2:
        rot = 1
    r = rot
    
    if r == 3:
        triangle(col,row, col+50,row+50, col,row+50)    # |\
    elif r == 1:
        triangle(col+50,row, col+50,row+50, col,row+50) # /|
    elif r == 2:
        triangle(col,row, col+50,row, col+50,row+50)    # \|
    elif r == 4:
        triangle(col,row, col+50,row, col,row+50)       # |/
        
    col += 50
    
    if i%12 == 0:
        row += 50
        col = 0
'''
