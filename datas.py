class Data:
    def __init__ (self, dia, mes, ano):
        print('Construindo Objetos Contas...{}'.format(self))
        self.dia = dia
        self.mes = mes
        self.ano = ano
        

    def formatada(self):
        print('{}/{}/{}'.format(self.dia, self.mes, self.ano))

   
        
  