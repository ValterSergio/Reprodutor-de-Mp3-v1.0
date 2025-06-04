class Musica:
    def __init__(self, **dados):
        for atributo, valor in dados.items():
            self.adicionar_atributo(atributo, valor)
    
    def get_indice(self):
        return self.indice
    
    def set_indice(self, indice: int):
        self.indice = indice

    def adicionar_atributo(self, atributo, valor):
        setattr(self, atributo, valor)
    
    def modificar_atributo(self, atributo, novo_valor):
        for atr, val in self.__dict__.items():
            if atr.lower() == atributo.lower():
                atr = novo_valor
                break
    
    
    def exibir_musica(self):
        dicio = self.__dict__
        for atributo,valor in dicio.items():
            print(atributo, valor)

