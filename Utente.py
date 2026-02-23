from Studente import Studente

import os
import csv

class Utente:

    def init(self, nome, password):
        self.nome = nome
        self.__password = password


    def menuUtente(self):
        while True:
            print("Menu Utente")
            print("1. Aggiungi Studente")
            print("2. Modifica Studente")
            print("3. Stampa Aula")
            print("0. Logout")

            scelta = input("Scelta: ")

            match scelta:
                case "0":
                    break
                case "1":
                    self.aggiungiStudente()
                case "2":
                    self.modificaStudente()
                case "3":
                    self.stampaAula()
                case _:
                    print("Scelta non valida.")

    def registraUtente(self, file_credenziali):
        with open(file_credenziali, "a") as file:
            file.write(self.nome, ",", self.__password, "\n")

    def loginUtente(self, file_credenziali):
        try:
            with open(file_credenziali, "r") as cred:
                righe = cred.readlines()
            for riga in righe:
                n, p = riga.strip().split(",")
                if n == self.nome and p == self.__password:
                    return True
        except FileNotFoundError:
            return False
        return False

    def aggiungiStudente(self):
        nome = input("Nome studente: ")
        corso = input("Corso: ")
        studente = Studente(nome, corso)
        with open("studenti.csv", "a", newline="") as file: # a = aggiunge in coda
            writer = csv.writer(file)
            writer.writerow(studente.to_list())
        print("Studente aggiunto.")

    def modificaStudente(self):
        nome_mod = input("Nome studente da modificare: ")
        if not os.path.exists("studenti.csv"):
            print("Nessun file studenti presente.")
            return
        studenti = []
        with open("studenti.csv", "r") as file: # r = lettura
            reader = csv.reader(file)
        for riga in reader:
            studenti.append(Studente(riga[0], riga[1]))
        trovato = False
        for studente in studenti:
            if studente.nome == nome_mod:
                studente.corso = input("Nuovo corso: ")
                trovato = True
        if trovato:
            with open("studenti.csv", "w", newline="") as file: # w = sovrascrive
                writer = csv.writer(file)
            for studente in studenti:
                writer.writerow(studente.to_list())
            print("Studente modificato.")
        else:
            print("Studente non trovato.")

    def stampaAula(self):
        if not os.path.exists("studenti.csv"):
            print("Nessuno studente presente.")
            return
        studenti = []
        with open("studenti.csv", "r") as file: # r = lettura
            reader = csv.reader(file)
        for riga in reader:
            studenti.append(Studente(riga[0], riga[1]))
        studenti.sort(key =lambda s: s.corso)
        print("Lista per Corso")
        for studente in studenti:
            print(studente)

    def controllaPassword(self, password):
        if self._password == password:
            return True
        else:
            return False


    def get_password(self):
        return self._password