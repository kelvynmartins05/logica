# Solicita ao usuário que insira o consumo em metros cúbicos
consumo_str = input("Digite o consumo de água em m3: ")

# Converte a entrada para um número decimal (float)
try:
    consumo = float(consumo_str)
    
    # Verifica se o valor digitado é válido (não pode ser negativo)
    if consumo < 0:
        print("Erro: O consumo de água não pode ser negativo.")
    else:
        # Estrutura de decisão para calcular o valor da conta
        if consumo <= 10:
            valor_conta = 7.59
        elif consumo <= 20:
            valor_conta = consumo * 1.31
        elif consumo <= 30:
            valor_conta = consumo * 4.64
        elif consumo <= 50:
            valor_conta = consumo * 6.62
        else: # Acima de 50m3
            valor_conta = consumo * 7.31
        
        # Exibe o resultado formatado com duas casas decimais
        print(f"O valor da conta de água é: R$ {valor_conta:.2f}")

except ValueError:
    print("Erro: Por favor, digite um valor numérico válido.")
