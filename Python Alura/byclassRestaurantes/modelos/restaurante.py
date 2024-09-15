from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio
class Restaurantes:
    restaurantes=[]
    def __init__(self,nome,categoria): #metodo especial de construção da estrutura asism, toda vez que essa classe for cirada será necessário informar os atributos
        self.nome= nome
        self.categoria= categoria
        self._ativo= False
        self._avaliacao= []
        self._cardapio=[]
        Restaurantes.restaurantes.append(self)
    def __str__(self):#metodo especial  para sempre que o restaurante foi mencionado em forma de texto não aparecer o endereço de memoria
        return f'{self.nome}||{self.categoria} '
    @classmethod
    def listar_restaurantes(cls):# metodo CRIADO para listar os restaurantes
        print(f'Lista dos restaurantes cadastados: \n') 
        print(f'{"Nome".ljust(20)} {"Categoria".ljust(20)} {"Avaliação".ljust(20)} {"Status"}\n')
        for restaurante in cls.restaurantes:
            print(f'{restaurante.nome.ljust(20)}|{restaurante.categoria.ljust(20)}|{str(restaurante.media_avaliacao).ljust(20)}|{restaurante.ativo}')
    @property
    def ativo(self):
        return  'Ativo' if self._ativo else'Desativado'
    def alterna_estado(self):
        self._ativo = not self._ativo
    def receber_avaliacao(self,cliente,nota):
        avaliacao= Avaliacao(cliente,nota)
        self._avaliacao.append(avaliacao)
    @property
    def media_avaliacao(self):
        if  not self._avaliacao:
            return "-"
        else:
            soma = sum(avaliacao._nota for avaliacao in self._avaliacao) 
            qnt = len(self._avaliacao)
            media= round(soma/qnt,1)
            return media
    def adicionar_no_cardapio(self,item):
        if isinstance(item,ItemCardapio):
            self._cardapio.append(item)
    @property
    def exibe_cardapio(self):
        print(f"Cardapio do {self.nome}\n")
        for i, item in enumerate( self._cardapio,1):
            if hasattr(item,'_descricao'):
                mensagem_prato= print(f" {i}- Nome: {item._nome.ljust(20)}|Preço:R$ {str(item._preco).ljust(20)}| Descrição: {item._descricao}")
                print(mensagem_prato)
            else:
                mensagem_bebida= print(f" {i}- Nome: {item._nome.ljust(20)}|Preço:R$ {str(item._preco).ljust(20)}| Tamanho: {item._tamanho}")
                print(mensagem_bebida)
                
                


