#datas / gerer les infos
from tinydb import TinyDB, Query
from salarie import Salarie

class BaseDeDonnee:
    """ Manipuler une base de donnee """
    def __init__(self, name):
        self.name = name
        self.bdd = None
        
    def get_name(self):
        return self.name
    
    def creer_bdd(self):
        self.bdd = TinyDB(f"{self.name}.json")
        
    def get_bdd(self, bdd):
        return self.bdd is not None
        

    def ajout_salarie(self):
        """ L'utilisateur ajoute un salarié """
        
        print(f"Pour ajouter un salarié, veuillez notez les informations suivantes : ")
        name = input(f"Name : ")
        competence = input(f"Compétence principale : ")
        salarie = Salarie(name,competence)
        self.bdd.insert({"Name":salarie.get_name(),"Compétence principale": salarie.get_competence()})
        

    def retourne_db(self,bdd):
        return self.bdd

