valor = int(input('Digite o valor em R$ '))

while True:
    if valor >= 100:
        cedula100 = valor // 100
        valor -= cedula100 * 100
        print('cédulas de R$ 100,00: {}'.format(cedula100))
        if not valor:
            break

    if valor >= 50:
        cedula50 = valor // 50
        valor -= cedula50 * 50
        print('cédulas de R$ 50,00: {}'.format(cedula50))
        if not valor:
            break

    if valor >= 20:
        cedula20 = valor // 20
        valor -= cedula20 * 20
        print('cédulas de R$ 20,00: {}'.format(cedula20))
        if not valor:
            break

    if valor >= 10:
        cedula10 = valor // 10
        valor -= cedula10 * 10
        print('cédulas de R$ 10,00: {}'.format(cedula10))
        if not valor:
            break

    if valor >= 5:
        cedula5 = valor // 5
        valor -= cedula5 * 5
        print('cédulas de R$ 5,00: {}'.format(cedula5))
        if not valor:
            break

    if valor:
        cedula1 = valor
        print('Cédulas de R$ 1,00: {}'.format(cedula1))
        break