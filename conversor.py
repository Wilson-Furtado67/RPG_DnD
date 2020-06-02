import csv
import os
import pprint # pprint é um modulo para aprisentaçoes bunitas de dicionarios e listas
import json
import copy
def procura_chaves(arquivo):
    """ Essa funçao ira ler a primeira linha do arquivo e retornar as chaves"""
    for linha in arquivo:
        return linha
                       
class Colecionador():
    def __init__(self,nome_do_banco):
        self.dicionario = {
            nome_do_banco: []
        }
        self.nome_do_banco = nome_do_banco
        
    def __str__(self):
        return "{}".format(self.dicionario)
    def __add__(self,other):
        self.update(other)
    
    def criar_dicionario(self,caminho_do_arquivo):
        ''' Esse metodo cria um dicionario apartir de um arquivo.csv'''
        endereco = os.path.join(caminho_do_arquivo)
        with open(endereco) as arquivo:
            panilha = csv.reader(arquivo,delimiter=',')
            lista_de_chaves = procura_chaves(panilha)
            for elemeto in panilha:
                new_dicionary = {}
                index_de_chaves = 0
                for valor in elemeto:
                    key = str(lista_de_chaves[index_de_chaves])
                    new_dicionary.setdefault(key,'') 
                    new_dicionary[key] = valor
                    index_de_chaves += 1
                self.dicionario[self.nome_do_banco].append(new_dicionary)
     
    def update(self,other):
        self.dicionario.update(other)
         
                
    def retornar_dicionario(self):
        return self.dicionario
    
    def purificar(self):
        pass
    
    def criar_json(self,nome_do_arquivo_json):
        """Esse metodo cria um arquivo json apartir do self.dicionario"""
        endereco = os.path.join(nome_do_arquivo_json)
        with open(endereco, 'w') as arquivo:
            json.dump(self.dicionario, arquivo,skipkeys=True,indent=4)

    
if __name__ in "__main__":
    nome_do_DB = str(input("qual sera o nome do DB: "))
    DB = Colecionador(nome_do_DB)    
    arquivo_csv = str(input("Qual é o nome do do arquivo csv: "))
    DB.criar_dicionario(arquivo_csv)     
    nome_do_json = str(input("Qualsera o nome do aquivo json: "))
    DB.criar_json(nome_do_json)
    
    
    