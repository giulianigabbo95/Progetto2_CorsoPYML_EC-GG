from Utente import Utente 

FILE_STUDENTI = "studenti.csv"

class Studente(Utente):

    def init(self, nome, password, corso):
        super().__init__(nome, password, corso)
        self.corso = corso

    def modificaCorso(self, nuovo_corso):
        self.corso = nuovo_corso

    def listaStudenti(self):
        return [self.nome, self.corso]