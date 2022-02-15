from math import hypot
catop = float(input('Digite o comprimento do cateto oposto: '))
catadj = float(input('Digite o comprimento do cateto adjacente: '))
hip = hypot(catop,catadj)
print('A hipotenusa desse triângulo retângulo é {:.2f}'.format(hip))
