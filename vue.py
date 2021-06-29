# affichages / mise en page / template
from modele import BaseDeDonnee



def decorer(func):
    print(f"\n \n ------------------------------------------------------- \n \n")
    


def afficher_salarie(bdd):
    """ afficher les salariés d'une base de donnée """
    u = 1
    for i in bdd:
        u += 1
        print(f"voici le salariés n°{u - 1} : {i}") 
    
# afficher_salarie(retourne_db)

