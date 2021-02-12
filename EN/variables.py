#Information input

a = int(input('Type the frist value: '))
b = int(input('Type the second value: '))


summ = a + b
subtraction = a - b
multiplication = a * b
division = a / b
rest = a % b

# Way to find the type of variablel 
print(type(summ))

# Converting the types to string
print('==================================================')
print('================With conversion===================')
print('==================================================')

print('sum: ' + str(summ))
print('subtraction: ' + str(subtraction))
print('multiplication: ' + str(multiplication))
print('division: ' + str(division))
print('rest: ' + str(rest))

# Concatenate  without having to convert
print('==================================================')
print('==============Without conversion==================')
print('==================================================')

print('sum: {}' .format(summ))
print('subtraction: {}' .format(subtraction))
print('multiplication: {}' .format(multiplication))
print('division: {}' .format(division))
print('rest: {}' .format(rest))