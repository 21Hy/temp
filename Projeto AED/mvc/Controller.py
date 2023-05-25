import json

class Controller:
    def __init__(self, master):
        self.master = master
        self.data = None
        self.users = None
        self.user_data = []

    def escrever_ficheiro_json(self,nome_ficheiro, data):
        self.json_string = json.dumps(data, indent = 2)
        self.json_file = open(nome_ficheiro, 'w')
        self.json_file.write(self.json_string)
        self.json_file.close()

    def ler_ficheiro_json(self,nome_ficheiro):
        with open(nome_ficheiro, 'r') as f:
            self.data = json.load(f)
        return self.data
    
    def quick_sort(self, lista): # código com ERRO
        if len(lista) <= 1:
            return 1
        else:
            pivot = lista[0]
            menores = [elem for elem in lista[1:] if elem.get_valor() < pivot.get_valor()]
            maiores = [elem for elem in lista[1:] if elem.get_valor() >= pivot.get_valor()]
            return self.quick_sort(menores) + [pivot] + self.quick_sort(maiores)
        
    def bubble_sort_valores(lista, ordenacao):
        for i in range(len(lista)):
            for j in range (0, len(lista) -i -1):
                if (
                    (lista[j].get_valor()) > 
                    (lista[j+1].get_valor())
                ):
                    temp = lista[j]
                    lista[j] = lista[j+1]
                    lista [j+1] = temp
        if ordenacao == 0: # decrescente
            return lista.reverse()
        if ordenacao == 1: # crescente
            return lista
        
    def bubble_sort_alfabeticamente(lista):
        for i in range(len(lista)):
            for j in range (0, len(lista) -i -1):
                if (
                    (lista[j].get_categoria()) > 
                    (lista[j+1].get_categoria())
                ):
                    temp = lista[j]
                    lista[j] = lista[j+1]
                    lista [j+1] = temp
        return lista
    
    def ordenar_por_categoria(self, categoria, lista): 
        for elemento in lista:
            if elemento.get_categoria() == categoria:
                yield elemento
        else:
            return None
                
    def ordenar_despesas_periodo_tempo(self):
        pass

        





    

