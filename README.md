Tableau interactif

Tableau interactif est une application développée en Python permettant à plusieurs clients de dessiner simultanément des formes géométriques sur une page web. Les formes envoyées par le client Python sont transmises en temps réel aux tableaux connectés au serveur.

## Fonctionnalités

Dessin de points, lignes, cercles, rectangles et carrés.

Choix des coordonnées, des dimensions et de la couleur RGB des formes.

Interface web utilisant HTML et Canvas.

Communication entre le client Python et le serveur via HTTP.

Diffusion des formes en temps réel aux tableaux connectés grâce aux WebSockets.

Gestion de plusieurs connexions au tableau interactif.

## Prérequis

Python 3.

Un navigateur web récent.

Les bibliothèques Python Requests et WebSockets.

## Installation

Clonez le dépôt, puis ouvrez un terminal dans le dossier du projet :

git clone https://github.com/Leonheagle/Tableau-interactif.git
cd tableau-interactif

Créez et activez un environnement virtuel.

Sous Windows :

python -m venv .venv
.venv\Scripts\activate

Installez les dépendances :

python -m pip install -r requirements.txt

## Lancement

Ouvrez deux terminaux dans le dossier du projet et activez l'environnement virtuel dans chacun.

*Terminal 1 — Serveur :*

python server.py

Le serveur HTTP écoute sur le port 8080 et le serveur WebSocket sur le port 8765.

*Terminal 2 — Client :*

Ouvrez le fichier index.html dans un navigateur web pour afficher le tableau interactif.

ensuite dans un terminal python client.py

Suivez les instructions du client pour choisir une forme, saisir ses coordonnées (stritement positif) et définir sa couleur RGB. La forme envoyée doit apparaître sur le tableau et être diffusée aux autres tableaux connectés.

## Structure du projet

client.py : saisie des paramètres des formes et envoi des requêtes HTTP.

server.py : réception des requêtes HTTP et diffusion des formes via WebSockets.

index.html : interface web et affichage des formes sur le canvas.

requirements.txt : dépendances nécessaires au projet.

## Technologies utilisées

Python, HTTP Server, Requests, Asyncio, Threading, WebSockets, HTML et Canvas HTML5.