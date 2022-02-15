cid = input('Digite o nome da sua cidade: ')
cid = cid.lower()
div = cid.split()
print('A sua cidade começa com o nome "Santo"? {}'.format('santo' in div[0]))
