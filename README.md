# Progetto n° 2
Progetto di gruppo n° 2 del Corso Python and Machine Learning di:
- [Elisabetta Carella](https://github.com/eli-carella)
- [Gabriele Giuliani](https://github.com/giulianigabbo95/).

---

## Testo
Realizzare un programma che gestisca un file denominato studenti.txt e che implementi:

1. Sistema di autenticazione:
    Il programma deve prevedere un ciclo ripetitivo che consenta all'utente di:
        - Effettuare la registrazione:
            - L'utente deve inserire nome e password
            - Le credenziali devono essere salvate nel file credenziali.txt, una per riga.
        - Effettuare il login
            - Il sistema deve verificare che le credenziali inserite siano presenti nel file.

2. Funzionalità disponibili dopo il login:
    Una volta autenticato, l'utente può scegliere tra le seguenti operazioni:
        - Inserimento o modifica studenti
            - Aggiungere un nuovo studente con i seguenti attributi:
                - Nome
                - Corso
            - Modificare la lista degli studenti già presenti.  
            NB: I dati devono essere salvati in formato CSV.
        - Stampa dell'aula
            - Visualizzare l'elenco completo degli studenti.
            - L'elenco deve essere ordinato per corso.

3. Gestione Admin
    Creare una classe Admin che estenda la classe Utente:
        - Non deve registrarsi.
        - Può accedere direttamente al sistema tramite credenziali hardcoded.
        - Ha la possibilità di resettare completamente la lista degli studenti.
        - Ogni intervento di reset deve essere accompagnato da una motivazione, che verrà salvata nel file intervento_utente.txt.