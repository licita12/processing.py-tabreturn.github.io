size(500,500)
background('#004477')
noFill()
stroke('#FFFFFF')
strokeWeight(3)

#for i in range(24):
#for i in range(8,12):
for i in range(0,12,3):
    print(i)
    ellipse(width/2,height/2, 30*i,30*i)
