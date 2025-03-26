menu = """
----------- MENU -----------
[1] DEPOSITAR
[2] SACAR
[3] EXTRATO
[0] SAIR
----------------------------
=> """

limite = 500
extrato = ""
numero_de_Saques = 0
limite_de_saques = 3
deposito = []
saldo = 0
saques = []
valido = 1

while True:
    opcao = input(menu)

    if opcao == "1":

        deposita = float(input("qual valor deseja depositar?"))
        valor = deposita
        
        if valido <= deposita:
             print(f"depositando o valor R${deposita}")
             deposito.append(valor)
             saldo += deposita
        else:
             print("tente um valor valido")

    elif opcao == "2":

        sacar = float(input("qual valor deseja sacar?"))

        if valido >= sacar:
            print("digite um valor valido")

        elif numero_de_Saques < limite_de_saques and saldo >= sacar and limite >= sacar:
                print(f"sacando o valor R${sacar}")
                saques.append(sacar)
                numero_de_Saques += 1

        elif numero_de_Saques >= limite_de_saques:
            print(f"O valor R${sacar} não pode ser sacado devido ao limite de saques do dia")

        else:
            print("você não tem saldo para esse saque ou o valor do saque é superior ao permitido")

    elif opcao == "3":
        print("-----------EXTRATO-----------")
        
        for valores_2 in deposito:
             print("Depositou R$",valores_2)

        for valores in saques:
                print("Sacou R$",valores)
        total_Depositos = sum(deposito)
        total_saques = sum(saques)
        saldo = total_Depositos - total_saques
        print(f"TOTAL: R${saldo}")
        print("-----------------------------")

    elif opcao == "0":
        break

    else:
        print("escolha uma opção valida")
