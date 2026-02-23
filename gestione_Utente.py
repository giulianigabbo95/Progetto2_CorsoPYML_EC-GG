# =========================
# CLASSE UTENTE
# =========================
import os
from gestione_Studente import Studente

class Utente:
    def __init__(self, nome, password):
        self.nome = nome
        self.password = password

    # MENU PRINCIPALE utente
    def menu(self):
        while True:
            print("\n--- MENU UTENTE ---")
            print("1. Aggiungi Studente")
            print("2. Modifica Studente")
            print("3. Stampa Aula")
            print("4. Logout")

            scelta = input("Scelta: ").strip()

            if scelta == "1":
                self.aggiungi_studente()
            elif scelta == "2":
                self.modifica_studente()
            elif scelta == "3":
                self.stampa_aula()
            elif scelta == "4":
                break
            else:
                print("Scelta non valida.")

    # AGGIUNGI STUDENTE
    def aggiungi_studente(self):
        nome = input("Nome studente: ").strip()
        corso = input("Corso: ").strip()

        if not nome or not corso:
            print("Nome e corso obbligatori.")
            return

        studente = Studente(nome, corso)
        file_path = os.path.join(os.path.dirname(__file__), "studenti.csv")

        
        with open(file_path, "a", encoding="utf-8") as f:
            f.write(f"{studente.nome},{studente.corso}\n")

        print("Studente aggiunto correttamente!")

    # MODIFICA STUDENTE
    def modifica_studente(self):
        nome_mod = input("Nome studente da modificare: ").strip()
        file_path = os.path.join(os.path.dirname(__file__), "studenti.csv")

        if not os.path.exists(file_path):
            print("Nessun file studenti presente.")
            return


        studenti = []
        with open(file_path, "r", encoding="utf-8") as f:
            for riga in f:
                riga = riga.strip()
                if riga:
                    parti = riga.split(",", 1)
                    if len(parti) == 2:
                        studenti.append(Studente(parti[0], parti[1]))

        trovato = False
        for studente in studenti:
            if studente.nome.lower() == nome_mod.lower():
                nuovo_corso = input("Nuovo corso: ").strip()
                if nuovo_corso:
                    studente.corso = nuovo_corso
                    trovato = True

        if trovato:
            with open(file_path, "w", encoding="utf-8") as f:
                for s in studenti:
                    f.write(f"{s.nome},{s.corso}\n")
            print("Studente modificato.")
        else:
            print("Studente non trovato.")

    # STAMPA AULA
    def stampa_aula(self):
        file_path = os.path.join(os.path.dirname(__file__), "studenti.csv")

        if not os.path.exists(file_path):
            print("Nessuno studente presente.")
            return

        #legge file studenti.csv e salva in lista poi alla fine stampa
        studenti = []
        with open(file_path, "r", encoding="utf-8") as f:
            for riga in f:
                riga = riga.strip()
                if riga:
                    parti = riga.split(",", 1)
                    if len(parti) == 2:
                        studenti.append(Studente(parti[0], parti[1]))

        if not studenti:
            print("Nessuno studente presente.")
            return

        # ordina per corso
        studenti.sort(key=lambda s: s.corso)

        print("\n--- LISTA AULA ORDINATA PER CORSO ---")
        for s in studenti:
            print(s)