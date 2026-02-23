
import os
from gestione_Utente import Utente
from  gestione_Admin import Admin
from gestione_Studente import Studente


# REGISTRAZIONE
def registrazione():
    nome = input("Inserisci nome: ")
    password = input("Inserisci password: ")

    with open("credenziali.txt", "a") as file:
        file.write(f"{nome},{password}\n")

    print("Registrazione completata.")

## LOGIN
def login(): 
    nome = input("Nome: ")
    password = input("Password: ")

    if nome == "admin" and password == "admin123":
        print("Accesso Admin effettuato.")
        return Admin()

    if os.path.exists("credenziali.txt"):
        with open("credenziali.txt", "r") as file:
            for riga in file:
                user, pwd = riga.strip().split(",")
                if user == nome and pwd == password:
                    print("Login effettuato.")
                    return Utente(nome, password)

    print("Credenziali errate.")
    return None


# MAIN

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