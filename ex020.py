from random import sample
a1 = input('Escreva o nome do primeiro aluno: ')
a2 = input('Escreva o nome do segundo aluno: ')
a3 = input('Escreva o nome do terceiro aluno: ')
a4 = input('Escreva o nome do quarto aluno: ')
print('Os alunos são {}, {}, {} e {} e a ordem de apresentação escolhida foi {}'.format(a1, a2, a3, a4, sample([a1,a2,a3,a4], k=4)))
