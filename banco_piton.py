#banco piton
#NOVO DESAFIO: FUNÇÃO EXTRATO, SAQUE E DEPÓSITO AGORA DEVERÃO SE TORNAR FUNÇÕES
titulo = " BANCO PÍTON "
caractere = "#"
saldo = 0
extrato = ""
limite_saques = 3

clientes = {"clientes": []}


def pressione_enter():
    input("Pressione Enter para continuar...")

def funcao_bank ():
    print (titulo.center (30, "-"))
    print (("Bem vindo!").center (30, "-"))
    print (caractere.center (30, "-"))
    print ("Pressione [1] para DEPOSITAR\n")
    print ("Pressione [2] para SACAR\n")
    print ("Pressione [3] para consultar EXTRATO\n")
    print ("Pressione [4] para CRIAR USUÁRIO\n")
    print ("Pressione [0] para SAIR")
    print (caractere.center (30, "-"))

def funcao_deposito (saldo, extrato, cpf,/):
    valor_deposito = (float(input(f"CPF: {cpf} \nEscolha um valor para DEPOSITAR: R$")))

    if valor_deposito > 0:
    
        saldo += valor_deposito 
        extrato += f"Depósito: R${valor_deposito:.2f}\n"
        print (f"Depositado com sucesso! Seu novo saldo é: R${saldo:.2f}")
        pressione_enter()
    else: 
        print("Valor inválido para depósito.")
        pressione_enter()
    return saldo, extrato

def funcao_sacar (*, limite_saque, numero_saques, limite_valor_saque, saldo, extrato, cpf):
    valor_sacar = (float(input(f"CPF: {cpf} \nEscolha um valor para SACAR: R$")))
    if valor_sacar > saldo:
        print (f"Você não possui saldo suficiente!")
        pressione_enter()

    elif numero_saques >= limite_saque:
        print(f"Limite de saques diários ({limite_saque}) atingido!")
        pressione_enter()

    elif valor_sacar > limite_valor_saque:
        print (f"Você não pode sacar um valor acima de R${limite_valor_saque:.2f}!")
        pressione_enter()

    elif valor_sacar > 0:
        saldo -= valor_sacar
        extrato += f"Saque: R${valor_sacar:.2f}\n"
        numero_saques += 1
        print (f"Saque efetuado com sucesso! Seu novo saldo é: R${saldo:.2f}")
        print(f"Você ainda pode fazer {limite_saque - numero_saques} saque(s) hoje.")
        pressione_enter()  
        return saldo, extrato, numero_saques          
        
    else:
        print (f"R${valor_sacar:.2f} é inválido!")
        pressione_enter()

def funcao_extrato (saldo, extrato, cpf):
    print (caractere.center (30, "-"))
    print ("--- EXTRATO ---")
    print(extrato if extrato else "Não foram realizadas movimentações.")
    print (f"Seu saldo é: R${saldo}")
    print (caractere.center (30, "-"))
    pressione_enter()
    

while True:

    funcao_bank()
    choice = int (input("Escolha uma das opções para começar: "))

    if choice == 1:
        cpf_cliente = input("Digite o CPF do cliente: ")
        cliente_encontrado = None
        for cliente in clientes["clientes"]:
            if cliente["cpf"] == cpf_cliente:
                cliente_encontrado = cliente
            break
        if cliente_encontrado:
            saldo, extrato = funcao_deposito(saldo, extrato, cpf_cliente)
        else:
            print("Cliente não encontrado!")
            pressione_enter()
            continue

    elif choice == 2:
        cpf_cliente = input("Digite o CPF do cliente: ")
        cliente_encontrado = None
        for cliente in clientes["clientes"]:
            if cliente["cpf"] == cpf_cliente:
                cliente_encontrado = cliente
                break
        if cliente_encontrado:
            saldo, extrato, numero_saques = funcao_sacar (
                limite_saque = limite_saques,
                numero_saques = numero_saques,
                limite_valor_saque = 1000,
                saldo = saldo,
                extrato = extrato,
                cpf = cpf_cliente
            )

        else:
            print("Cliente não encontrado!")
            pressione_enter()
            continue
            
    elif choice == 3:
        
        cpf_cliente = input("Digite o CPF do cliente: ")
        cliente_encontrado = None
        for cliente in clientes["clientes"]:
            if cliente["cpf"] == cpf_cliente:
                cliente_encontrado = cliente
            break
        if cliente_encontrado:
            saldo, extrato = funcao_extrato(saldo, extrato, cpf_cliente)
        else:
            print("Cliente não encontrado!")
            pressione_enter()
            continue

    elif choice == 4:
        print(caractere.center(30, "="))
        nome = input("Digite o nome do cliente: ")
        cpf = input("Digite o CPF do cliente: ")
        endereço = input ("Digite o endereço do cliente: ")

        
        cpf_existe = False
        for cliente in clientes["clientes"]:
            if cliente["cpf"] == cpf: 
                cpf_existe = True
                break

        if cpf_existe:
            print("Já existe um cliente com esse CPF!")
            pressione_enter()
            continue
        else:
            novo_cliente = {"nome": nome, "cpf": cpf}
            clientes["clientes"].append(novo_cliente)  
            print("Cliente adicionado com sucesso!")
            pressione_enter()
            continue


    elif choice == 0:
        print ("Obrigado por usar o BANCO PÍTON!")
        break

    else: 
        print ("Opção inválida!")
        pressione_enter()
        continue


    
