sal = float(input('Qual é o seu salário ?'))
if sal > 1250.00:
    sal = sal + (sal*10/100)
    print('Seu novo salário é de {}'.format(sal))
else:
    sal = sal + (sal*15/100)
    print('Seu novo salário é de {}'.format(sal))
