size(500,500)
background('#004477')
noFill()
stroke('#FFFFFF')
strokeWeight(3)

ellipse(100,100, 80,80)
'''
i = 1
row = 1
col = 1

while i <= 16:
    ellipse(100*col,100*row, 80,80)
    
    if i == 4 or i == 8 or i == 12:
        row += 1
        col = 0
    col += 1
    i += 1
