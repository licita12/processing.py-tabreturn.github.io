# creating new dictionaries

# list
studentlist = ['Sam', 24]

# dictionary
studentdict = {'name':'Sam', 'age':24}

# accessing dictionaries

print( studentdict['name'] )  # displays Sam
print( studentdict['age'] )   # displays 24
print( studentdict )          # {'name': 'Sam', 'age': 24}
print( studentdict.keys() )   # ['name', 'age']
print( studentdict.values() ) # ['Sam', 24]
print( studentdict.items() )  # [('name', 'Sam'), ('age', 24)]
items = studentdict.items()
print( items[0] )             # ('name', 'Sam')
print( items[0][0] )          # name

# modifying dictionaries

studentdict['age'] = 25
print( studentdict )          # {'name': 'Sam', 'age': 25}
studentdict['id'] = 19011501
print( studentdict )          # {'name': 'Sam', 'id': 19011501, 'age': 25}
del studentdict['age']
print(studentdict)            # {'name': 'Sam', 'id': 19011501}

# nested dictionaries

# dictionary of lists
students = {
  'names':['Sam', 'Lee'],
  'ages':[24, 18]
}
print( students['names'][1] ) # displays Lee

# list of dictionaries
students = [
  {'name':'Sam', 'age':24},
  {'name':'Lee', 'age':18}
]
print( students[1]['name'] )  # displays Lee

# iterating dictionaries

print(studentdict)
# {'name': 'Sam', 'id': 19011501}

#for k in studentdict.keys():
for k in studentdict:
    print(k)
    
for v in studentdict.values():
    print(v)

for k,v in studentdict.items():
    print(k,v)

for k,v in sorted( studentdict.items() ):
    print(k,v)
    
