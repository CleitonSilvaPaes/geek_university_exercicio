class Elevador:
    
    capacidade = []
    
    def __init__(self) -> None:
        self.__capacidade = 4
        self.__andares = 3
        self.__andar = 0
        
    def entra(self, pessoa):
        if len(self.capacidade) <= self.__capacidade:
            self.capacidade.append(pessoa)
            return 'Entrou com sucesso'
        else:
            return 'Nao foi posivel entrar pois esta lotado'
        
    def sair(self):
        try:
            self.capacidade.pop()
            return 'Saiu com sucesso'
        except IndexError:
            return 'Nao ao pessoa para sair'

    def sobe(self):
        if self.__andar < self.__andares:
            self.__andar += 1
            return 'Subiu com sucesso'
        else:
            return 'Nao foi possivel subir pois esta no andar mais alto'

    def descer(self):
        if self.__andar > 0:
            self.__andar -= 1
            return 'Desceu com sucesso'
        else:
            return 'Nao foi possivel descer pois esta no andar mais baixo'

ele = Elevador()
use = 'Cleiton'