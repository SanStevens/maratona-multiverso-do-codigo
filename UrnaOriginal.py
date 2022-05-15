#Variaveis

maiorp = 'SEM VOTOS'
maiorv = 'SEM VOTOS'
faltas = 0

#Candidatos a Prefeitos
C1 = C2 = C3 = C4 = VBP = VNP = 0
Z = ''

#Candidatos a Vereador
V1 = V2 = V3 = V4 = VBV = VNV = 0

#Empate
empate = 0
Cand1 = ''
Cand2 = ''
Voto = ''
Voto1 = 0
Voto2 = 0

#Código

print('\n1º ELEIÇÃO DA CIDADE TERMINAL - SEJA BEM VINDO - TRE da UNISA \n')
Q = int(input('Informe o número de eleitores que vão votar hoje: '))
C = int(input('Seu Código de Identificação RA da UNISA: '))
P = ''
V = ''

# Eleitores
NumEl = 1
E = 0
cont = 1
print('\nVOTAÇÃO INDIVIDUAL - "BEM VINDO AO TRE - UNISA, ESCOLHA UMA DAS OPÇÕES:\n')
print('Instruções para os votos\n')
print('Responder o questionário com as seguintes siglas com letras MAIÚSCULAS:\n')
print('Candidatos a prefeitura:\n')
print('C1 - Marcos Gabriel do partido - Algoritmo')
print('C2 - André Garcia 2 do partido - String')
print('C3 - Jesiel Brandão do partido - Variável')
print('C4 - Professor João Roberto do partido - Unisa\n')
print('Candidatos a vereador:\n')
print('V1 - Diego Dias Rocha do partido - Tutor')
print('V2 - Python do partido - Linguagem')
print('V3 - Srta. Nota do partido - Projeto')
print('V4 - Tipo Inteiro do partido - Int\n')
print('Outras opções\n')
print('VB - Voto branco')
print('VN - Voto nulo\n')
print('Caso a sigla digitada seja diferente destas acima, apresentará mensagem de código inválido e deverá inserí-la novamente.\n')
print('Caso marque [N] no campo de eleitor presente, os votos de prefeito e vereador serão anulados.\n')
print('Responda com S para sim e N para não')
while cont <= Q:
    print('\nEleitor {}\n'.format(NumEl))
    presente = input('Eleitor você deseja continuar [S/N]? ')
    if presente == 'n' or presente == 'N':
        faltas += 1
        NumEl += 1
        cont += 1
        VNP += 1
        VNV +=1
    elif presente == 'S':
        while P != 'C1' and P != 'C2' and P != 'C3' and P != 'C4' and P != 'VB' and P != 'VN':
            P = input('\nEm quem você vai votar para Prefeito ? ')

            if P == 'C1':
                C1 += 1
            elif P == 'C2':
                C2 += 1
            elif P == 'C3':
                C3 += 1
            elif P == 'C4':
                C4 += 1
            elif P == 'VB':
                VBP += 1
            elif P == 'VN':
                VNP += 1
            else:
                print('Código inválido, favor responder com (C1, C2, C3, C4, VB, VN)')
        P = ''

        while V != 'V1' and V != 'V2' and V != 'V3' and V != 'V4' and V != 'VB' and V != 'VN':
            V = input('Em quem você vai votar para Vereador ?  ')
            if V == 'V1' or V == 'v1':
                V1 += 1
            elif V == 'V2' or V == 'v2':
                V2 += 1
            elif V == 'V3' or V == 'v3':
                V3 += 1
            elif V == 'V4' or V == 'v4':
                V4 += 1
            elif V == 'VB' or V == 'vb':
                VBV += 1
            elif V == 'VN' or V == 'vn':
                VNV += 1
            else:
                print('Código inválido, favor responder com (V1, V2, V3, V4, VB, VN )')
        V = ''
        E += 1
        cont += 1
        NumEl += 1

    print("\n.::ENCERRAMENTO DAS VOTAÇÕES:.\n")

