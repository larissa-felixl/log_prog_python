nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
if idade >= 16:
    print(f'{nome} está apto(a) a tirar o título e votar!')
else:
    print('{nome} ainda não está apto(a) a votar')
