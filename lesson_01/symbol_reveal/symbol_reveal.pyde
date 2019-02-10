# setup new document
size(600, 740)
background('#004477')
noFill()
stroke('#FFFFFF')
strokeWeight(3)

xco = 400
yco = 440

'''
1. Draw a line beginning at an x-coordinate of half the display window width, and y-coordinate of a third of the window height.
   The endpoint must have an x/y-coordinate equal to xco & yco
'''
line(width/2,height/3, xco,yco)

'''
2. Draw a centred ellipse with a width that is an eleventh of the display window width, 
   and a height that is a fourteenth of the window height.
3. Draw a centred ellipse with a width that is a nineteenth of the display window width, 
   and a height that is a twenty-second of the window height.
4. Draw a line beginning at an x/y-coordinate equal to xco & yco respectively. 
   The endpoint must have an x-coordinate of the display window width minus xco, and a y-coordinate equal to yco.
5. Draw a line beginning at an x-coordinate of the display window width minus xco, and y-coordinate equal to yco. 
   The endpoint must have an x-coordinate of half the display window width, and a y-coordinate of a third of the window height.
6. Draw a centred ellipse with a width that is a fifth of the display window width, 
   and height that is a twelfth of the display window height.
'''
ellipse(width/2, height/2, width/11, height/14)
ellipse(width/2, height/2, width/19, height/22)
line(xco,yco, width-xco,yco)
line(width-xco,yco, width/2,height/3)
ellipse(width/2, height/2, width/5, height/12)
