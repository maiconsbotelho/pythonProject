

print("Escolha uma das opções\n")
print("1 - Maça")
print("2 - Laranja")
print("3 - Banana")


opcao = int(input("\nDigita a opção escolhida: "))
quantidade = int(input("Digite a quantidade desejada: "))

maca = 2.30
laranja = 3.60
banana = 1.85
ssss = 2


if (opcao == 1):
    resultado = quantidade * maca
    print("\nVocê esta comprando {} maças".format(quantidade))
    print("Total da compra: R$ {}".format(resultado))

elif (opcao == 2):
    resultado = quantidade * laranja
    print("\nVocê esta comprando {} laranjas".format(quantidade))
    print("Total da compra: R$ {}".format(resultado))

elif (opcao == 3):
    resultado = quantidade * banana
    print("\nVocê esta comprando {} bananas".format(quantidade))
    print("Total da compra: R$ {}".format(resultado))

else:
    print("Opção invalida")

