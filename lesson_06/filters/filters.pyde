# This sketch makes use of:
# "Rubber Duck" by Florentijn Hofman, in Darling Harbour as part of the 2013 Sydney Festival.
# Newtown grafitti [CC BY 2.0], via Wikimedia Commons

size(480,480)
background('#004477')

rubberduck = loadImage(
  '480px-Rubber_Duck_in_Sydney,_January_5,_2013.jpg'
)
image(rubberduck, 0,0)
textSize(28)
text('Rubber Duck', 20,150)

filter(BLUR, 3)

#filter(DILATE); filter(DILATE)
#filter(ERODE); filter(ERODE)
#filter(GRAY)
#filter(INVERT)
#filter(POSTERIZE, 3)
#filter(THRESHOLD)
'''
filter(BLUR, 30); filter(POSTERIZE, 4)
filter(BLUR, 30); filter(POSTERIZE, 4)
filter(BLUR, 30); filter(POSTERIZE, 4)
'''
textSize(15)
text('Sydney, 2013', 20,180)
