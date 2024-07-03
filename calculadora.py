import math

# Lista para armazenar o histórico
historico = []

def somar(x, y):
    resultado = x + y
    historico.append(f"Adição: {x} + {y} = {resultado}")
    return resultado

def subtrair(x, y):
    resultado = x - y
    historico.append(f"Subtração: {x} - {y} = {resultado}")
    return resultado

def multiplicar(x, y):
    resultado = x * y
    historico.append(f"Multiplicação: {x} * {y} = {resultado}")
    return resultado

def dividir(x, y):
    if y == 0:
        historico.append("Erro: Divisão por zero!")
        return "Erro: Divisão por zero!"
    resultado = x / y
    historico.append(f"Divisão: {x} / {y} = {resultado}")
    return resultado

def potencia(x, y):
    resultado = x ** y
    historico.append(f"Potência: {x} ^ {y} = {resultado}")
    return resultado

def raiz_quadrada(x):
    resultado = math.sqrt(x)
    historico.append(f"Raiz quadrada: sqrt({x}) = {resultado}")
    return resultado

def logaritmo(x, base=10):
    resultado = math.log(x, base)
    historico.append(f"Logaritmo (base {base}): log({x}) = {resultado}")
    return resultado

def seno(x):
    resultado = math.sin(math.radians(x))
    historico.append(f"Seno: sin({x} graus) = {resultado}")
    return resultado

def cosseno(x):
    resultado = math.cos(math.radians(x))
    historico.append(f"Cosseno: cos({x} graus) = {resultado}")
    return resultado

def tangente(x):
    resultado = math.tan(math.radians(x))
    historico.append(f"Tangente: tan({x} graus) = {resultado}")
    return resultado

def fatorial(x):
    resultado = math.factorial(x)
    historico.append(f"Fatorial: {x}! = {resultado}")
    return resultado

def valor_absoluto(x):
    resultado = abs(x)
    historico.append(f"Valor absoluto: abs({x}) = {resultado}")
    return resultado

def graus_para_radianos(x):
    resultado = math.radians(x)
    historico.append(f"Graus para Radianos: {x} graus = {resultado} radianos")
    return resultado

def radianos_para_graus(x):
    resultado = math.degrees(x)
    historico.append(f"Radianos para Graus: {x} radianos = {resultado} graus")
    return resultado

def mostrar_historico():
    for registro in historico:
        print(registro)

# Exemplo de uso
print("Adição: ", somar(5, 3))
print("Subtração: ", subtrair(10, 4))
print("Multiplicação: ", multiplicar(7, 2))
print("Divisão: ", dividir(8, 2))
print("Potência: ", potencia(3, 3))
print("Raiz quadrada: ", raiz_quadrada(16))
print("Logaritmo (base 10): ", logaritmo(100))
print("Seno (em graus): ", seno(30))
print("Cosseno (em graus): ", cosseno(60))
print("Tangente (em graus): ", tangente(45))
print("Fatorial: ", fatorial(5))
print("Valor absoluto: ", valor_absoluto(-7))
print("Graus para Radianos: ", graus_para_radianos(180))
print("Radianos para Graus: ", radianos_para_graus(math.pi))

print("\nHistórico: ")
mostrar_historico()
