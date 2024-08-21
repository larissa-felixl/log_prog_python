nome = input('Digite o nome: ')
disciplina = input('Digite o nome da disciplina: ')
nota = float(input('Digite a nota: '))
if nota < 0 or nota > 10:
    print('Erro no sistema, nota inválida!')
else:
    if nota >= 5.5 and nota < 6.0:
        nota = 6
    if nota >= 6:
        status = 'aprovado(a)'
    else:
        status = 'reprovado(a)'
    print(f'{nome} está {status} em {disciplina} com nota {nota}.')