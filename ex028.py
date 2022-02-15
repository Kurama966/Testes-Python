from random import randint
print('Pensei em um número entre 0 e 5, tente adivinhar qual foi. ')
num = randint(0, 5)
esc = int(input('Escreva seu palpite: '))
print('O número que pensei foi {} e o seu número escolhido foi {}'.format(num,esc))
if num == esc:
    print('Parabéns você é bom de adivinhação!')
else:
    print('Não foi dessa vez!')
