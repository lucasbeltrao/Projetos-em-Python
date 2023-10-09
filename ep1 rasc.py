# Função para calcular o saldo
def calcula_saldo(V, D, M, J):
    cont_mes = 0
    S_m = 0
    S = V 

    if 0.01 <= J <= 1 and 12 <= M <= 360 and V >= 1000:
        while cont_mes < M: 
            S_m += D  
            S_m *= (1 + J)  
            cont_mes += 1
        S += S_m
        S = round(S, 2)
    else:
        S = "Valores de entrada inválidos."

    return S

# Função para calcular notas e moedas
def calcula_notas(S):
    notas = [100, 50, 10, 2]
    moedas = [1, 0.5, 0.1, 0.01]
    resultado = {}

    if S < 0:
        return "Saldo inválido."
    
    for nota in notas:
        quantidade_notas = S // nota
        if quantidade_notas > 0:
            resultado[f'{quantidade_notas} nota(s) de {nota} reais'] = int(quantidade_notas)
            S -= quantidade_notas * nota

    for moeda in moedas:
        quantidade_moedas = S // moeda
        if quantidade_moedas > 0:
            if moeda >= 1:
                resultado[f'{quantidade_moedas} moeda(s) de {int(moeda)} reais'] = int(quantidade_moedas)
            else:
                resultado[f'{quantidade_moedas} moeda(s) de {int(moeda * 100)} centavos'] = int(quantidade_moedas)
            S -= quantidade_moedas * moeda

    return resultado

# Solicita as entradas do usuário
V = float(input("Digite o valor do depósito inicial: "))
D = float(input("Digite o valor dos depósitos mensais: "))
M = int(input("Digite a quantidade de meses: "))
J = float(input("Digite a taxa de juros mensal: "))

# Chamando a função para calcular o saldo final
saldo_final = calcula_saldo(V, D, M, J)

if saldo_final == "Valores de entrada inválidos.":
    print(saldo_final)
else:
    resultado_notas_moedas = calcula_notas(saldo_final)
    if resultado_notas_moedas == "Saldo inválido.":
        print(resultado_notas_moedas)
    else:
        print(f"Após {M} meses, o saldo final foi de {saldo_final} reais.")
        print("Os", saldo_final, "reais foram sacados com:")
        for item, quantidade in resultado_notas_moedas.items():
            if "moeda" not in item:
                print(f'{item}')
            else:
                print(f'{item}')