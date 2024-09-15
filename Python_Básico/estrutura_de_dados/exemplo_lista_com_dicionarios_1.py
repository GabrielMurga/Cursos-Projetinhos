clientes= [    
    { "nome": "Gabriel Losekann Paiva Murga", "telefone": "(21)973259462", "email" : "gabrielpaiva@gmail.com"},
    {"nome": " Claudia Paiva", "telefone": "(21)987653902", "email": "cacaupaiva@gmail.com"},
    {"nome": "Alice Terra", "telefone":"(32)908072013", "email": "aliceterra@gmail.com"}
    ]

print("\n [LISTA DE CLIENTES CADASTRADOS!]")
for cliente in clientes:
    print("Nome", cliente["nome"])
    print("Telefone", cliente["telefone"])
    print("Email", cliente["email"])