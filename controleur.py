#faire fonctionner le bazar
from modele import BaseDeDonnee

    
    
def ajout(element, func1):
    """ Ajoute un élément à une base de donnée """
    while True:
        print(f"Voulez-vous ajouter {element} ?")
        reponse = input(f"Répondez par oui ou non:" )
        try:
            if reponse == "Oui" or reponse == "oui":
                func1()
                continue
            else:
                print(f"Vous ne souhaitez pas ajouter un nouveau salarié")
                break
        except ValueError:
            print(f"Une erreur s'est glissé dns votre réponse.")
            break
    
    
    
# ajout("salarié", ajout_salarie,database_salaries)