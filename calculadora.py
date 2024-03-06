
print('\nCALCULADORA')

print('+ Adição')
print('- subtração')
print('* Multiplicação')
print('/ Divisão')


operador = input('\nQual operação você quer realizar? ')

if (operador == '+') or (operador == '-') or (operador == '*') or (operador == '/'):
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))

    if (operador == '+'):
        resultado = n1 + n2
        print('\nResultado {} {} {} = {}'.format(n1, operador, n2, resultado))

    elif (operador == '-'):
        resultado = n1 - n2
        print('\nResultado {} {} {} = {}'.format(n1, operador, n2, resultado))

    elif (operador == '*'):
        resultado = n1 * n2
        print('\nResultado {} {} {} = {}'.format(n1, operador, n2, resultado))

    elif (operador == '/'):
        resultado = n1 / n2
        print('\nResultado {} {} {} = {}'.format(n1, operador, n2, resultado))

else:
    print('Operação invalida!!!')

print('Encerrando o programa...')


