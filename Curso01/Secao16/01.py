class Pessoa:
    
    def __init__(self, nome, idade, altura) -> None:
        self.__nome:str = nome
        self.__idade:str = idade
        self.__altura:str = altura
        
    
    def mostrar_na_tela(self):
        return f'Nome: {self.__nome.title()}, Idade: {self.__idade}, Altura: {self.__altura}'
    
    
    def get_nome(self):
        return self.__nome
    
    
    def set_nome(self, nome):
        self.__nome = nome
        

    def get_idade(self):
        return self.__idade
    
    
    def set_idade(self, idade):
        self.__idade = idade
        
    
    def get_altura(self):
        return self.__altura
    
    
    def set_altura(self, altura):
        self.__altura = altura
        
        
usu = Pessoa('cleiton', 23, 170)
print(usu.mostrar_na_tela())