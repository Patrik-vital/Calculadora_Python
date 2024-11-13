print("Bem vindo a calculadora! \nQual operação deseja realizar?")

print("1- Soma \n2- Subtração \n3- Multiplicação \n4- Divisão")
operacao = int(input())

def soma():
    x = int(input())
    y = int(input())
    soma = x + y
    return soma

def subtracao():
    x = int(input())
    y = int(input())
    soma = x - y
    return subtracao

def multiplicacao():
    x = int(input())
    y = int(input())
    soma = x * y
    return multiplicacao

def divisao():
    x = int(input())
    y = int(input())
    soma = x/y
    return divisao
            
def qual_operacao(operacao):
    if operacao == 1:
        return soma()
    elif operacao == 2:
        return subtracao() 
    elif operacao == 3:
        return multiplicacao()
    elif operacao == 4:
        return divisao()    

qual_operacao(operacao)