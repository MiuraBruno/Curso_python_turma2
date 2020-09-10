n = int(input('Informe o numero de alunos:\n'))
alunos = {}

for i in range(n):
    nome = input('Informe o Nome do aluno:\n')
    alunos[nome] = []
    notas = input('Informe as tres notas do aluno separadas por espaco:\n').split(' ')
    media = (float(notas[0]) + float(notas[1]) + float(notas[2]))/3
    alunos[nome].append(media)
    #print(media)
    if media >= 7.0:
        alunos[nome].append('Aprovado')
    elif media >= 5.0:
        alunos[nome].append('Exame')
    else:
        alunos[nome].append('Reprovado')


print('\n\n')
print('-' * 20 + 'STATUS DA SALA' + '-' * 20)
        
for i in alunos:
    print('O aluno %s' %(i))
    print('A media foi = %.2f' %(alunos[i][0]))
    print('O seu status e %s' %(alunos[i][1]))
    print('-' * 30)
    print('\n\n')