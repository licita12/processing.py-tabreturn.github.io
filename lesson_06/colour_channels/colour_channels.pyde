size(1000,720)
background('#004477')
noStroke()
modefenster = loadImage('modefenster.png')
image(modefenster, 0,0)

# grab a section of the display window
grab = get(0,0, 200,200)
image(grab, 600,100)

# grab a section of the display window and optional scale it
#    src. coords --> dest. coords 
copy(0,0,200,200,    600,600,100,100)

# read the color of a pixel
singlepixel = get(190,200)
fill(singlepixel)
rect(700,300, 200,200)

print(singlepixel) # -248272

halfwidth = width/2

x = 0
y = 0

for i in range(halfwidth*height):
    
    if i%halfwidth==0 and i!=0:
        y += 1
        x = 0
    x += 1
    
    # rgb
    
    pixel = get(x,y)
    #set(x+halfwidth, y, pixel)

    r = red(pixel)
    g = green(pixel)
    b = blue(pixel)
    
    rgb = color(r, g, b)
    #set( x+halfwidth, y, rgb )

    set( x+halfwidth, y, color(r,r,r) ) # red map
    set( x+halfwidth, y, color(g,g,g) ) # green map
    set( x+halfwidth, y, color(b,b,b) ) # blue map

    # greyscale

    #channelavg = (r + g + b) / 3
    channelavg = (r*0.89 + g*1.77 + b*0.33) / 3
    greyscale = color(channelavg, channelavg, channelavg)
    set( x+halfwidth, y, greyscale )
    
    # inverse colour
    
    invcolour = color(255-r, 255-g, 255-b)
    set( x+halfwidth, y, invcolour )
    
    # inverse greyscale
    
    invgreyscale = color(255-channelavg, 255-channelavg, 255-channelavg)
    set( x+halfwidth, y, invgreyscale )

# hsb

colorMode(HSB, 360, 100, 100)
x = 0
y = 0

for i in range(halfwidth*height):
    
    if i%halfwidth==0 and i!=0:
        y += 1
        x = 0
    x += 1
    
    pixel = get(x,y)
    h = hue(pixel)
    s = saturation(pixel)
    b = brightness(pixel)
    
    set( x+halfwidth,y, color(h, s, b) )           # pixel
    set( x+halfwidth,y, color((h-50)%360, s, b) )  # colour shift
    set( x+halfwidth,y, color((h+180)%360, s, b) ) # colour invert
    set( x+halfwidth,y, color(h, 100, b) )         # saturated
    
