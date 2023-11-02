class Pessoa:
    def __init__(self,nome,peso,idade):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.comendo = False
        self.andando = False
        self.dormindo = False
    def comer(self, alimento):
        if self.dormindo == True:
            print(f"{self.nome} não pode comer enquanto dorme")
        elif self.andando == True:
            print(f"{self.nome} não pode comer enquanto anda")
        elif self.comendo == False:
            print(f"{self.nome} está comendo {alimento}")
            self.comendo = True
        else:
            print(f"{self.nome} já está comendo")
    def parar_comer(self):
        if self.comendo == True:
            print(f"{self.nome} acabou de comer")
            self.comendo = False
        else:
            print(f"{self.nome} não está comendo")
    def andar(self):
        if self.dormindo == True:
            print(f"{self.nome} não pode andar enquanto dorme")
        elif self.comendo == True:
            print(f"{self.nome} não pode andar enquanto come")
        elif self.andando == False:
            print(f"{self.nome} está andando")
            self.andando = True
        else:
            print(f"{self.nome} já está andando")
    def parar_andar(self):
        if self.andando == True:
            print(f"{self.nome} parou de andar")
            self.andando = False
        else:
            print(f"{self.nome} já está parado")
    def dormir(self):
        if self.comendo == True:
            print(f"{self.nome} está comendo, não pode dormir")
        elif self.andando == True:
            print(f"{self.nome} está andando, não pode dormir")
        elif self.dormindo == False:
            print(f"{self.nome} foi dormir")
            self.dormindo = True
        else:
            print(f"{self.nome} já está dormindo")
    def acordar(self):
        if self.andando == True:
            print(f"{self.nome} não está dormindo")
        elif self.comendo == True:
            print(f"{self.nome} não está dormindo")
        elif self.dormindo == True:
            print(f"{self.nome} acordou")
            self.dormindo = False
        else:
            print(f"{self.nome} não está dormindo")

