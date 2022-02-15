m = float(input('Digite um valor em metros: '))
km = m/1000
hm = m/100
dam = m/10
dm = m*10
cm = m*100
mm = m*1000
print('O valor digitado foi {} metros \nO valor em quilômetros é {} km. \nO valor em hectômetros é {} hm. \nO valor em decâmetros é {} dam. \nO valor em decímetros é {:.0f} dm. \nO valor em centímetros é {:.0f} cm \nO valor em milímetros é {:.0f} mm'.format(m, km, hm, dam, dm, cm, mm))
