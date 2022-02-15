dias = float(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos quilômetros foram rodados? '))
vd = dias * 60
kmr = km * 0.15
valor = vd + kmr
print('Você alugou o carro por {:.0f} dias e rodou por {} km, o valor total a ser pago é de R$ {:.2f}'.format(dias, km, valor))
