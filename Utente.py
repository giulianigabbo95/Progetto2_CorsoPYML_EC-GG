from Studente import Studente

import os
import csv

FILE_CREDENZIALI = "credenziali.txt"
FILE_STUDENTI = "studenti.csv"


class Utente:

    def init(self, nome, password):
        self.nome = nome
        self.__password = password


    def menuUtente(self):
        while True:
            print("Menu Utente")
            print("0. Logout")
            print("1. Aggiungi Studente")
            print("2. Modifica Studente")
            print("3. Stampa Aula")

            scelta = input("Scelta: ")

            match scelta:
                case "0":
                    break
                case "1":
                    self.aggiungiStudente(FILE_STUDENTI)
                case "2":
                    self.modificaStudente(FILE_STUDENTI)
                case "3":
                    self.stampaAula(FILE_STUDENTI)
                case _:
                    print("Scelta non valida.")

    def registraUtente(self, file_credenziali):
        with open(file_credenziali, "a") as file:
            if self.nome in file_credenziali:
                return False 
            file.write(self.nome, ",", self.__password, "\n")
            return True

    def loginUtente(self, file_credenziali):
        try:
            with open(file_credenziali, "r") as cred:
                righe = cred.readlines()
            for riga in righe:
                n, p = riga.strip().split(",")
                if n == self.nome and p == self.__password:
                    return True
                else:
                    print("Nome o Password Errati!")
        except FileNotFoundError:
            return False
        return False

    def aggiungiStudente(self, file_studenti):
        nome = input("Nome studente: ")
        corso = input("Corso: ")
        studente = Studente(nome, corso)
        with open(file_studenti, "a", newline="") as file: # a = aggiunge in coda
            writer = csv.writer(file)
            writer.writerow(studente.to_list())
        print("Studente aggiunto.")

    def modificaStudente(self, file_studenti):
        nome_mod = input("Nome studente da modificare: ")
        if not os.path.exists(file_studenti):
            print("Nessun file studenti presente.")
            return
        studenti = []
        with open(file_studenti, "r") as file: # r = lettura
            reader = csv.reader(file)
        for riga in reader:
            studenti.append(Studente(riga[0], riga[1]))
        trovato = False
        for studente in studenti:
            if studente.nome == nome_mod:
                studente.corso = input("Nuovo corso: ")
                trovato = True
        if trovato:
            with open(file_studenti, "w", newline="") as file: # w = sovrascrive
                writer = csv.writer(file)
            for studente in studenti:
                writer.writerow(studente.to_list())
            print("Studente modificato.")
        else:
            print("Studente non trovato.")

    def stampaAula(self, file_studenti):
        if not os.path.exists(file_studenti):
            print("Nessuno studente presente.")
            return
        studenti = []
        with open(file_studenti, "r") as file: # r = lettura
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