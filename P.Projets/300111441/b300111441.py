# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 15:43:59 2020
@author: skofo
"""

import random,math
sv = 0
sc = 0
nb_simul = 5000
for x in range(nb_simul):
    arr1 = random.randint(0,60)
    arr2 = random.randint(0,60)
    c = abs(arr1 - arr2)
    sv = sv + c
    sc = sc + c * c
mv = sv / nb_simul
mc = sc / nb_simul
e = math.sqrt((mc - mv * mv)/nb_simul)
print("Estimation ponctuelle",mv)
