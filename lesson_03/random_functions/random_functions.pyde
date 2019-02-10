randomSeed(213)
size(600,600)
background('#004477')
noFill()
stroke('#FFFFFF')
strokeWeight(3)

x = random(5)
print(x)
x = random(5,10)
print(x)
print( int(x) )

#for i in range(100):
#    point( random(width), height/2 )

for i in range(1000):
    point( random(width), random(height) )

'''
# gaussian
for i in range(100):
    g = randomGaussian()
    
    if abs(g) > 1 :
        print(g)
        
    point(width/2 + g * 100, height/2)
    
