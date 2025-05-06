def maior_numero(n1,n2,n3):
    if n1 >= n2 and n1 >= n3:
        return n1
    elif n2 >= n1 and n2 >= n3:
        return n2
    else:
        return n3
    
resultado = maior_numero(4, 22, 13)
print(f"O maior número entre é: {resultado}")