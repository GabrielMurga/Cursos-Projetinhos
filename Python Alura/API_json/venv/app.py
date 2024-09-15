import requests
import json
url='https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
response= requests.get(url)
if response.status_code==200:
    dados=response.json()
    dados_restaurantes = {}
    for item in dados:
        nome_do_restaurante = item['Company']

        if nome_do_restaurante not in dados_restaurantes:
            dados_restaurantes[nome_do_restaurante] = []

        dados_restaurantes[nome_do_restaurante].append({
            "Item": item['Item'],
            "Preço": item['price'],
            "Descrição": item['description']
        })
        #Nesse código, eu criei um dicionário chamado dados_restaurantes,
#  e cada restaurante é um item do dicionário, 
# para cada restaurante eu crio uma lista, 
# que dentro dessa lista eu tenho dicionários 
# com as informações de item preço e descrição.Numa forma reduzida ficaria algo
# assim:{
#     "McDonald’s": [
#         {
#             "Item": "Big Mac",
#             "Preço": 5.99,
#             "Descrição": "Sanduíche clássico com hambúrguer, queijo, alface, molho especial."
#         },
#         {
#             "Item": "McFlurry",
#             "Preço": 3.49,
#             "Descrição": "Sobremesa de sorvete com cobertura e pedaços de chocolate."
#         }
#     ],
#     "Burger King": [
#         # Outros itens de outro restaurante
#     ]
# }

else:
    print(f"Codigo do erro é{response.status_code}")
    
for nome_do_restaurante,dados in dados_restaurantes.items():
    nome_do_arq=f'{nome_do_restaurante}.json'
    with open(nome_do_arq,'w') as arquivo_restaurante:
        json.dump(dados,arquivo_restaurante,indent= 4)# Passo o que eu queria mostrar, o nome do arquivo e a identação



# Ainda não entendi muito bem esse arquivo json, é basicamente uma lista com dicionários
# gigante escrita a mão e assiado há uma url htpps

