import os
#import csv

# =========================
# CLASSE STUDENTE
# =========================

class Studente:
    def __init__(self, nome, corso):
        self.nome = nome
        self.corso = corso

    def to_list(self):
        return [self.nome, self.corso]

    def __str__(self):
        return f"Nome: {self.nome} - Corso: {self.corso}"


# =========================
# CLASSE UTENTE
# =========================

class Utente:
    def __init__(self, nome, password):
        self.nome = nome
        self.password = password

    def menu(self):
        while True:
            print("\n1. Inserisci/Modifica Studenti")
            print("2. Stampa Aula")
            print("3. Logout")
            scelta = input("Scelta: ")

            if scelta == "1":
                gestione_studenti()
            elif scelta == "2":
                stampa_aula()
            elif scelta == "3":
                break
            else:
                print("Scelta non valida.")


# =========================
# CLASSE ADMIN (FIGLIA)
# =========================

class Admin(Utente):
    def __init__(self):
        super().__init__()

    def menu(self):
        while True:
            print("\n1. Inserisci/Modifica Studenti")
            print("2. Stampa Aula")
            print("3. Reset Lista Studenti")
            print("4. Logout")
            scelta = input("Scelta: ")

            if scelta == "1":
                gestione_studenti()
            elif scelta == "2":
                stampa_aula()
            elif scelta == "3":
                self.reset_lista()
            elif scelta == "4":
                break
            else:
                print("Scelta non valida.")

    def reset_lista(self):
        motivo = input("Inserisci motivazione reset: ")

        # w = sovrascrive completamente il file studenti
        with open("studenti.csv", "w", newline="") as file:
            pass

        # a = aggiunge log nel file intervento
        with open("intervento_utente.txt", "a") as log:
            log.write(f"Reset effettuato da ADMIN. Motivo: {motivo}\n")

        print("Lista studenti resettata.")


# =========================
# FUNZIONI SISTEMA
# =========================

def registrazione():
    nome = input("Inserisci nome: ")
    password = input("Inserisci password: ")

    # a = aggiunge nuova riga
    with open("credenziali.txt", "a") as file:
        file.write(f"{nome},{password}\n")

    print("Registrazione completata.")


def login():
    nome = input("Nome: ")
    password = input("Password: ")

    # Accesso Admin hardcoded
    if nome == "admin" and password == "admin123":
        print("Accesso Admin effettuato.")
        return Admin()

    if os.path.exists("credenziali.txt"):
        # r = lettura file
        with open("credenziali.txt", "r") as file:
            for riga in file:
                user, pwd = riga.strip().split(",")
                if user == nome and pwd == password:
                    print("Login effettuato.")
                    return Utente(nome, password)

    print("Credenziali errate.")
    return None


# =========================
# GESTIONE STUDENTI
# =========================

def gestione_studenti():
    print("\n1. Aggiungi Studente")
    print("2. Modifica Studente")
    scelta = input("Scelta: ")

    if scelta == "1":
        nome = input("Nome studente: ")
        corso = input("Corso: ")

        studente = Studente(nome, corso)

        # a = aggiunta in coda
        with open("studenti.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(studente.to_list())

        print("Studente aggiunto.")

    elif scelta == "2":
        nome_mod = input("Nome studente da modificare: ")
        studenti = []

        if os.path.exists("studenti.csv"):

            # r = lettura
            with open("studenti.csv", "r") as file:
                reader = csv.reader(file)
                for riga in reader:
                    studenti.append(Studente(riga[0], riga[1]))

            trovato = False

            for studente in studenti:
                if studente.nome == nome_mod:
                    nuovo_corso = input("Nuovo corso: ")
                    studente.corso = nuovo_corso
                    trovato = True

            if trovato:
                # w = sovrascrive completamente il file
                with open("studenti.csv", "w", newline="") as file:
                    writer = csv.writer(file)
                    for studente in studenti:
                        writer.writerow(studente.to_list())

                print("Studente modificato.")
            else:
                print("Studente non trovato.")
        else:
            print("Nessun file studenti presente.")


# =========================
# STAMPA AULA
# =========================

def stampa_aula():
    studenti = []

    if os.path.exists("studenti.csv"):

        # r = lettura
        with open("studenti.csv", "r") as file:
            reader = csv.reader(file)
            for riga in reader:
                studenti.append(Studente(riga[0], riga[1]))

        # Ordinamento per corso
        studenti.sort(key=lambda s: s.corso)

        print("\n--- LISTA AULA ORDINATA PER CORSO ---")
        for studente in studenti:
            print(studente)
    else:
        print("Nessuno studente presente.")


# =========================
# MAIN
# =========================

def main():
    while True:
        print("\n1. Registrazione")
        print("2. Login")
        print("3. Esci")
        scelta = input("Scelta: ")

        if scelta == "1":
            registrazione()
        elif scelta == "2":
            utente = login()
            if utente:
                utente.menu()
        elif scelta == "3":
            break
        else:
            print("Scelta non valida.")


if __name__ == "__main__":
    main()