real = float(input('Quantos reais você tem na carteira? R$ '))
dol = real/5.37
euro = real/6.47
iene = real/0.049
won = real/0.0048
print('Com R$ {}, você pode comprar US$ {:.2f}! '.format(real, dol))
print('Com R$ {}, você pode comprar EUR {:.2f}! '.format(real, euro))
print('Com R$ {}, você pode comprar JPY {:.2f}! '.format(real, iene))
print('Com R$ {}, você pode comprar WON {:.2f}! '.format(real, won))