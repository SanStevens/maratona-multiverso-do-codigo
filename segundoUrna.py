print("\n 1º ELEIÇÃO DA CIDADE TERMINAL - SEJA BEM VINDO - TRE da UNISA ")

#Candidatos a Prefeitos
marcos = andre = jesiel = VotoBranco = Nulo = 0
Z = ''

#Candidatos a Prefeito e senha
Senha = 1234
marcos = 10
andre= 20
jesiel= 30
Branco = 0
Voto = 0
Nulo = 0
Votomarcos = 0
Votoandre = 0
Votojesiel = 0
VotoBranco = 0

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

#Eleitores
NumEl = 1
E = 0
cont = 1

print("------------------------------------------------------------------")
while S != Senha:
    S = int(input("Senha errada! mesário: Por favor digite sua senha novamente: "))
    print("------------------------------------------------------------------")
    print("\nEleitor escolha uma opção abaixo: \n")
while(1):
    print("Para votar no candidato marcos, digite", marcos, "\nPara votar no candidato andre, digite", andre, "\nPara votar no candidato jesiel, digite", jesiel, "\nPara votar em BRANCO, digite",Branco,"\n")
    print("\n--------Digite o número do seu candidato--------\n")
    Voto = int(input("Vote no seu candidato: "))

    if Voto == marcos:
        print("Você deseja votar no canditado - Marcos (10)?")
    elif Voto == andre:
        print("Você deseja votar no canditado - Andre (20)?")
    elif Voto == jesiel:
        print("Você deseja votar no canditado - Jesiel (30)?")
    elif Voto == Branco:
        print("Você deseja votar em Branco?")
    else:
        print("Você deseja votar Nulo?")

    Cv = int(input("1: Confirmar \n0: Corrigir\n"))

    if Cv != 1:
        print("\nCorrija seu voto!\n")
    else:
        S = int(input("Digite sua senha para confirmar: "))
        while S != Senha:
            S = int(input("Senha errada! Digite sua senha novamente: "))
        if Voto == 10:
            Votomarcos += 1
        elif Voto == 20:
            Votoandre += 1
        elif Voto == 30:
            Votojesiel += 1
        elif Voto == 0:
            VotoBranco += 1
        else:
            Nulo += 1
        print("Voto computado com sucesso!\n")

        Vn = int(input("Deseja votar novamente?\n1: Para votar novamente \n0: Para encerrar\n"))

        E += 1
        cont += 1
        NumEl += 1

        if Vn != 1:
            print("------------------------------------------------------------------")
            S = int(input("Digite sua senha para encerrar a sessão de votos: \n"))
            print("------------------------------------------------------------------")
            while S != Senha:
                S = int(input("Senha errada! Digite sua senha novamente: "))
            VtV = Votomarcos + Votoandre + Votojesiel
            Pvmarcos = Votomarcos / VtV * 100
            Pvandre = Votoandre / VtV * 100
            Pvjesiel = Votojesiel / VtV * 100

            if Pvmarcos > 50:
                print("\nMarcos 10 - venceu a eleição e foi eleito novo prefeito de Terminnal!\n" )
            elif Pvandre > 50:
                print("\nAndre 20 - venceu a eleição e foi eleito novo prefeito de Terminnal!\n")
            elif Pvjesiel > 50:
                print("\nJesiel 30 - venceu a eleição e foi eleito novo prefeito de Terminnal!\n")
            else:
                print("\nEmpate - A eleição irá para o Segundo Turno!\n")

            totalVBeVNp = (VotoBranco + Nulo)

            print('Total de eleitores que se increveram para votar.......................................:', Q)
            print('Total de eleitores que votaram...........................................:', E)
            print("\nESTATÍSTICAS  DA ELEIÇÃO: ")
            print('O candidato Marcos 10, teve....................................:', Pvmarcos, "% Porcento - Dos votos")
            print('O candidato Andre 20, teve.......................................:', Pvandre, "% Porcento - Dos votos")
            print('O candidato Jesiel 30, teve.......................................:', Pvjesiel, "% Porcento - Dos votos")
            print()
            print("Votos Nulos e Branco: ")
            print('Total de votos em brancos e nulos, de candidatos à prefeitura............:', totalVBeVNp)
            print('Número de votos brancos para candidatos à prefeitura......................:', VotoBranco)
            print('Número de votos nulos para candidatos à prefeitura........................:', Nulo)

            print("\nFIM DAS ELEIÇÔES PARA PREFEITO DE TERMINAL, A SEÇÂO ACABOU!\n")
            break

