# Map

list(map( lambda x: x * 2, range(10)))


#  Filter
list(filter( lambda x: x >= 5 , range(20)))


# Reduce

import functools
functools.reduce( lambda x, y: x + y, range(10))
