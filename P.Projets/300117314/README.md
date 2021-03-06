# Python Automation MORTEZA

<img src="images/2.PNG" width="974" heigth="564"></img>
Dans ce scénario on va configurer tous nos éléments de réseaux avec nos python scripts en utilisant python3 installé dans nos Docker Containers afin d’ouvrir le site de collège Boréal avec notre docker de Firefox.


<img src="images/3.PNG" width="974" heigth="564"></img>
R1 est notre routeur de pont entre Internet ou notre réseau local, pour cette raison on doit configurer NAT protocole. Sans NAT nos instruments locaux ne seront pas capables de sortir de notre réseau local. 
Pour vérifier si on est bien connecté à notre serveur virtuel pour sortir de ce réseau, on utilise la commande ip address dhcp dans l’interface f0/0. Si on obtient notre adresse IP ça veut dire que l’infrastructure est prête.

<img src="images/4.PNG" width="974" heigth="564"></img>
Ici vous pouvez vérifier qu’on a reçu notre adresse IP. 192.168.122.27. Nos python scripts configurent automatiquement ce routeur en utilisant cette adresse IP. 
Maintenant on va vérifier est-ce que notre Python Docker est connecté à notre serveur ou non.
Dans la photo suivante : 
Si notre Docker reçoit son adresse IP automatiquement par protocole de DHCP, ça nous assure qu’il est bien connecté. On peut aussi vérifier la version de notre python. En exécutant le commande ls vous pouvez voir les dossiers on a créés pour sauvegarder nos scripts dans ce Docker, et avec la commande de nano (nom de ce dossier) on peut voir son contenu.
Ici on va configurer DHCP,EIGRP et NAT aves ces scripts.
<img src="images/5.PNG" width="974" heigth="564"></img>


<img src="images/6.PNG" width="974" heigth="564"></img>
Avec ce script on va créer une piscine pour notre Docker connecté à l’interface f2/0 de R1.
<img src="images/7.PNG" width="974" heigth="564"></img>
Ici on va configurer notre EIGRP pour lier ce routeur avec les autre éléments de notre réseau.
<img src="images/8.PNG" width="974" heigth="564"></img>
NAT protocole pour qu’on puisse sortir de notre réseau local.
# Exécuter nos scripts
 
<img src="images/9.PNG" width="974" heigth="564"></img>
Dans cette photo le résultat de ces configurations se sont affichés dans notre Docker, et aussi on peut vérifier que dans R1 DHCP est configuré.

<img src="images/10.PNG" width="974" heigth="564"></img>
Et ici dans R1, EIGRP100, et NAT sont configurés avec nos python scripts.

<img src="images/11.PNG" width="974" heigth="564"></img>

Maintenant on démarre notre Python Docker3, connecté au routeur R2 et il reçoit adresse IP de POOl que vient de créer dans R1, on vérifie nos scripts dedans avec la commande ls. Pour configurer R2, on l’allume, on donne une adresse IP a l’intrerface f0/0 pour y arriver avec Telnet, on écrit IP ROUTE statique pour avoir connexion entre notre Docker de network 192.168.2.0 et ce routeur. Et on configure Telnet dans ce R2.

<img src="images/12.PNG" width="974" heigth="564"></img>
Avec ce script on configure notre routing protocole(EIGRP).
<img src="images/14.PNG" width="974" heigth="564"></img>
Et avec ce script on va configurer DHCP dans ce routeur pour notre utilisateur qui sont connectés à l’interface f1/0 qui reçoit son adresse IP de ce script(192.168.4.1).



# Exécuter nos scripts
<img src="images/15.PNG" width="974" heigth="564"></img>
<img src="images/16.PNG" width="974" heigth="564"></img>
<img src="images/17.PNG" width="974" heigth="564"></img>
Dans ces photos vous pouvez vérifier vos configurations. Votre DHCP pool, EIGRP et vos interfaces.

Maintenant c’est le moment re démarrer votre Firefox. 
On l’allume, on fait commande Ifconfig pour vérifier notre adresse IP.(192.168.4.2)

<img src="images/18.PNG" width="974" heigth="564"></img>

Et à la fin, WWW.COLLEGEBOREAL.CA 
<img src="images/19.PNG" width="974" heigth="564"></img>

Merci de votre attention.



