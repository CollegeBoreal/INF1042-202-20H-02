# :rotating_light: PROJET DE FIN DE SESSION HIVER 2020 INTRODUCTION À LA PROGRAMMATION :rotating_light:
:fire: PROJET FUN SUR LA CRÉATION DU JEU DU PENDU :fire:

:speech_balloon: EN QUOI CONSISTE CE JEU :question:

:exclamation: Le but du jeu est de trouver un mot en devinant les lettres qui le composent

:video_game: :eyes:

:point_down: :point_down: :point_down: :point_down: :point_down: :point_down: :point_down:

<img src="Capture d’écran, le 2020-04-14 à 08.45.39.png" width="580" height="341"></img>

:dash: :dash: :dash: :dash: :dash: :dash:


:x: LES DIFFÉRENTES PARTIES QUI CONSTITUENT CE JEU DE PENDU :x:

:one: CRÉATION D'UNE LISTE DE MOT :globe_with_meridians:
* avec [ ]
* ensuite pour que les mots soit choisi de manière aléatoire, on utilise le module random :slot_machine:

et ça donne 
```
import random
a = ["", "", ""]
b = random.choice(a)
```

:two: :clock1: LA GESTION DU TEMPS POUR CONTRÔLER LE FLUX D'INFORMATIONS QU'ON TRANSMET AU JOUEUR :clock130:
* Avec le module time

et ça donne
```
import time
time.sleep(le nombre de seconde)
```


:three: DÉTERMINATION DU NOMBRE D'ESSAI :1234: :ballot_box_with_check:

* Dans notre jeu le nombre d'essai correspond à la longueur du mot à trouvé

* grâce à ("len")

:four: CRÉATION D'UNE BOUCLE WHILE :loop:
* si le nombre d'essaie est > 0 alors le jeu continue
* si le nombre d'essaie est == 0 alors vous avez échoué

:five: DEMANDE AU JOUEUR DE DEVINER :pencil:
* pour ce faire on demande au joueur de rentrer un caractère qu'il devine
```
dévine = input(str())
```
* pour éviter de prendre plus qu'un caractère on a 
```
devine[ 0 ]
```


