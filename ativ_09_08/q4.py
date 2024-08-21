login = input('Digite seu login: ')
senha = input('Digite sua senha: ')
if login == "admin" and senha == "123":
    print(f'Seja bem vindo(a) {login}!')
else:
    print('Senha ou login incorretos tente novamente!')