# -*- coding : utf-8 -*-

import functools

x = map (lambda x : x*2, range(10))
a = list (x)
print (a)

b = list(filter (lambda x : x > 5 , range(10)))
print(b)

c = functools.reduce(lambda x,y : x+y , range (10))
print (c)
