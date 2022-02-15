print('Vamos calcular o preço da sua viagem.')
dist = float(input('Qual é a distância da viagem em Km? '))
if dist <= 200:
    print('Você está prestes a fazer uma viagem de {} km'.format(dist))
    print('O preço da sua passagem será de {:.2f} reais'.format(dist*0.5))
else:
    print('Você está prestes a fazer uma viagem de {} km'.format(dist))
    print('O preço da sua passagem será de {:.2f} reais'.format(dist*0.45))
