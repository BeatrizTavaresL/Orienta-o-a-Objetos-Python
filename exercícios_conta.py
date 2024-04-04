def criar_conta(numero, titular, saldo, limite):
    conta = {
                "numero": numero,
                "titular": titular,
                "saldo": saldo,
                "limite": limite
            }
    return conta

conta = criar_conta(123, 'Beatriz', 22.00, 100.00)

def deposita(conta, valor):
    conta["saldo"] += valor

def saque(conta, valor):
    conta["saldo"] -= valor

def extrato(conta):
    print('Saldo é {}'.format(conta['saldo']))
