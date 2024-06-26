class Calculadora:
    def soma(self, a, b):
        return a + b
    
    def subtracao(self, a, b):
        return a - b
    
    def divisao(self, a, b):
        if b != 0:
            return a / b
        else:
            return 'O resultado sempre sera 0'
    
    def multiplicacao(self, a, b):
        return a * b
    

num1 = float(input('Primeiro valor: '))
num2 = float(input('Segundo valor: '))
opcao = input('Deseja +, -, /, * ')

minha_calculadora = Calculadora()

while True:
    while opcao not in('+','-','/','*'):
        opcao = input('Entre com esses valores: +, -, /, *  : ')
    if opcao in('+','-','/','*'):
        if opcao == '+':
            resultado = minha_calculadora.soma(num1, num2)
        elif opcao == '-':
            resultado = minha_calculadora.subtracao(num1, num2)
        elif opcao == '/':
            resultado = minha_calculadora.divisao(num1, num2)
        elif opcao == '*':
            resultado = minha_calculadora.multiplicacao(num1, num2)
        else:
            raise 'Opção invalida'
        break


print(f'Resultado: {resultado} !!!')