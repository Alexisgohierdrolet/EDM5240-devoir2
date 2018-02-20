#coding : utf-8

#Isoler les rangées dont l'élément 17 contient "fonds du canada pour les périodiques"


import csv

with open('grants.csv', encoding='utf-8') as f:
    csvReader = csv.reader(f, delimiter=',')

    for row in csvReader:
        # Regarder l'element de la colonne purpose_fr
        purp_fr = row[17].lower()

        # si c'est le fonds desiré, afficher...
        if ("fonds du canada pour les périodiques" in purp_fr):
            print("date de subvention : ", row[13].split('-')[0], row)

