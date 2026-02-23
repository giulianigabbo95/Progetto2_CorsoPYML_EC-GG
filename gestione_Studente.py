# CLASSE STUDENTE

class Studente:
    def __init__(self, nome, corso):
        self.nome = nome
        self.corso = corso

    def to_list(self):
        return [self.nome, self.corso]

    def __str__(self):
        return f"Nome: {self.nome} - Corso: {self.corso}"