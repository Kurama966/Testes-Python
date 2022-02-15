vel = float(input('Qual é a velocidade do seu carro? '))
if vel > 80:
    print('Você passou acima da velocidade permitida de 80 km/h e foi multado!')
    print('Você pagará uma multa de R$ {:.2f}'.format((vel-80)*7))
print('Tenha um bom dia! Dirija com segurança!')
