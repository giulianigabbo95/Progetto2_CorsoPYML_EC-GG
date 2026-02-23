from Utente import Utente 

import datetime

class Admin(Utente):

    def init(self, nome, corso):
        super().__init__("admin", "root")

    def menuAdmin(self):
        while True:
            print("Menu Admin")
            print("0. Logout")
            print("1. Reset Studenti")

            scelta = input("Scelta: ")

            match scelta:
                case "0":
                    break
                case "1":
                    self.resetStudenti("studenti.csv", "intervento_utente.txt")
                case _:
                    print("Scelta non valida.")


    def resetStudenti(self, file_studenti, file_intervento):
        motivazione = input("Inserisci motivazione del reset: ")
        with open(file_studenti, "w", newline=""): # w = cancella tutto
            pass
        with open(file_intervento, "a") as log: # a = aggiunge al log
            log.write(datetime.now(), "- Reset Admin - Motivo:", motivazione, "\n")
        print("Lista studenti resettata con successo.")