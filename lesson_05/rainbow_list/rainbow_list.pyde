rainbow = ['blue', 'orange', 'yellow']

print(rainbow)
print(rainbow[0])   # displays blue
print(rainbow[1])   # displays orange
print(rainbow[2])   # displays yellow
print(rainbow[-1])  # displays yellow
print(rainbow[-2])  # displays orange
print(rainbow[0:2]) # displays ['blue', 'orange']

rainbow[0] = 'red'
print(rainbow)      # ['red', 'orange', 'yellow']

rainbow.append('blue')
print(rainbow)      # red, orange, yellow, blue

colors = ['indigo', 'violet']
rainbow.extend(colors)
print(rainbow)      # red, orange, yellow, blue, indigo, violet

yellowindex = rainbow.index('yellow')
print(yellowindex)  # 2

rainbow.insert(3, 'green')
print(rainbow)      # red, orange, yellow, green, blue, indigo, violet

i = rainbow.pop(5)  # removes indigo and assigns it to i
'''
or, to just remove indigo:
rainbow.pop(5)
'''
print(i)            # indigo
print(rainbow)      # red, orange, yellow, green, blue, violet

rainbow.pop()       # removes violet
print(rainbow)      # red, orange, yellow, green, blue

rainbow.extend(colors)
print(rainbow)      # red, orange, yellow, green, blue, indigo, violet

rainbow.remove('indigo')
print(rainbow)      # red, orange, yellow, green, blue, violet
