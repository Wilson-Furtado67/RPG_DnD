from random import randint
class Dado:
    def __init__(self,lados):
        self.lados = lados
        self.valor = 0
        
    def __str__(self):
        representasao = '{}'.format(self.valor)
        return  representasao
    
    def __add__(self,outra):
        total = self.valor + outra
        return total   
     
    def __radd__(self,outra):
        if outra == 0:
            return self
        else:
            return self.__add__(outra)
        
    def jogar(self):
        self.valor = randint(1,self.lados)


         