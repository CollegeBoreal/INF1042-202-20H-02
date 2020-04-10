# Python Automation MORTEZA

<img src="images/2.PNG" width="974" heigth="564"></img>
Dans ce scénario on va configurer tous nos éléments de réseaux avec nos python scripts en utilisant python3 installé dans nos Docker Containers afin d’ouvrir le site de collège Boréal avec notre docker de Firefox.


<img src="images/3.PNG" width="974" heigth="564"></img>
R1 est notre routeur de pont entre Internet ou notre réseau local, pour cette raison on doit configurer NAT protocole. Sans NAT nos instruments locaux ne seront pas capables de sortir de notre réseau local. 
Pour vérifier si on est bien connecté à notre serveur virtuel pour sortir de ce réseau, on utilise la commande ip address dhcp dans l’interface f0/0. Si on obtient notre adresse IP ça veut dire que l’infrastructure est prête.














<img src="images/Screen Shot 2020-04-07 at 3.10.07 PM.png" width="" heigth=""></img>

1- INSTALLATION DE LA MACHINE VIRTUELLE
Pour créer votre lab afin d'automatisation il faut installer VMware Workstation Pro dans le Windows et Vmware Fusion dans le Mac.​

Dès que l'istallation c'est finie, vous devez installer GNS3 VM pour automatiser vos instruments de réseau avev GNS3, autremen dit, ça devient le serveur de vos machines dans votre GNS3 et ça vous aide d'utiliser un grand nombre de Docker Container préparés par GNS3.​

KVM support available doit étre vrai quand vous redémarrarez votre GNS3 VM, et vous devez aussi céer un autre addapteur dans cette machine dans le mode Pond.

 
 2-Installation de GSN3
 

Télécharger la dernière version dans le site www.gns3.com

Confiquer votre GNS3 pour le lier à votre GNS VM.

Télécharger des ISOs des différents instruments pour installer dedans.

Télécharger les différents Docker Container pour les utiliser dans vos travaux.

Quand vous lancez votre GNS3, votre serveur virtuel doit être vert(allumé).

3-PRÉPARER VOTRE PYTHON:

Il faut vérifier la version de votre Python dans cmd avec la commande.

 " python –version":

Python3 est prêt pour utiliser, mais pour python version 2 vous devez importer et installer get-pip.txt, Netmiko ou Paramiko pour le rendre capable d'exécuter les programme concernat de configurer vos instruments de réseau.

Ce sont tous mis dans python3.

4-RÉDIGER VOS PROGRAMMES :
 En général, chaque programme est constitué de deux parties, la promière c'est pour arriver à la destination, la euxième c'est pour la configurer, pour cette raison:

_Il faut préparer vos programme d'une manière que votre python puisse:

_Se connecter à la destination précise, arriver dans le mode de configuration et éxécurer le reste de programme en utilisant Telnet ou SSH et Address IP de la destination dans lequel vous avez activé Telnet ou SSH.

5-VÉRIFIER LA CONNECTION DANS VOTRE LAB:
Si: 

1-vous pouvez obtenir Address IP dans votre lab de votre machine virtuelle qui est votre serveur​

2- si vous pouvez pinguer vos instruments de cmd de votre ordinateur

3- si votre python est prêt

C'est le moment d'exécuter vos programmes et regardrer comment ça va simplifier la vie pour les informaticiens quui ont leurs programmes en mains pour configurer les instruments en cliquant un seul boutton.
 

## :one: Installation

```
PS > pip --version
```

<img src="images/Picture1.png" width="974" heigth="193"></img>

```
PS > python -m pip install -u pip
```
<img src="images/Picture2.png" width="974" heigth="193"></img>

```
PS > pip install netmiko
PS > pip install paramiko
```

<img src="images/Picture3.png" width="918" heigth="664"></img>

## :two: Execution

C’est mon Ubunto Docker Container qui a reçu son adresse IP de DHCP :

<img src="images/Picture4.png" width="974" heigth="564"></img>
