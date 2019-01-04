# Barrow

Les cartes de Barrow permettent de présenter une situation, de proposer des choix et d'associer un score en fonction des réponses choisies

Ce script permet de générer des cartes de Barrow au format html à partir d'un CSV.

Ce script nécessite l'installation de Python

Ce CSV doit :
- être séparé par des ;
- la 1° ligne doit contenir le titre, la description de la situation suivi de 2 cases avec 0
- les lignes suivantes contiennent : la question, le commentaire et nombre de points attribués à cette réponse.
Je n'ai pas encore géré les champs multilignes

Pour générer le fichier html, glisser/déposer le csv sur exec.bat