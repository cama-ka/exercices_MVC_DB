from controleur import ajout
from modele import BaseDeDonnee
from vue import afficher_salarie


bd1 = BaseDeDonnee("salaries")
# Initialisation d'un objet base de donnée d'après la classe BaseDeDonnee qui contiendra les salariés

bd1.creer_bdd()
# création d'un fichier json où seront stocké les informations de la base de donnee

ajout("Salarié", bd1.ajout_salarie)
# ajout d'une information 


afficher_salarie(bd1.bdd)

