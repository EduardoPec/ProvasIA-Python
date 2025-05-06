produtos = {}
total_compra = 0
cont = 0

while cont < 5:
    cont += 1
    nome = input(f"Digite o nome do produto {cont}: ")
    preco = float(input(f"Digite o valor do produto {nome}: "))
    total_compra += preco
    produtos[nome] = preco

print("===========Sua da Compra===========")
for nome, preco in produtos.items():
    print(f"{nome}: R$ {preco:.2f}")
    
print(f"Valor total da compra: R$ {total_compra:.2f}")