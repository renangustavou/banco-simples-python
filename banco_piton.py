#banco piton
titulo = " BANCO PÍTON "
caractere = "#"
saldo = 0
limite_saque = 3
limite_valor_saque = 1000
extrato = ""
numero_saques = 0 
nome_cliente = input ("Insira seu nome: ")
mensagem_inicio = f"Bem-vindo, {nome_cliente}!"

def pressione_enter():
    input("Pressione Enter para continuar...")

def funcao_bank ():
    print (titulo.center (30, "-"))
    print (mensagem_inicio.center (30, "-"))
    print (caractere.center (30, "-"))
    print ("Pressione [1] para DEPOSITAR\n")
    print ("Pressione [2] para SACAR\n")
    print ("Pressione [3] para EXTRATO\n")
    print ("Pressione [0] para SAIR")
    print (caractere.center (30, "-"))

while True:

    funcao_bank()
    choice = int (input("Escolha uma das opções para começar: "))

    if choice == 1:
        valor_deposito = (float(input("Escolha um valor para depositar R$")))

        if valor_deposito > 0:
            extrato += f"Depósito: R${valor_deposito:.2f}\n"
            saldo += valor_deposito
            print (f"Depositado com sucesso! Seu novo saldo é: R${saldo:.2f}")
            pressione_enter()
            continue

    elif choice == 2:
        valor_sacar = (float(input("Escolha um valor para sacar R$")))

        if valor_sacar > saldo:
            print (f"Você não possui saldo suficiente!")
            pressione_enter()
            continue

        elif numero_saques >= limite_saque:
            print(f"Limite de saques diários ({limite_saque}) atingido!")
            pressione_enter()
            continue

        elif valor_sacar > limite_valor_saque:
            print (f"Você não pode sacar um valor acima de R${limite_valor_saque:.2f}!")
            pressione_enter()
            continue

        elif valor_sacar > 0:
            saldo -= valor_sacar
            extrato += f"Saque: R${valor_sacar:.2f}\n"
            numero_saques += 1
            print (f"Saque efetuado com sucesso! Seu novo saldo é: R${saldo:.2f}")
            print(f"Você ainda pode fazer {limite_saque - numero_saques} saque(s) hoje.")
            pressione_enter()
            continue
        
        else:
            print (f"R${valor_sacar:.2f} é inválido!")
            pressione_enter()
            continue
            
    elif choice == 3:
        print (caractere.center (30, "-"))
        print ("--- EXTRATO ---")
        print(extrato if extrato else "Não foram realizadas movimentações.")
        print (f"Seu saldo é: R${saldo}")
        print (caractere.center (30, "-"))
        pressione_enter()
        continue

    elif choice == 0:
        print ("Obrigado por usar o BANCO PÍTON!")
        break

    else: 
        print ("Opção inválida!")
        pressione_enter()
        continue
    