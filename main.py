'''
Realizzare un programma che gestisca un file denominato studenti.txt e che implementi:

1. Sistema di autenticazione:
    Il programma deve prevedere un ciclo ripetitivo che consenta all'utente di:
        - Effettuare la registrazione:
            . L'utente deve inserire nome e password
            . Le credenziali devono essere salvate nel file credenziali.txt, una per riga.
        - Effettuare il login
            . Il sistema deve verificare che le credenziali inserite siano presenti nel file.

2. Funzionalità disponibili dopo il login:
    Una volta autenticato, l'utente può scegliere tra le seguenti operazioni:
        - Inserimento o modifica studenti
            . Aggiungere un nuovo studente con i seguenti attributi:
                a. Nome
                b. Corso
            . Modificare la lista degli studenti già presenti.
            NB: I dati devono essere salvati in formato CSV.
        - Stampa dell'aula
            . Visualizzare l'elenco completo degli studenti.
            . L'elenco deve essere ordinato per corso.

3. Gestione Admin
    Creare una classe Admin che estenda la classe Utente:
        - Non deve registrarsi.
        - Può accedere direttamente al sistema tramite credenziali hardcoded.
        - Ha la possibilità di resettare completamente la lista degli studenti.
        - Ogni intervento di reset deve essere accompagnato da una motivazione, che verrà salvata nel file intervento_utente.txt.
'''
from Utente import Utente

FILE_CREDENZIALI = "credenziali.txt"
FILE_STUDENTI = "studenti.csv"

# MAIN
while True:
    print("1. Registrazione")
    print("2. Login")
    print("0. Esci")

    scelta = input("Scelta: ")

    match scelta:
        case "1":
            new_user_nome = input("Inserisci Nome: ")
            new_user_pass = input("Inserisci Password: ")
            new_user = Utente(new_user_nome, new_user_pass)
            if new_user.registraUtente(FILE_CREDENZIALI):
                print("Utente Registrato!")
                new_user.menuUtente()
            else:
                print("Utente NON registrato!")
        case "2":
            old_user_nome = input("Inserisci Nome: ")
            old_user_pass = input("Inserisci Password: ")
            old_user = Utente(old_user_nome, old_user_pass)
            if old_user.loginUtente(FILE_CREDENZIALI) == True:
                print("Accesso effettuato!")
                old_user.menuUtente()
            else:
                print("Accesso Fallito!")
        case "0":
            break
        case _:
            print("Scelta non valida.")

