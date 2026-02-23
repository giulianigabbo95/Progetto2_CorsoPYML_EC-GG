from Utente import Utente 

FILE_STUDENTI = "studenti.csv"

class Studente(Utente):
    
    def init(self, nome, password, corso):
        super().__init__(nome, password, corso)
        self.corso = corso

    
    def set_corso(self, nuovo_corso):
        self.corso = nuovo_corso