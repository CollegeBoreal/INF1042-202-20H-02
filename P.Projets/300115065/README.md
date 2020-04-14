# ✨Mon projet "Morse Code Translator in Python"✨

## 📌Vue generale du jeu:

Le code Morse (du nom de Samuel Morse, son inventeur) est un code télégraphique utilisant un alphabet conventionnel fait de traits et de points, et, quant au son, de longues et de brèves.
Depuis le 1er février 1999, le code Morse a été abandonné pour les communications maritimes au profit d'un système satellitaire.

Cette technique est très simple. Chaque alphabet en anglais signifie une série de ".",",","/","-". Il suffit de crypter le message du message aux symboles et de décrypter des symboles à l'anglais.

## 📌Mise en œuvre
```
Python fournit une structure de données appelée dictionnaire qui stocke les informations sous la forme de paires clé-valeur, ce qui est très pratique pour mettre en œuvre un chiffrement tel que le code morse. Nous pouvons sauvegarder le tableau du code morse dans un dictionnaire où (paires clé-valeur) => (Caractères anglais-Code morse). Le texte en clair (caractères anglais) prend la place des clés et le texte chiffré (code morse) forme les valeurs des clés correspondantes. Les valeurs des clés sont accessibles à partir du dictionnaire de la même manière que nous accédons aux valeurs d'un tableau à travers leur index et vice versa.
```

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
Le message est python program
Le résultat est ['.--.', '-.--', '-', '....', '---', '-.', ' ', '.--.', '.-.', '---', '--.', '.-.', '.-', '--']
```

* Les impulsions longues et courtes peuvent être des signaux électriques, sonores, ou encore lumineux. Tout format de télécommunication est possible.


* Par convention, à l'écrit, séparer les caractères d'un espace, et chaque mot avec un double quotes '' Parfois les caractères sont séparés par un single quote '

## ✨Algorithme

## 📌Comment décoder le Code Morse ? (Principe de déchiffrement)
Le déchiffrement/traduction Morse en français (ou anglais) utilise le même alphabet que le chiffrement.

## 📌Comment reconnaitre le code Morse ?

Le message est composé principalement de points et de tirets (ou parfois, de toute autre paire de caractères).

Le code morse est surtout auditif, un bruit composé de sons longs et court (comme des bips) c'est aussi du code Morse.
```
Exemple : bip biiiip bip = .-.
```

Idem, certains utilisent des syllabes en I ou E pour court et A ou O pour long.
```
Exemple : TATITA = -.- (long, court, long)
```
## 📌Comment écrire le code Morse ?

Il n'y a pas vraiment de bonne facon ou de méthode officielle d'écrire du Morse. Il s'agit avant tout d'un code sonore. Visuellement le code Morse écrit devrait être disposé sur une même ligne. L'informatique a pourtant du mal à l'écrire avec les tirets - ou _ et les points . qui ne sont pas au même niveau.

L'essentiel est de bien différencier les caractères : exemple ▄ (court) et ▄▄▄▄ (long).

## 📌Comment déchiffrer du code Morse audio MP3 ?

Ecouter le message et taper en même temps sur le clavier . (point) pour un son court/aigu et - (tiret) pour un son long/grave.

## 📌Comment déchiffrer le code Morse sans espace ?

Le déchiffrement du Morse sans séparateur est très difficile, un séparateur est presque indispensable, les possibilités sont exponentielles. dCode propose des outils, notamment une attaque par brute-force ou par dictionnaire.

Exemple : -.-. (4 caractères) peut vouloir dire 8 choses différentes : C ou KE ou NN ou NTE ou TR ou TAE ou TEN ou TETE

## 📌Comment apprendre l'alphabet Morse par des moyens mnémotechniques ?

Il existe plusieurs méthodes. La méthode des consonances permet de retenir les 26 codes en apprenant par coeur 26 mots de l'alphabet. Chaque syllabe est alors convertie en un point ou un trait selon sa consonance. Les syllabes en O sont transformées en trait long, alors que les autres sont des tirets courts.

Exemple : PSYCHOLOGIE, commence par un P, et contient 2 syllabes en O, P est donc codé en Morse .--.

## 📌Comment envoyer un SOS en Morse ?
SOS se code ... --- ... (3 courts, 3 longs, 3 courts)
