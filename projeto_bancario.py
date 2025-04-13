def menu():
      return """
       ----------- MENU -----------
      [c] NOVA CONTA
      [0] NOVO USUARIO 
      [1] DEPOSITAR
      [2] SACAR
      [3] EXTRATO
      [4] SAIR
       ----------------------------
       => """
     
def novo_usuario():
    cpf = int(input("Seu CPF:"))
    return  cpf
def deposito():
     valor_depositar = float(input("qual valor deseja depositar?"))
     return valor_depositar
def saque():
     sacar = float(input("qual valor deseja sacar?"))
     return sacar


def main():
     limite = 500
     extrato = ""
     numero_de_Saques = 0
     limite_de_saques = 3
     saldo = 0
     menor_que = 1
     agencia = "0001"
     numero_da_conta = 0
     data_nascimento = 2021
     lista_deposito = []
     lista_saques = []
     lista_usuarios = []
     conta_corrente = []
     conta_poupanca = []
     conta_kids = []



     while True:
      opcao = input(menu())

      if opcao == "1":
          valor_depositar = deposito()
          valor = valor_depositar
          if valor_depositar >= menor_que:
             print(f"depositando o valor R${valor_depositar}")
             saldo += valor_depositar
             lista_deposito.append(valor)
          else:
             print("tente um valor valido")

      elif opcao == "0":
          cpf_ja_existe = False
          cpf = novo_usuario()
          for usuario in lista_usuarios:
              if usuario [0] == cpf:
                cpf_ja_existe = True
          if cpf_ja_existe:
              print("seu CPF já está na nossa base")
          else:
           usuario = input("Nome:")
           data_nascimento_usuario = input("Data de nascimento: EX: DIA/MÊS/ANO")
           endereço =input("Endereço: EX: LOGRADORO - NUMERO, BAIRRO, CIDADE, ESTADO E CEP")
           email = input ("Email:")
           print(f"Seu usuario foi criando {usuario}, no CPF {cpf}, vinculado ao Email {email}")
           dados_usuarios = cpf, usuario, data_nascimento_usuario, endereço, email
           lista_usuarios.append(dados_usuarios)

      elif opcao == "c":
          cpf_ja_existe = False
          login = int(input("Seu CPF:"))
          for usuario in lista_usuarios:
             if usuario [0] == cpf:
                cpf_ja_existe = True
          if cpf_ja_existe:
             tipo_de_conta = input("[c]conta corrente, [p]conta poupança, [k]conta kids")
             if tipo_de_conta == "c":
                nome = input("Nome:")
                print ("Apenas numeros")
                telefone = int (input("Telefone:"))
                numero_da_conta +=1
                print(f"seu numero de conta corrente é {numero_da_conta} e a agencia é {agencia}")
                corrente = login,nome, telefone, numero_da_conta, agencia
                conta_corrente.append(corrente)

             elif tipo_de_conta == "p":
                nome_p = input("Nome:")
                print ("Apenas numeros")
                telefone_p = int (input("Telefone:"))
                numero_da_conta +=1
                print(f"seu numero de conta poupança é {numero_da_conta} e a agencia é {agencia}")
                poupanca = login, nome_p, telefone_p
                conta_poupanca.append(poupanca)

             elif tipo_de_conta == "k":
                nome_kids = input("Nome:")
                nome_pai = input("nome do pai:")
                nome_mae = input("nome da mãe:")
                print ("Apenas numeros")
                ano_de_nascimento = int(input("Ano de nascimento:"))
                if data_nascimento > ano_de_nascimento:
                  print("seu filho não tem idade para conta")
                else: 
                 print(f"seu numero da conta do seu filho é {numero_da_conta} e a agencia é {agencia}")
                 numero_da_conta +=1 
                 kids = login, nome_kids, nome_pai, nome_mae, ano_de_nascimento
                 conta_kids.append(kids)
                 print(conta_kids)

          else:
             print("Você não é nosso cliente, crie um usuario e depois uma conta.")
          print(conta_corrente)

      elif opcao == "2":
          sacar = saque()
          if sacar < menor_que:
            print("digite um valor valido")

          elif numero_de_Saques < limite_de_saques and saldo >= sacar and limite >= sacar:
                print(f"sacando o valor R${sacar}")
                numero_de_Saques += 1
                lista_saques.append(sacar)

          elif numero_de_Saques >= limite_de_saques:
            print(f"O valor R${sacar} não pode ser sacado devido ao limite de saques do dia")

          else:
            print("você não tem saldo para esse saque ou o valor do saque é superior ao permitido")

      elif opcao == "3":
          print("-----------EXTRATO-----------")
        
          for valores_2 in lista_deposito:
             print("Depositou R$",valores_2)
          for valores in lista_saques:
                print("Sacou R$",valores)
          total_Depositos = sum(lista_deposito)
          total_saques = sum(lista_saques)
          saldo = total_Depositos - total_saques
          print(f"TOTAL: R${saldo}")
        
          print("-----------------------------")

      elif opcao == "4":
        break

     else:
      print("escolha uma opção valida")
main()
