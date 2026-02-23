# =========================
# CLASSE UTENTE
# =========================
import Studente
import os
import csv

class Utente:
    def __init__(self, nome, password):
        self.nome = nome
        self.password = password

    def menu(self):
        while True:
            print("\n1. Aggiungi Studente")
            print("2. Modifica Studente")
            print("3. Stampa Aula")
            print("4. Logout")

            scelta = input("Scelta: ")

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

    # =========================
    # METODI STUDENTI
    # =========================

    def aggiungi_studente(self):
        nome = input("Nome studente: ")
        corso = input("Corso: ")

        studente = Studente(nome, corso)

        # a = aggiunge in coda
        with open("studenti.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(studente.to_list())

        print("Studente aggiunto.")

    def modifica_studente(self):
        nome_mod = input("Nome studente da modificare: ")

        if not os.path.exists("studenti.csv"):
            print("Nessun file studenti presente.")
            return

        studenti = []

        # r = lettura
        with open("studenti.csv", "r") as file:
            reader = csv.reader(file)
            for riga in reader:
                studenti.append(Studente(riga[0], riga[1]))

        trovato = False

        for studente in studenti:
            if studente.nome == nome_mod:
                studente.corso = input("Nuovo corso: ")
                trovato = True

        if trovato:
            # w = sovrascrive
            with open("studenti.csv", "w", newline="") as file:
                writer = csv.writer(file)
                for studente in studenti:
                    writer.writerow(studente.to_list())

            print("Studente modificato.")
        else:
            print("Studente non trovato.")

    def stampa_aula(self):
        if not os.path.exists("studenti.csv"):
            print("Nessuno studente presente.")
            return

        studenti = []

        # r = lettura
        with open("studenti.csv", "r") as file:
            reader = csv.reader(file)
            for riga in reader:
                studenti.append(Studente(riga[0], riga[1]))

        # ordinamento per corso
        studenti.sort(key=lambda s: s.corso)

        print("\n--- LISTA AULA ORDINATA PER CORSO ---")
        for studente in studenti:
            print(studente)