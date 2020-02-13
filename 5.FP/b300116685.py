# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 15:58:43 2020

@author: Amir
"""

list(map( lambda x: x * 2, range(10)))


#  Filter
list(filter( lambda x: x >= 5 , range(20)))


# Reduce

import functools
functools.reduce( lambda x, y: x + y, range(10))