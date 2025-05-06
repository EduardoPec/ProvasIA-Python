import random

def lancar_dados():

    dado1 = random.randint(1, 6) 
    dado2 = random.randint(1, 6)  
    soma = dado1 + dado2  
    return dado1, dado2, soma  

if __name__ == "__main__":
    dado1, dado2, resultado = lancar_dados()
    print("============= Lançador de Dados =============")
    print(f"O valor do primeiro dado foi: {dado1}")
    print(f"O valor do segundo dado foi: {dado2}")
    print(f"A soma dos dois dados é igual a: {resultado}")
    print("=============================================")

