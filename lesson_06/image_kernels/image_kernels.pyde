size(1000,720)
background('#004477')
noStroke()
mwaashambooy = loadImage('mwaash-ambooy-grey.png')
image(mwaashambooy, 0,0)

halfwidth = width/2
x = 0
y = 0

for i in range(halfwidth*height):
    
    if i%halfwidth==0 and i!=0:
        y += 1
        x = 0
    x += 1
    
    #sample = red( get(x,y) )
    sample = [
      red(get(x-1,y-1)), red(get(x,y-1)), red(get(x+1,y-1)),
      red(get(x-1,y))  , red(get(x,y))  , red(get(x+1,y)),
      red(get(x-1,y+1)), red(get(x,y+1)), red(get(x+1,y+1))
    ]
    
    #kernel = color(sample,sample,sample)
    # identity
    kernel = [
      0*sample[0], 0*sample[1], 0*sample[2],
      0*sample[3], 1*sample[4], 0*sample[5],
      0*sample[6], 0*sample[7], 0*sample[8]
    ]
    '''
    # box blur
    kernel = [
      0.11*sample[0], 0.11*sample[1], 0.11*sample[2],
      0.11*sample[3], 0.11*sample[4], 0.11*sample[5],
      0.11*sample[6], 0.11*sample[7], 0.11*sample[8]
    ]
    # edge detection
    kernel = [
      0*sample[0], 1*sample[1], 0*sample[2],
      1*sample[3],-4*sample[4], 1*sample[5],
      0*sample[6], 1*sample[7], 0*sample[8]
    ]
    # sharpen
    kernel = [
      0*sample[0],-1*sample[1], 0*sample[2],
     -1*sample[3], 5*sample[4],-1*sample[5],
      0*sample[6],-1*sample[7], 0*sample[8]
    ]
    '''
    #set(x+halfwidth, y, kernel)
    r = sum(kernel)
    set( x+halfwidth, y, color(r, r, r) )

'''
# colour kernel

mwaashambooy = loadImage('mwaash-ambooy-colour.png')
image(mwaashambooy, 0,0)

x = 0
y = 0

kernel = [
  2, 1, 0,
  1, 1,-1,
  0,-1,-2
]

for i in range(halfwidth*height):

    if i%halfwidth==0 and i!=0:
        y += 1
        x = 0
    x += 1
    
    # colour
    sample = [
      get(x-1,y-1), get(x,y-1), get(x+1,y-1),
      get(x-1,y)  , get(x,y)  , get(x+1,y),
      get(x-1,y+1), get(x,y+1), get(x+1,y+1)
    ]
    
    kernelr = [
      red(sample[0])*kernel[0], red(sample[1])*kernel[1], red(sample[2])*kernel[2],
      red(sample[3])*kernel[3], red(sample[4])*kernel[4], red(sample[5])*kernel[5],
      red(sample[6])*kernel[6], red(sample[7])*kernel[7], red(sample[8])*kernel[8]
    ]
    kernelg = [
      green(sample[0])*kernel[0], green(sample[1])*kernel[1], green(sample[2])*kernel[2],
      green(sample[3])*kernel[3], green(sample[4])*kernel[4], green(sample[5])*kernel[5],
      green(sample[6])*kernel[6], green(sample[7])*kernel[7], green(sample[8])*kernel[8]
    ]
    kernelb = [
      blue(sample[0])*kernel[0], blue(sample[1])*kernel[1], blue(sample[2])*kernel[2],
      blue(sample[3])*kernel[3], blue(sample[4])*kernel[4], blue(sample[5])*kernel[5],
      blue(sample[6])*kernel[6], blue(sample[7])*kernel[7], blue(sample[8])*kernel[8]
    ]
    
    rgb = color( sum(kernelr), sum(kernelg), sum(kernelb) )
    set( x+halfwidth, y, rgb )
    
