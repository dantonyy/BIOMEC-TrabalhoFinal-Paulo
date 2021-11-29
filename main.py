#coding: utf-8
"""
Faculdade de Medicina de Ribeirão Preto - Universidade de São Paulo (FMRP-USP)
Fundamentos de Informática em Biomecânica
Docente: Paulo Santiago
Discentes: Dantony de Castro B. Donato (11845581) & Maria Emília L. Castelucci (11812604)
"""

idade = int(input("Insira sua idade: "))
peso = int(input("Insira seu peso: "))
sexo = int(input("Digite 1 caso seja mulher e 2 caso seja homem: "))

#Menu
print('''[ 1 ] Calcular Gasto Energético Basal
[ 2 ] Gasto calórico Realizando corrida
[ 3 ] Gasto calórico Andando de bicicleta
[ 4 ] Gasto calórico Pulando corda
[ 5 ] Trocar informações de entrada (idade, peso e sexo)
[ 6 ] Sair do programa

OBS.: Você sempre será retornado para o menu principal ao realizar alguma ação. Caso desejar, para finalizar o programa, Digite 6.''')
opcao = 0
while opcao != 6:
    opcao = int(input('\nOpção desejada: '))
    if opcao == 1:
        if 0 < idade < 3:
            if sexo == 1:
                geb = (58.31 * peso) - 31.1
                print("\nSeu gasto energético basal é: ", geb, "kcal")
            if sexo == 2:
                geb = (59.512 * peso) - 30.4
                print("\nSeu gasto energético basal é: ", geb, "kcal")
        if 4 < idade < 10:
            if sexo == 1:
                geb = (20.315 * peso) + 485.9
                print("\nSeu gasto energético basal é: ", geb, "kcal")
            if sexo == 2:
                geb = (22.706 * peso) + 504.6
                print("\nSeu gasto energético basal é: ", geb, "kcal")
        if 11 < idade < 18:
            if sexo == 1:
                geb = (13.384 * peso) + 692.6
                print("\nSeu gasto energético basal é: ", geb, "kcal")
            if sexo == 2:
                geb = (17.686 * peso) + 692.2
                print("\nSeu gasto energético basal é: ", geb, "kcal")
        if 19 < idade < 30:
            if sexo == 1:
                geb = (14.818 * peso) + 486.6
                print("\nSeu gasto energético basal é: ", geb, "kcal")
            if sexo == 2:
                geb = (15.057 * peso) + 692.2
                print("\nSeu gasto energético basal é: ", geb, "kcal")
        if 31 < idade < 60:
            if sexo == 1:
                geb = (8.126 * peso) + 845.6
                print("\nSeu gasto energético basal é: ", geb, "kcal")
            if sexo == 2:
                geb = (11.472 * peso) + 873.1
                print("\nSeu gasto energético basal é: ", geb, "kcal")
        if idade >= 60:
            if sexo == 1:
                geb = (9.082 * peso) + 658.5
                print("\nSeu gasto energético basal é: ", geb, "kcal")
            if sexo == 2:
                geb = (11.711 * peso) + 587.7
                print("\nSeu gasto energético basal é: ", geb, "kcal")
    elif opcao == 2:
        vel = int(input("Insira a velocidade da corrida (em km/h): "))
        tempo = int(input("Insira o tempo de realização da atividade (em minutos): "))
        corrida = (peso * vel * 0.0175) * tempo
        print("\nNuma corrida de ", tempo," minutos, você perderá ", corrida, " kcal")
    elif opcao == 3:
        tempo = int(input("Insira o tempo de realização da atividade (em minutos): "))
        tempo2 = tempo/60
        metbike = 5.5
        bike = peso * metbike * tempo2
        print("Andando de bicicleta por ", tempo, " minutos você perderá ", bike, " kcal")
    elif opcao == 4:
        vel2 = int(input('''        [ 1 ] Velocidade Moderada
        [ 2 ] Velocidade Rápida
        Opcao: '''))
        tempo = int(input("Insira o tempo de realização da atividade (em minutos): "))
        tempo2 = tempo / 60
        if vel2 == 1:
            metcord = 10
            corda = metcord * tempo2 * peso
        elif vel2 == 2:
            metcord = 12
            corda = metcord * tempo2 * peso
        print("Pulando corda por ", tempo, " minutos, você perderá ", corda, " kcal")
    elif opcao == 5:
        idade = int(input("Insira sua idade: "))
        peso = int(input("Insira seu peso: "))
        sexo = int(input("Digite 1 caso seja mulher e 2 caso seja homem: "))