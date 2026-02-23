import os

from gestione_Utente import Utente

# CLASSE ADMIN 

class Admin(Utente):
    def __init__(self):
        super().__init__("admin", "admin123")

    def reset_lista(self):
        motivo = input("Inserisci motivazione reset: ")

        with open("studenti.csv", "w", newline=""):
            pass

        with open("intervento_utente.txt", "a") as log:
            log.write(f"Reset effettuato da ADMIN. Motivo: {motivo}\n")

        print("Lista studenti resettata.")

        def menu(self):
            while True:
                print("\n1. Aggiungi Studente")
                print("2. Modifica Studente")
                print("3. Stampa Aula")
                print("4. Reset Lista Studenti")
                print("5. Logout")

                scelta = input("Scelta: ")

                if scelta == "1":
                    self.aggiungi_studente()
                elif scelta == "2":
                    self.modifica_studente()
                elif scelta == "3":
                    self.stampa_aula()
                elif scelta == "4":
                    self.reset_lista()
                elif scelta == "5":
                    break
                else:
                    print("Scelta non valida.")