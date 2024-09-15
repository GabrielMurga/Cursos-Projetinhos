from modelos.restaurante import Restaurantes
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
bebida_suco= Bebida("Suco de Laranja",5.0,"Grande")
macarrao1=Prato("Carbonara",30,"Spaghetti à carbonara ")
restaurante1=Restaurantes('Outback','Gourmet')
restaurante2=Restaurantes('Coco-Bambum','Frutos do mar')
restaurante3= Restaurantes('MacDonalds',"Fast-food")
restaurante1.receber_avaliacao('Gabriel',5)
restaurante1.receber_avaliacao('Gabriel',10)
restaurante1.adicionar_no_cardapio(bebida_suco)
restaurante1.adicionar_no_cardapio(macarrao1)
bebida_suco.aplicar_desconto(8)
macarrao1.aplicar_desconto(5)
def main():
    Restaurantes.listar_restaurantes()
    restaurante1.exibe_cardapio
if __name__=='__main__':
    main()