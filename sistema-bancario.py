menu = """
    Menu!!!

    [1] sacar
    [2] depositar
    [3] Extrato
    [0] Sair

"""

saldo = 0
extrato = []
quantidade_saque = 0
LIMITE_SAQUE = 3

while True:
    opcao = int(input(menu))
    print(opcao)

    if opcao == 1:

        saque = float(input('Valor do saque: '))

        if quantidade_saque == 3:

            print('Já atingiu o limite de saque diario!')

        elif saque > 500:

            print('Limite maximo de saque é de R$ 500.00')
        
        elif saque > saldo:

            print('Saldo insuficente!')
        
        elif saque <= saldo:
            print('Aguarde a contagem do dinheiro!')
            print(f'Sacado: R$ {saque:.2f}')
            saldo -= saque
            quantidade_saque += 1
            descricao_saque = f'Saque no valor R$ {saque:.2f}'
            extrato.append(descricao_saque)

        else:
            print('Por favor, digite um valor válido para o saque.')
    
    elif opcao == 2:

        deposito = float(input('Valor do deposito:'))

        if deposito > 0:

            print(f'Deposito no valor de R$ {deposito:.2f} efetuado com sucesso!')
            saldo += deposito
            descricao_deposito = f'Deposito no valor R$ {deposito:.2f}'
            extrato.append(descricao_deposito)

        else:
            print('Por favor, digite um valor válido para o deposito.')
    
    elif opcao == 3:

        print(f'Seu saldo atual é de R$ {saldo:.2f}\n')
            
        if len(extrato) == 0:
            print(f'##### Seu extrato bancario: #####\n')
            print('Nenhuma transação efetuada no momento!!')
        
        else:
            print(f'##### Seu extrato bancario: #####\n')
            for ext in extrato:
                print(ext)

    elif opcao == 0:
        break

    else:
        print('Por favor, digite uma opção válida!!.')