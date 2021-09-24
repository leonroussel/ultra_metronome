# Normalisation de la vitesse en trail

## Motivations

Pratiquant le trail, j'étais à la recherche d'un outil pouvant prédire mes temps de passage à différent point du parcours en fonction des statistiques que sont la distance, le dénivelé, la technicité du terrain, de la météo, de l'état de forme... 

Avant de pouvoir réellement créer un prédicteur, il s'agit d'abord d'étudier l'influence des paramètres sur la performance. Il vient alors l'idée de créer une vitesse normalisée que le terrain soit plat ou vallonée afin de pouvoir ensuite étudier le ralentissement et la gestion durant l'effort.

Il s'agit dans un premier temps de créer un modèle simple, et de ne pas invoquer des moyens mathématiques/statistiques important. 

## Inspirations

Cette idée n'est pas née toute seule. Je relève notamment la valeur "vitesse à plat" créé par Strava qui suit cette philosophie. Il existe également des sites internet qui propose de prévoir des temps, mais ceux-ci semblent assez obsolètes.

## Choix de la course

Pour créer un vitesse normalisée, il faut étudier un cas concret.
Il faut donc séléctionner une course avec du dénivelé (un maximum de dénivelé !), avec une distance assez longue pour avoir beaucoup d'information avec uniquement une seule course.
Il faut ensuite que l'(les)athlète(s) que l'on étudie soit le plus constant possible. (Si à chaque ravitaillement, l'athlète fait entre 5 et 60 minutes de pauses, le modèle qui s'applique sur la partie course n'a plus de sens)

Tous ces facteurs m'ont amené à étudier la course de Francois D'Haène sur l'UTMB en 2021.

Et afin d'affûter le modèle, on pourra ensuite utiliser d'autres athlètes.

## Model n°1

...