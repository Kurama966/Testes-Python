alt = float(input('Qual a altura da sua parede? '))
larg = float(input('Qual a largura da sua parede? '))
area = larg*alt
# print('A área da sua parede é de {} metros quadrados e sabendo que cada litro de tinta pinta 2 metros quadrados você irá precisar de {:.2f} litros de tinta'.format(area, area/2))
print('Sua parede tem a dimensão de {}m x {}m e a área de {}m²'.format(larg, alt, area))
print('Você irá precisar de {}l de tinta para pintar a parede'.format(area/2))
