from Utente import Utente 

import datetime

class Admin(Utente):
    
    def init(self, nome, corso):
        super().__init__("admin", "root")


    def resetStudenti(self, file_studenti, file_intervento):
        motivazione = input("Inserisci motivazione del reset: ")
        open(file_studenti, "w").close()
        with open(file_intervento, "a") as file:
            file.write(datetime.now(), "- Reset Admin - Motivo:", motivazione, "\n")
        print("Lista studenti resettata con successo.")