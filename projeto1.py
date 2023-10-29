#Criando um sistema bancário com Python

menu = """

##### MENU #####

Escolha o que deseja fazer:

1 - Depositar

2 - Sacar

3 - Ver Extrato

0 - Sair


"""
print(menu)

saldo = 0
limite_saldo = 500
extrato = ""
numero_de_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = int(input("Escolha o que deseja fazer. Digite 1 para Depositar/2 para Sacar/3 para ver Extrato/0 para sair do sistema: "))
    if opcao == 1:
        depositar = float(input("Informe quanto deseja depositar: R$"))
        if depositar > 0:
            if saldo + depositar <= limite_saldo:
                saldo += depositar
                extrato += f"Depósito: R${depositar}\n"
                print("Muito Obrigado!" f"Você acaba de depositar R${depositar}.")
            else:
                print(f"O depósito excede o limite de saldo de R${limite_saldo}.")
        else:
            print("Você selecionou um valor inexistente para deposito. Verifique se você não selecionou 0 ou algum valor negativo.")
    elif opcao == 2:
        if numero_de_saques < LIMITE_SAQUES:  
            sacar = float(input("Informe quanto você deseja sacar: R$"))
            if sacar <= saldo:  
                saldo -= sacar  
                extrato += f"Saque: R${sacar}\n"
                numero_de_saques += 1  
                print("Muito Obrigado!" f"Você acaba de sacar R${sacar}.")
            else:
                print("Saldo insuficiente. Não é possível sacar esse valor.")
        elif numero_de_saques >= LIMITE_SAQUES:
            print(f"Você atingiu o limite de saques ({LIMITE_SAQUES}).")
        elif saldo <= 0:
            print("Não há saldo disponível para saque.")

    elif opcao == 3:
        print(f"""Muito Obrigado! Aqui está seu extrato:

{extrato}
Saldo Atual: R${saldo}
""")

    elif opcao == 0:
        print("Muito Obrigado! Você saiu do sistema com sucesso.")
        break