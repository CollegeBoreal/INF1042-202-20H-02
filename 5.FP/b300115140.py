# -*- coding: utf-8 -*-
"""
FP : Map et filter
"""
#map
t = (map(lambda x : x*2, range (10)))
print (list(t))


# filter
l = list(filter(lambda x: x >= 5, [ x for x in range(20) ]))
print (list(l))


#reduce
import functools
f = functools.reduce( lambda x, y: x + y, range(5))
print (f)