if C1 == C2  and C1 > C3 and C1 > C4 and C2 > C3 and C2 > C4:
    maiorp = 'empate'
    empate = 1
    Cand1 = 'C1'
    Cand2 = 'C2'
elif C1 == C3  and C1 > C2 and C1 > C4 and C3 > C2 and C3 > C4:
    maiorp = 'empate'
    empate = 1
    Cand1 = 'C1'
    Cand2 = 'C3'
elif C1 == C4  and C1 > C2 and C1 > C3 and C4 > C2 and C4 > C3:
    maiorp = 'empate'
    empate = 1
    Cand1 = 'C1'
    Cand2 = 'C4'
elif C2 == C3 and C2 > C1 and C2 > C4 and C3 > C1 and C3 > C4:
    maiorp = 'empate'
    empate = 1
    Cand1 = 'C2'
    Cand2 = 'C3'
elif C2 == C4 and C2 > C1 and C2 > C3 and C4 > C1 and C4 > C3:
    maiorp = 'empate'
    empate = 1
    Cand1 = 'C2'
    Cand2 = 'C4'
elif C3 == C4 and C3 > C1 and C3 > C2 and C4 > C1 and C4 > C2:
    maiorp = 'empate'
    empate = 1
    Cand1 = 'C3'
    Cand2 = 'C4'
elif C1 > C2 and C1 > C3 and C1 > C4:
    maiorp = 'C1'
elif C2 > C1 and C2 > C3 and C2 > C4:
    maiorp = 'C2'
elif C3 > C1 and C3 > C2 and C3 > C4:
    maiorp = 'C3'
elif C4 > C1 and C4 > C2 and C4 > C3:
    maiorp = 'C4'

if V1 > V2 and V1 > V3 and V1 > V4:
    maiorv = 'V1'
elif V2 > V1 and V2 > V3 and V2 > V4:
    maiorv = 'V2'
elif V3 > V1 and V3 > V2 and V3 > V4:
    maiorv = 'V3'
elif V4 > V1 and V4 > V2 and V4 > V3:
    maiorv = 'V4'


totalVBeVNp = (VBP + VNP)
totalVBeVNv = (VBV + VNV)

somavP = (C1 + C2 + C3 + C4)
somavV = (V1 + V2 + V3 + V4)


print('Total de eleitores que podem votar.......................................:', Q)
print('Total de eleitores que votaram...........................................:', E)
print('Total de eleitores que faltaram..........................................:', faltas)
print('Código de identificação RA usado na votação...............................:', C)
print('Total de votos em brancos e nulos, de candidatos à prefeitura............:', totalVBeVNp)
print('Total de votos em brancos e nulos, de candidatos a vereador..............:', totalVBeVNv)
print('Total de votos apurados para prefeito....................................:', somavP)
print('Total de votos apurados para vereador....................................:', somavV)

print('\nNúmero de votos para o Candidato C1.....................................:', C1)
print('Número de votos para o Candidato C2.......................................:', C2)
print('Número de votos para o Candidato C3.......................................:', C3)
print('Número de votos para o Candidato C4.......................................:', C4)
print('Número de votos brancos para candidatos à prefeitura......................:', VBP)
print('Número de votos nulos para candidatos à prefeitura........................:', VNP)

print('\nNúmero de votos para o Candidato V1.....................................:', V1)
print('Número de votos para o Candidato V2.......................................:', V2)
print('Número de votos para o Candidato V3.......................................:', V3)
print('Número de votos para o Candidato V4.......................................:', V4)
print('Número de votos brancos para candidatos a vereador........................:', VBV)
print('Número de votos nulos para candidatos a vereador..........................:', VNV)

print('\nCandidato a Prefeito mais votado.........................................:', maiorp)
print('Candidato a Vereador mais votado..........................................:', maiorv)

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