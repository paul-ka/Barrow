# Barrow

Les cartes de Barrow permettent de pr�senter une situation, de proposer des choix et d'associer un score en fonction des r�ponses choisies

Ce script permet de g�n�rer des cartes de Barrow au format html � partir d'un CSV.

Ce script n�cessite l'installation de Python

Ce CSV doit :
- �tre s�par� par des ;
- la 1� ligne doit contenir le titre, la description de la situation suivi de 2 cases avec 0
- les lignes suivantes contiennent : la question, le commentaire et nombre de points attribu�s � cette r�ponse.
Je n'ai pas encore g�r� les champs multilignes

Pour g�n�rer le fichier html, glisser/d�poser le csv sur exec.bat