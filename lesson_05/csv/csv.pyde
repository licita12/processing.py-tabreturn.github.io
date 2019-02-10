csv = loadStrings('playlist.csv')
#print(csv)

for entry in csv:
    #print(entry)
    #print( entry.split(',') )
    print( entry.split(',')[1] )
    
