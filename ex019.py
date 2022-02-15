from random import sample
a1 = input('Escreva o nome do primeiro aluno: ')
a2 = input('Escreva o nome do segundo aluno: ')
a3 = input('Escreva o nome do terceiro aluno: ')
a4 = input('Escreva o nome do quarto aluno: ')
esc = sample([a1, a2, a3, a4], k=1)
print('Os nomes dos quatro alunos são {}, {}, {} e {}. \nO aluno escolhido foi {}'.format(a1, a2, a3, a4, esc))
