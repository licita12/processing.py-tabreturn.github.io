rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
print( len(rainbow) )

# using range
'''
for i in range( len(rainbow) ):
    print(rainbow[i])
'''

# using no range
for band in rainbow:
    print(band)

# using enumerate
for i,v in enumerate(rainbow):
    print( ('%s: %s') % (i, v) )
