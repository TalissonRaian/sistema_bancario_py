from datetime import datetime
agora = datetime.now()
data_formatada = agora.strftime("%Y-%m-%d")


saldo = 0
limite = 500
extrato = []
numero_de_saque = 0
limite_de_saque = 3

menu = '''
|========MENU==========|
|1 - Consultar Extrato |
|2 - Realizar Deposito |
|3 - Realiza Saque     |
|4 - Finalizar         |
||||||||||||||||||||||||
'''

while True:
    opcao = input(menu)

    if opcao == '1':
        print(f'Seu saldo e de R$:{saldo:.2f}')
        print('Extrato:')
        for operacao in extrato:
            print(operacao)

    elif opcao == '2':
        deposito = float(input('Digite o valor que deseja depositar: R$:'))
        if deposito > 0:
            saldo += deposito
            extrato.append(f'{data_formatada} Deposito realizado valor R$:{deposito:.2f}')
            print(f'Deposito no valor de R$:{deposito:.2f} Realizado com sucesso!')

    elif opcao == '3':
        if numero_de_saque < limite_de_saque:
            saque = float(input("Digite o valor que deseja sacar R$:"))
            if saque <= limite:
                saldo -= saque
                extrato.append(f'Saque realizado valor R$:{saque:.2f}')
                numero_de_saque += 1
                print(f'Saque no valor de R${saque:.2f} Realizado com sucesso!')
            else:
                print('Valor superior ao limite de saque')
        else:
            print('Limite de saques diários atingido.')
    elif opcao == '4':
        print('App Finalizado!')
        break
    else:
        print("Opção invalida")

