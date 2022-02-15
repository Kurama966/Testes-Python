print('\033[1;34m-=\033[m'*20)
print('Analisador de Triângulos')
print('\033[1;34m-=\033[m'*20)
a = float(input('Digite a primeira medida: '))
b = float(input('Digite a segunda medida: '))
c = float(input('Digite a terceira medida: '))
if a+b > c and a+c > b and b+c > a:
    print('Podemos formar um triângulo com essas três medidas')
else:
    print('Não podemos formar um triângulo com essas medidas')
