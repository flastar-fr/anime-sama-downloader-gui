# Anime Sama Downloader GUI
## Description
Ce projet adapte une version CLI pour avoir un outil capable de tourner sur un serveur en continue.

Il permet de télécharger des épisodes d'anime depuis Anime Sama, que ce soit épisode par épisode ou saison par saison.
Un futur support pour scan est prévu.
Il permet également de programmer le télécharger d'anime en cours.

## Lancement
Via ``uv`` sur Windows :
````
$env:PYTHONPATH="." ; uv run python -m gui

uv run -m src.gui
````

Via ``Docker`` :
````
docker run --rm `
  -e APP_HOST="0.0.0.0" `
  -e APP_PORT=8080 `
  -e APP_RELOAD="false" `
  -e TZ="Europe/Paris" `
  -p 8080:8080 `
  flastar/anime-sama-downloader-gui
````

N'hésitez pas à rajouter un volume également.

Pour accéder à l'interface web il faut alors utiliser l'adresse IP du serveur et le port sélectionné (8000 par défaut).

## Utilisation de l'IA
- Quasi totalité du frontend réalisé par l'IA
- 50-60% du backend par IA (chaque fonction individuellement, la structure a bien été réalisée par un humain)

## Disclaimer
Cet outil est à but éducatif et n'est pas voué à être utilisé.
Respectez les lois locales en vigueur chez vous.
Utilisez le façon responsable pour être en accord avec les termes du site anime-sama.pw.

## Création du projet
Ce projet est un fork.

Le repo original accessible [ici](https://github.com/SertraFurr/Anime-Sama-Downloader) 
contient une CLI permettant de télécharger un anime / scan et pouvant être retrouvée dans la branche "old".

Ce projet est une version GUI faite pour tourner en continue sur un serveur accessible via une interface web.
