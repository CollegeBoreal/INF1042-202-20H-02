# PROJET DE FIN DE SESSION HIVER 2020 INTRODUCTION À LA PROGRAMMATION
* PROJET FUN SUR LA CRÉATION DU JEU DU PENDU
* EN QUOI CONSISTE CE JEU
* Le but du jeu est de trouver un mot en devinant les lettres qui le composent

:one: LES DIFFÉRENTES PARTIES QUI CONSTITUENT CE JEU DE PENDU

:a: CRÉATION D'UNE LISTE DE MOT
* avec [ ]
* ensuite pour que les mots soit choisi de manière aléatoire, on utilise le module random

et ça donne 
```
import random
a = ["", "", ""]
b = random.choice(a)
```

:b: LA GESTION DU TEMPS POUR CONTRÔLER LE FLUX D'INFORMATIONS QU'ON TRANSMET AU JOUEUR
* Avec le module time

et ça donne
```
import time
time.sleep(le nombre de seconde)
```


:c: DÉTERMINATION DU NOMBRE D'ESSAI

* Dans notre jeu le nombre d'essai correspond à la longueur du mot à trouvé

$ len
