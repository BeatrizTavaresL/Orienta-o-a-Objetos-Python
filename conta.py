class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print('Construindo objeto ... {}'.format(self))
        self.__numero = numero
        self.__titular = titular 
        self.__saldo = saldo
        self.__limite = limite
        


    def extrato(self):
        print('O saldo de {} do titular {} e o limite é de {}'.format(self.__saldo, self.__titular, self.__limite))

    def deposita(self, valor):
        self.__saldo += valor
    
    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_sacar

    def saque(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou do limite disponível!".format(valor))


    def transferir(self, valor):
        self.saque(valor) 
        self.deposita(valor)

    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular
    
    @property
    def limite(self):   # def get_limite(self): 
        return self.__limite  
    
    @limite.setter
    def limite(self, novo_limite): # def set_limite(self, novo_limite): 
        self.__limite = novo_limite

    @staticmethod
    def codigo_banco():
        return '001'
    
    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco':'237'}
    
    

 # __numero__ esses dois espaço, quer dizer que encapsulou o acesso aos atributos. 