size(960,480)
background('#004477')
noStroke()
halfwidth = width/2

fill('#FF0000'); rect(0,0,width,80)
fill('#FF9900'); rect(0,80,width,80)
fill('#FFFF00'); rect(0,160,width,80)
fill('#00FF00'); rect(0,240,width,80)
fill('#0099FF'); rect(0,320,width,80)
fill('#6633FF'); rect(0,400,width,80)
    
rubberduck = loadImage(
  '480px-Rubber_Duck_in_Sydney,_January_5,_2013.jpg'
)
image(rubberduck, 0,0)

# manual blends

colorMode(RGB, 1)
#c = color(1,0,0) # red

x = 0
y = 0

for i in range(halfwidth*height):

    if i%halfwidth==0 and i!=0:
        y += 1
        x = 0
    x += 1

    layer1 = get(x, y)
    layer0 = get(x+halfwidth, y)
    r = red(layer0) * red(layer1)
    g = green(layer0) * green(layer1)
    b = blue(layer0) * blue(layer1)
    set( x+halfwidth, y, layer1 )
    
'''
blendMode(MULTIPLY)
image(rubberduck, halfwidth,0)
fill('#FF0000')
ellipse(halfwidth,height/2, 300,300)
blendMode(BLEND)
# back to normal hereafter ...
