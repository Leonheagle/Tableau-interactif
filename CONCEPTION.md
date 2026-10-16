# Conception du tableau interactif

Dans ce fichier Markdown, j'explique comment j'ai conceptualisé le tableau interactif et comment j'ai utilisé l'IA dans ce but.

**## Choix de conception**

Le projet est réalisé en trois grandes parties : la partie serveur Python, la partie client Python et la partie web.

Au début de ma conception, je me suis orienté vers une solution utilisant une bibliothèque permettant de gérer à la fois les requêtes HTTP et les connexions WebSocket. J'ai ensuite choisi de séparer ces deux mécanismes afin d'utiliser des outils plus proches de ceux étudiés en cours.

Dans ma version finale, le serveur Python utilise `http.server` pour recevoir les requêtes HTTP envoyées par le client et `websockets` pour communiquer avec les tableaux web connectés. Le serveur reçoit les informations d'une forme, puis les transmet aux clients connectés afin qu'ils puissent l'afficher en temps réel.

Le client Python utilise `requests` pour envoyer les formes au serveur. Il permet à l'utilisateur de choisir le type de forme, ses coordonnées, ses dimensions et sa couleur RGB.

J'utilise HTML, CSS et JavaScript pour réaliser l'interface web. L'élément `canvas` permet de dessiner les différentes formes reçues par WebSocket.

Cette séparation permet de distinguer la saisie des formes, leur transmission par le serveur et leur affichage dans le navigateur.

**## Utilisation de l'intelligence artificielle**

J'ai utilisé une intelligence artificielle conversationnelle comme outil d'accompagnement pendant le développement. Mon objectif n'était pas uniquement d'obtenir un code fonctionnel, mais aussi de comprendre les mécanismes utilisés et les choix possibles.

Le travail s'est déroulé de manière progressive :

- **Compréhension du code :** demande d'explications sur les fonctions Python, les imports, les requêtes HTTP et les connexions WebSocket.

- **Conception de l'application :** réflexion sur la séparation entre le client Python, le serveur et l'interface web, ainsi que sur le rôle de chaque composant.

- **Choix des bibliothèques :** adaptation de la conception pour utiliser `http.server`, `requests` et `websockets`, en privilégiant les outils étudiés en cours.

- **Résolution des problèmes :** analyse des erreurs rencontrées et recherche de corrections adaptées au fonctionnement du projet, notamment pour faire communiquer les serveurs HTTP et WebSocket.

- **Documentation :** aide à la rédaction du `README.md` et du présent fichier afin d'expliquer le fonctionnement du projet et les choix de conception.

J'ai privilégié une approche itérative : je soumettais une question ou un problème précis, j'examinais les explications et les propositions, puis je les confrontais au fonctionnement de mon application. Cette méthode m'a permis de progresser par étapes plutôt que de construire l'ensemble du projet en une seule fois.

L'IA m'a notamment aidé à écrire et à relier les différentes parties du code, ainsi qu'à comprendre comment transmettre les formes du client Python jusqu'au navigateur.

L'IA a donc servi d'assistant technique et pédagogique. Les choix de conception ont été discutés au fil du développement, en tenant compte des objectifs du projet, des contraintes du sujet et de mon niveau de compréhension.