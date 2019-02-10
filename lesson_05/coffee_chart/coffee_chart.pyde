size(800,800)
background('#004477')

mug = 110
col = 1
row = 1
coffees = [
  'cafe con leche', 'espresso', 'demi-creme',
  'americano', 'capucchino', 'latte',
  'ristretto', 'macchiato', 'flat white'
]

for coffee in coffees:
    x = width/4*col
    y = height/4*row

    # mug
    stroke('#FFFFFF')
    strokeWeight(4)
    noFill()
    arc(x+55,y, 40, 40, -HALF_PI, HALF_PI)
    arc(x+55,y, 65, 65, -HALF_PI, HALF_PI)
    rect(x-mug/2,y-mug/2, mug,mug)

    if col%3 == 0:
        row += 1
        col = 1
    else:
        col += 1

'''
mug = 110
col = 1
row = 1

coffees = [
  { 'name':'cafe con leche','espresso':50, 'hotwater':0, 'steamedmilk':30,'foamedmilk':0  },
  { 'name':'espresso',      'espresso':60, 'hotwater':0, 'steamedmilk':0, 'foamedmilk':0  },
  { 'name':'demi-creme',    'espresso':40, 'hotwater':0, 'steamedmilk':40,'foamedmilk':0  },
  { 'name':'americano',     'espresso':60, 'hotwater':30,'steamedmilk':0, 'foamedmilk':0  },
  { 'name':'capucchino',    'espresso':40, 'hotwater':0, 'steamedmilk':30,'foamedmilk':30 },
  { 'name':'latte',         'espresso':35, 'hotwater':0, 'steamedmilk':10,'foamedmilk':30 },
  { 'name':'ristretto',     'espresso':30, 'hotwater':0, 'steamedmilk':0, 'foamedmilk':0  },
  { 'name':'macchiato',     'espresso':40, 'hotwater':0, 'steamedmilk':0, 'foamedmilk':60 },
  { 'name':'flat white',    'espresso':40, 'hotwater':0, 'steamedmilk':60,'foamedmilk':0  }
]

for coffee in coffees:
    print(coffee['name'])
    print(coffee['espresso'])
    print(coffee['hotwater'])
    print(coffee['steamedmilk'])
    print(coffee['foamedmilk'])
    print('---')
    
    x = width/4*col
    y = height/4*row
    level = 0
    
    noStroke()
    # espresso
    fill('#332222')
    rect(x-mug/2,y+mug/2-coffee['espresso']-level, mug,coffee['espresso'])
    level += coffee['espresso']
    
    # hotwater
    fill('#0099FF')
    rect(x-mug/2,y+mug/2-coffee['hotwater']-level, mug,coffee['hotwater'])
    level += coffee['hotwater']
    
    # steamedmilk
    fill('#FFFFFF')
    rect(x-mug/2,y+mug/2-coffee['steamedmilk']-level, mug,coffee['steamedmilk'])
    level += coffee['steamedmilk']
    
    # foamedmilk
    fill('#DDDDDD')
    rect(x-mug/2,y+mug/2-coffee['foamedmilk']-level, mug,coffee['foamedmilk'])
    level += coffee['foamedmilk']
    
    # mug
    stroke('#FFFFFF')
    strokeWeight(4)
    noFill()
    arc(x+55,y, 40, 40, -HALF_PI, HALF_PI)
    arc(x+55,y, 65, 65, -HALF_PI, HALF_PI)
    rect(x-mug/2,y-mug/2, mug,mug)
    
    # label
    fill('#FFFFFF')
    text(coffee['name'], x-textWidth(coffee['name'])/2, y+90)
    
    if col%3 == 0:
        row += 1
        col = 1
    else:
        col += 1
        
