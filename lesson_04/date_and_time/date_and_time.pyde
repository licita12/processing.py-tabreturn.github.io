y = year()    # returns the current year as an integer (2003, 2004, 2005, etc)
m = month()   # returns the current month as an integer from 1 - 12
d = day()     # returns the current day as a value from 1 - 31
print('{}-{}-{}'.format(y,m,d))

h = hour()    # returns the current hour as a value from 0 - 23.
m = minute()  # returns the current minute as an integer from 0 - 59
s = second()  # returns the current second as an integer from 0 - 59
print('{}-{}-{}'.format(h,m,s))
'''
for i in range(1000000):
    rect(10,10,10,10)
'''
ms = millis() # returns the number of milliseconds (thousandths of a second) since starting the program
print(ms)
    
