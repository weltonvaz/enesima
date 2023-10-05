# Função para calcular a raiz enésima de um número inteiro
def calcular_raiz_enesima(numero, n):
    if numero < 0 and n % 2 == 0:
        return "Não é possível calcular a raiz enésima de um número negativo com um expoente par."
    resultado = numero ** (1/n)
    return resultado

# Solicitar ao usuário o número e o valor de n
numero = float(input("Digite um número: "))
n = int(input("Digite o valor de n: "))

# Calcular e exibir a raiz enésima
raiz = calcular_raiz_enesima(numero, n)
print(f"A raiz enésima de {numero} com expoente {n} é igual a {raiz:.2f}")
