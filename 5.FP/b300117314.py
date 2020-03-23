
"""
@author: Morti
"""


import functools

x = map (lambda x : x*2, range(15))
a = list (x)
print (a)

b = list(filter (lambda x : x > 5 , range(15)))
print(b)

c = functools.reduce(lambda x,y : x+y , range (15))
print (c)
