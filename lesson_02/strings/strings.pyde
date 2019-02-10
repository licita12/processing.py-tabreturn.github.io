size(500, 500)
background('#004477')
fill('#FFFFFF')

hello = 'hello world'
print(hello)

#whatsup = 'what's up!'
whatsup = "what\'s up!"
question = 'is your name really "world"?'
print(whatsup)
print(question)

#all = hello + whatsup + question
all = hello + '. ' + whatsup + ' ' + question
all = ('%s. %s %s') % (hello, whatsup, question)
print(all)
'''
hello world. what's up! is your name really "world"?
'''
print( len(all) )  # displays the total number of characters (52)

print( all[0] )    # displays the first character (h)
print( all[1] )    # displays character at position 1 (e)
print( all[4] )    # displays character at position 4 (o)
print( all[:4] )   # displays: hell
print( all[1:4] )  # displays: ell
print( all[4:] )   # displays: o world...

'''
[:-x] returns everything from index 0
up to but not including the fourth last character
'''
print( all[:-4] )  # ...ur name really "world"

'''
[-x:] returns everything from the fourth last character
to the end of the string
'''
print( all[-4:] )  # ld"?

'''
[x:-y] returns everything from index 4
to the end of the string
'''
print( all[4:-4] ) # o world. ...eally "wor

print( all.upper() )         # HELLO WO...Y "WORLD"?
print( all.title() )         # Hello Wo...y "World"?
print( all.count('o') )      # o
print( all.count('or') )     # 4
print( all.find('world') )   # 6
print( all.find('lemon') )  # -1
print( all.find('world',7) ) # 45

# print( all[0:5].title() + '...' )
print( all[0:5].title() + 
       all[all.find('.')] + 
       all[all.find(' ')] + 
       all[13:17].title() + 
       all[all.find(' is'):-16] + all[-1:] 
)
