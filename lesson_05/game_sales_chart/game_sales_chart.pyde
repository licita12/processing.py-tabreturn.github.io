size(800,800)
background('#004477')
noStroke()
csv = loadStrings('list_of_best-selling_video_games.csv')

tetrisentry = csv[1].split('\t')
tetrissales = tetrisentry[1]
#print( tetrissales + 1 )
print( int(tetrissales) + 1 )

'''
rainbow = [
  '#FF0000',
  '#FF9900',
  '#FFFF00',
  '#00FF00',
  '#0099FF',
  '#6633FF'
]

for i in range(1, len(csv)):
    entry = csv[i]
    #print(entry)
    #print(entry.split('\t'))
    #print(entry.split('\t')[0]) # rank
    #print(entry.split('\t')[1]) # sales
    #print(entry.split('\t')[2]) # title
    #print(entry.split('\t')[3]) # developer
    #print(entry.split('\t')[4]) # publisher
    
    fields = entry.split('\t')
    
    # u represts the width of the display divided by tetris sales 
    # (multiply u by a title's sales to calculate a bar's width)
    tetrissales = float(csv[1].split('\t')[1])
    u = width / tetrissales
    
    barwidth = u * int(fields[1])
    barheight = float(height) / (len(csv)-1)
    barx = 0
    bary = barheight * (int(fields[0])-1)
    
    fill( rainbow[(int(fields[0])-1) % len(rainbow)] )

    rect(barx,bary, barwidth,barheight)
    fill(0)
    text( fields[2], barx+5, bary+barheight-3 )
