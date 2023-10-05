def calcular_raiz(n, num):
    return num ** (1/n)

n = int(input("Digite o valor de n para a raiz enésima: "))
num = int(input("Digite o número inteiro: "))

resultado = calcular_raiz(n, num)

print(f"A raiz {n}ª de {num} é {resultado}")
