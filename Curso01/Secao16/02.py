class Pessoa:
    def __init__(self, nome:str, idade, altura) -> None:
        self.__nome:str = nome.title()
        self.__idade:str = idade
        self.__altura:str = altura
        
    
    def mostrar_na_tela(self):
        return f'Nome: {self.__nome}, Idade: {self.__idade}, Altura: {self.__altura}'
    
    
    def get_nome(self):
        return self.__nome
    
    
    def set_nome(self, nome):
        self.__nome = nome.title()
        

    def get_idade(self):
        return self.__idade
    
    
    def set_idade(self, idade):
        self.__idade = idade
        
    
    def get_altura(self):
        return self.__altura
    
    
    def set_altura(self, altura):
        self.__altura = altura


class Agenda:
    
    def __init__(self) -> None:
        self.__agenda = []
 
    
    def add_pessoa(self, pessoa:Pessoa):
        self.__agenda.append(pessoa)
  
    
    def remove_pessoa(self, nome):
        if len(self.__agenda) > 0:
            encontrou = False
            for i in self.__agenda:
                if nome.title() == i.get_nome():
                    self.__agenda.remove(i)
                    encontrou = True
            if encontrou:
                return 'Removido com sucesso da agenda'
            else:
                return 'Nao foi possivel encontrar na agenda'
        else:
            return 'Agenda vazia'


    def buscar_pessoa(self, nome):
        if len(self.__agenda) > 0:
            indece = -1
            for index, item in enumerate(self.__agenda):
                if nome.title() == item.get_nome():
                    indece = index
            if indece >= 0:
                return f'A posicao na agenda: {indece}'
            else:
                return f'Nao foi encontrado na agenda!'
        else:
            return 'Agenda vazia'


    def mostrar_agenda(self):
        for index, item in enumerate(self.__agenda):
            yield f'Posicao na agenda: {index}, Nome: {item.get_nome()}, Idade: {item.get_idade()}, Altura: {item.get_altura()}'


    def mostrar_pessoa_index(self, i):
        if len(self.__agenda) > 0:
            indece = -1
            for index, item in enumerate(self.__agenda):
                if i == index:
                    indece = item
            if indece == -1:
                return f'Nao foi encontrado na agenda!'
            else:
                return f'Nome: {indece.get_nome()}, Idade: {indece.get_idade()}, Altura: {indece.get_altura()}'
        else:
            return 'Agenda vazia'
    
    
agenda = Agenda()
usu = Pessoa('silva', 23, 170)
usu1 = Pessoa('cleitons', 18, 175)
agenda.add_pessoa(usu)
agenda.add_pessoa(usu1)
print(agenda.remove_pessoa('cleiton'))
print(agenda.buscar_pessoa('cleitons'))
for i in agenda.mostrar_agenda():
    print(i)

print(agenda.mostrar_pessoa_index(1))