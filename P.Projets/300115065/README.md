# ✨Mon projet "Morse Code Translator in Python"✨

## 📌Vue generale du jeu:

Le traducteur de code Morse est utilisé en cryptographie. Il est nommé par Samuel F. B. Morse. Par cette technique, nous convertissons un message en une série de points, de virgules, de "-", de "/".

Cette technique est très simple. Chaque alphabet en anglais signifie une série de ".",",","/","-". Il suffit de crypter le message du message aux symboles et de décrypter des symboles à l'anglais.

### Le dictionnaire est donné ci-dessous:

```
'A':'.-', 'B':'-...',
'C':'-.-.', 'D':'-..', 'E':'.',
'F':'..-.', 'G':'--.', 'H':'....',
'I':'..', 'J':'.---', 'K':'-.-',
'L':'.-..', 'M':'--', 'N':'-.',
'O':'---', 'P':'.--.', 'Q':'--.-',
'R':'.-.', 'S':'...', 'T':'-',
'U':'..-', 'V':'...-', 'W':'.--',
'X':'-..-', 'Y':'-.--', 'Z':'--..',
'1':'.----', '2':'..---', '3':'...--',
'4':'....-', '5':'.....', '6':'-....',
'7':'--...', '8':'---..', '9':'----.',
'0':'-----', ', ':'--..--', '.':'.-.-.-',
'?':'..--..', '/':'-..-.', '-':'-....-',
'(':'-.--.', ')':'-.--.-'}
```

### Exemple
```
Le message est PYTHON-PROGRAMME
Le résultat est... -.-- - .... --- -. -....- .--. .-. --- --. .-. .- --
```

## 📌Algorithme

### Cryptage

```
Etape 1 : A partir d'une chaîne de caractères, nous extrayons d'abord chaque lettre du mot et la faisons correspondre avec le dictionnaire de Morse, puis nous considérons le code correspondant à la lettre.
Étape 2 : L'étape suivante consiste à stocker le code dans une variable. Et nous devons suivre qu'un espace doit être maintenu entre chaque code Morse.
Étape 3 : Deux espaces doivent être maintenus entre chaque mot.
```

### Décryptage
```
Étape 1 : Nous commençons par ajouter un espace à la fin de la chaîne.
Étape 2 : Nous parcourons maintenant chaque lettre du message jusqu'à ce que l'espace ne soit pas rencontré.
Etape 3 : Lorsque nous obtenons un espace, nous vérifions avec le dictionnaire de morse et nous le stockons dans une variable.
Etape 4 : Lorsque nous obtenons 2 espaces consécutifs, nous ajoutons un autre espace à notre variable contenant la chaîne décodée.
Étape 5 : Lorsque nous obtenons le dernier espace du message, cela signifie que c'est la dernière lettre du générateur de code Morse.
```


