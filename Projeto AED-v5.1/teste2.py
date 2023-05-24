class Despesas:
    def __init__(self, categoria, descricao, valor, data):
        self.categoria = categoria
        self.descricao = descricao
        self.valor = valor
        self.data = data

    def set_nome(self, categoria):
        self.categoria = categoria
    def set_descricao(self, descricao):
        self.descricao = descricao
    def set_valor(self, valor):
        self.valor = valor
    def set_data(self, data):
        self.data = data

    def get_categoria(self):
        return self.categoria
    def get_descricao(self):
        return self.descricao
    def get_valor(self):
        return self.valor
    def get_data(self):
        return self.data


def quick_sort(lista):
    if len(lista) <= 1:
        return 1
    else:
        pivot = lista[0]
        menores = [elem for elem in lista[1:] if elem < pivot]
        maiores = [elem for elem in lista[1:] if elem >= pivot]
        return quick_sort(menores) + [pivot] + quick_sort(maiores)
    
def bubble_sort(lista):
    for i in range(len(lista)):
        for j in range (0, len(lista) -i -1):
            if (
                (lista[j].get_valor()) > 
                (lista[j+1].get_valor())
            ):
                temp = lista[j]
                lista[j] = lista[j+1]
                lista [j+1] = temp
    return lista

def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivot = lista[0]
    
        menores = [elem for elem in lista[1:] if elem.get_valor() < pivot.get_valor()]
        maiores = [elem for elem in lista[1:] if elem.get_valor() >= pivot.get_valor()]
        print(maiores, menores, pivot)
        return quick_sort(menores) + [pivot] + quick_sort(maiores)

lista= [
    Despesas('A','aaa', 0,'data'),
    Despesas('A','aaa', 8,'data'),
    Despesas('A','aaa', 6,'data'),
    Despesas('A','aaa', 5,'data'),
    Despesas('A','aaa', 7,'data'),
    Despesas('A','aaa', 423,'data'),
    Despesas('A','aaa', 3,'data'),
    Despesas('A','aaa', 9,'data'),
    Despesas('A','aaa', 1,'data'),
    Despesas('A','aaa', 2,'data'),

]

a=quick_sort(lista)

for elemento in a:
    print(elemento.get_valor())
