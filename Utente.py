class Utente:
    
    def init(self, nome, password):
        self.nome = nome
        self.__password = password


    def registraUtente(self, file_credenziali):
        with open(file_credenziali, "a") as file:
            file.write(self.nome, ",", self.__password, "\n")

    def loginUtente(self, file_credenziali):
        try:
            with open(file_credenziali, "r") as f:
                righe = f.readlines()
            for riga in righe:
                n, p = riga.strip().split(",")
                if n == self.nome and p == self.__password:
                    return True
        except FileNotFoundError:
            return False
        return False

    def controllaPassword(self, password):
        if self._password == password:
            return True
        else:
            return False


    def get_password(self):
        return self._password