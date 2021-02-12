#Entrada de dados

a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))


soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b

# Forma de descobrir a tipagem da variavel
print(type(soma))

# Conversao dos tipos para string
print('==================================================')
print('================Com Conversao=====================')
print('==================================================')

print('soma: ' + str(soma))
print('subtracao: ' + str(subtracao))
print('multiplicacao: ' + str(multiplicacao))
print('divisao: ' + str(divisao))
print('resto: ' + str(resto))


# Realiza contactenação sem precisar converter
print('==================================================')
print('================Sem Conversao=====================')
print('==================================================')

print('soma: {}' .format(soma))
print('subtracao: {}' .format(subtracao))
print('multiplicacao: {}' .format(multiplicacao))
print('divisao: {}' .format(divisao))
print('resto: {}' .format(resto))