size(1050,500)
background('#004477')
noStroke()

# no tint
img = loadImage('guardian-lion.png')
image(img, 0,0)

# orange tint
#tint(255,153,0)
orange = color(255,153,0)
tint(orange)  
image(img, width/3,0)

# orange and 50% transparent
orange50 = color(255,153,0,128)
tint(orange50)
#image(img, width/3*2,0)

# manual tint

thirdwidth = width/3
x = 0
y = 0

for i in range( thirdwidth*(height-50) ):
    
    x += 1

    if i%thirdwidth==0 and i!=0:
        y += 1
        x = 0
    
    colorMode(RGB, 1,1,1,1)
    
    layer1 = get(x,y)
    r = red(orange50) * red(layer1)
    g = green(orange50) * green(layer1)
    b = blue(orange50) * blue(layer1)
    a = alpha(orange50)
    fill( color(r,g,b,a) )
    rect(x+width-thirdwidth, y, 1, 1)
    
