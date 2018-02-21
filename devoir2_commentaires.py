#coding : utf-8

### BONJOUR, ICI JHR ###
### Mes notes et corrections sont encore précédées de trois dièses ###

#Isoler les rangées dont l'élément 17 contient "fonds du canada pour les périodiques"

import csv

### Je commence par créer un compteur, la variable «nb», pour savoir combien de subvention ton code permet de ramasser

nb = 0

### Je vais aussi modifier légèrement le nom du fichier afin de permettre à ton code de rouler sur mon ordi

with open('../grants.csv', encoding='utf-8') as f:
	csvReader = csv.reader(f, delimiter=',')

	for row in csvReader:
		# Regarder l'element de la colonne purpose_fr

### Intéressante mise en minuscules de la chaîne de caractères dans laquelle tu vas chercher
### Ça peut solutionner certains cas où il y a une multitude d'orthographes possibles

		purp_fr = row[17].lower()

		# si c'est le fonds desiré, afficher...
		if ("fonds du canada pour les périodiques" in purp_fr):

### J'augmente mon compteur de 1

			nb += 1

### Bonne méthode pour trouver l'année.
### J'avoue que je n'y avais pas pensé!
### Ma méthode était plutôt celle-ci : annee = ligne[13][:4]
### Les deux fonctionnent bien :)

### J'ajoute aussi l'affichage de ma variable «nb»

			print("date de subvention : ", row[13].split('-')[0], row, nb)

### Ton code fonctionne bien,
### mais il ne permet malheureusement pas de trouver toutes les subventions du Fonds du Canada pour les périodiques
### Il en identifie 2494
### Or, le Fonds est aussi identifié par son acronyme dans certains cas (FCP)
### En ajoutant un «or» à ton «if», ça nous donne
### «if "fonds du canada pour les périodiques" in purp_fr or "fcp -" in purp_fr:»
### Cela t'en donne 4608 et se rapproche davantage de ce que l'on cherche. :)