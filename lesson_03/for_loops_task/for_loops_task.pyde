size(600,600)
background('#004477')
noFill()
stroke('#FFFFFF')
strokeWeight(3)

# challenges

for i in range(12):
    print(i)
    line(75,138+i*13, 228,88+i*13)

distance = 10;
for i in range(1,9):
    line(370,70+distance, 522,70+distance)
    distance *= 1.5

for i in range(13):
    if i%2 > 0:
        line(302,370+(13*i), 377,370+(13*i))
    else:
        line(225,370+(13*i), 300,370+(13*i))
    
# guidelines
'''
stroke('#0099FF')
fill('#0099FF')

line(75,138, 228,88)
text('(75, 138)', 75-40,138-10)
text('(228, 88)', 228-20,88-10)

line(370,80, 522,80)
text('(370, 80)', 370-40,80-10)
text('(522, 80)', 522-20,80-10)

line(225,370, 300,370)
text('(225, 370)', 225-40,370-10)
text('(300, 370)', 300-20,370-10)
