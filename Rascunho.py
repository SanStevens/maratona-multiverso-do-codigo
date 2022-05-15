print("\n 1º ELEIÇÃO DA CIDADE TERMINAL - SEJA BEM VINDO - TRE da UNISA ")

#Variaveis
maiorp = 'SEM VOTOS'
faltas = 0
Senha = 1234
Voto = 0
Nulo = 0
#Candidatos a Prefeitos
marcos = andre = jesiel = VotoBranco = Nulo = 0
Z = ''
#Empate
empate = 0
Cand1 = ''
Cand2 = ''
Voto = ''
Voto1 = 0
Voto2 = 0

#Código

#Código
print("\n ATENÇÂO - Mesario da Unisa você será responsavel pelo controle da votação e dos eleitores\n")
S = int(input(" Mesario: Digite a senha chave de segurança para iniciar a sessão: "))
print()
Q = int(input('Informe o número de eleitores que vão votar hoje: '))
P = ''

print()

#Instrução para votar
print('\nVOTAÇÃO INDIVIDUAL - "BEM VINDO AO TRE - UNISA, ESCOLHA UMA DAS OPÇÕES:\n')
print('-----------Instruções para os votos-----------\n')
print('Responder o questionário digitando o númreo do seu candidato:\n')
print('Candidatos a prefeitura:')
print('Marcos 10 - Marcos Gabriel do partido - Algoritmo')
print('Andre 20 - André Garcia do partido - String')
print('Jesiel 30 - Jesiel Brandão do partido - Variável')
print()
print('Outras opções: ')
print('Branco - Voto branco, Digite: 0')
print('Nulo - Voto nulo, Digite: qualquer número\n')
print('Caso o número digitado seja diferente destes acima, seu voto será anulado.\n')
print('Caso marque [N] no campo de eleitor presente, os votos de prefeito e vereador serão anulados.\n')
print('Responda com S para sim e N para não')

# Eleitores
NumEl = 1
E = 0
cont = 1

print("------------------------------------------------------------------")
while S != Senha:
    S = int(input("Senha errada! mesário: Por favor digite sua senha novamente: "))
    print("------------------------------------------------------------------")
    print("\nEleitor escolha uma opção abaixo: \n")
while cont <= Q:
    print('\nEleitor {}\n'.format(NumEl))
    presente = input('Eleitor você deseja continuar [S/N]? ')
    if presente == 'n' or presente == 'N':
        NumEl += 1
        cont += 1
        Nulo += 1
    elif presente == 'S':
        while P != 'Marcos' and P != 'Anre' and P != 'Jesiel' and P != 'VotoBranco' and P != 'Nulo':
            P = input('\nEm quem você vai votar para Prefeito ? ')

            if P == 'C1':
                marcos += 1
            elif P == 'C2':
                andre += 1
            elif P == 'C3':
                jesiel += 1
            elif P == 'VB':
                VotoBranco += 1
            elif P == 'VN':
                Nulo += 1
            else:
                print('Código inválido, favor responder com (Marcos, Andre, Jesiel, VotoBranco, Nulo)')
            P = ''
            E += 1
            cont += 1
            NumEl += 1

if marcos == andre and marcos > jesiel and andre > jesiel:
    maiorp = 'empate'
    empate = 1
    Cand1 = 'Marcos'
    Cand2 = 'Andre'
elif marcos == jesiel and marcos > andre and jesiel > andre:
    maiorp = 'empate'
    empate = 1
    Cand1 = 'Marcos'
    Cand2 = 'Jesiel'
elif andre == jesiel and andre > marcos and jesiel > marcos:
    maiorp = 'empate'
    empate = 1
    Cand1 = 'Andre'
    Cand2 = 'Jesiel'
elif marcos > andre and marcos > jesiel:
    maiorp = 'Marcos'
elif andre > marcos and andre > jesiel:
    maiorp = 'Andre'
elif jesiel > marcos and jesiel > andre:
    maiorp = 'Jesiel'

totalVBeVNp = (VotoBranco + Nulo)

somavP = (marcos + andre + jesiel)


print('Total de eleitores que podem votar.......................................:', Q)
print('Total de eleitores que votaram...........................................:', E)
print('Total de eleitores que faltaram..........................................:', faltas)
print('Código de identificação RA usado na votação...............................:', Senha)
print('Total de votos em brancos e nulos, de candidatos à prefeitura............:', totalVBeVNp)
print('Total de votos apurados para prefeito....................................:', somavP)
print("\nESTATÍSTICAS  DA ELEIÇÃO: ")
print('\nNúmero de votos para o Candidato C1.....................................:', marcos)
print('Número de votos para o Candidato C2.......................................:', andre)
print('Número de votos para o Candidato C3.......................................:', jesiel)
print()
print("Votos Nulos e Branco: ")
print('Total de votos em brancos e nulos, de candidatos à prefeitura............:', totalVBeVNp)
print('Número de votos brancos para candidatos à prefeitura......................:', VotoBranco)
print('Número de votos nulos para candidatos à prefeitura........................:', Nulo)

print('\nCandidato a Prefeito mais votado.........................................:', maiorp)

print("\nFIM DAS ELEIÇÔES PARA PREFEITO DE TERMINAL, A SEÇÂO ACABOU!\n")


if empate != 1:
    print('\n')
elif empate == 1:
    print("Segundo Turno! Houve empate de votação entre {} e {}.".format(Cand1, Cand2))
    NumEl = 0
    cont = 1
    while cont <= Q:
        print('Responda com S para sim e N para não')
        print('Eleitor {}'.format(NumEl + 1))
        presente = input('Votar no Segundo Turno [S/N]? ')
        if presente == 'n' or presente == 'N':
            faltas += 1
            NumEl += 1
            cont += 1
        elif presente == 'S' or presente == 's':
            while Voto != Cand1 and Voto != Cand2:
                Voto = input('Você deseja votar no candidato {} ou {}? '.format(Cand1, Cand2))
                if Voto == Cand1:
                    Voto1 += 1
                    NumEl += 1
                    cont += 1
                elif Voto == Cand2:
                    Voto2 += 1
                    NumEl += 1
                    cont += 1
                else:
                    print('Código inválido, favor responder com {} ou {} (MAIUSCULO)'.format(Cand1, Cand2))
            Voto = ''
    if Voto1 > Voto2:
        print('O novo Prefeito de Terminal é {}'.format(Cand1))

    elif Voto1 < Voto2:
        print('O novo Prefeito de Terminal é {}'.format(Cand2))

    print('Votos para o candidato {}: {} '.format(Cand1, Voto1))
    print('Votos para o candidato {}: {}'.format(Cand2, Voto2))