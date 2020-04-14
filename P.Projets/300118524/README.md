# PROJET DE FIN DE SESSION HIVER 2020 INTRODUCTION À LA PROGRAMMATION
* PROJET FUN SUR LA CRÉATION DU JEU DU PENDU
* EN QUOI CONSISTE CE JEU

Le but du jeu est de trouver un mot en devinant les lettres qui le composent

:video_game: :eyes:

:point_down:

<img src="Capture d’écran, le 2020-04-14 à 08.45.39.png" width="580" height="341"></img>

:eyes: :play:


:x: LES DIFFÉRENTES PARTIES QUI CONSTITUENT CE JEU DE PENDU :x:

:one: CRÉATION D'UNE LISTE DE MOT
* avec [ ]
* ensuite pour que les mots soit choisi de manière aléatoire, on utilise le module random

et ça donne 
```
import random
a = ["", "", ""]
b = random.choice(a)
```

:two: LA GESTION DU TEMPS POUR CONTRÔLER LE FLUX D'INFORMATIONS QU'ON TRANSMET AU JOUEUR
* Avec le module time

et ça donne
```
import time
time.sleep(le nombre de seconde)
```


:three: DÉTERMINATION DU NOMBRE D'ESSAI

* Dans notre jeu le nombre d'essai correspond à la longueur du mot à trouvé

* grâce à ("len")

:four: CRÉATION D'UNE BOUCLE WHILE
* si le nombre d'essaie est > 0 alors le jeu continue
* si le nombre d'essaie est == 0 alors vous avez échoué

:five: DEMANDE AU JOUEUR DE DEVINER
* pour ce faire on demande au joueur de rentrer un caractère qu'il devine
```
dévine = input(str())
```
* pour éviter de prendre plus qu'un caractère on a 
```
devine[ 0 ]
```


