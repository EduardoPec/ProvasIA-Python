contato = {}

contato["Nome"] = input("Informe o nome do contato: ")
contato["Número"] = input("Informe seu número de telefone: ")
contato["Email"] = input("Informe seu email: ")

for chave, valor in contato.items():
    print("===========================")
    print(f"{chave}: {valor}")
    print("===========================")