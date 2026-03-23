consumo = input("Digite o consumo de água em m3: ")

try:
    consumo = float(consumo)
    
    if consumo < 0:
        print("Erro: O consumo de água não pode ser negativo.")
    else:
        
        if consumo <= 10:
            valor_conta = 44.95
        elif consumo <= 20:
            valor_conta = consumo * 8.75
        elif consumo <= 50:
            valor_conta = consumo * 16.76
        else: 
            valor_conta = consumo * 17.46
        
        
        print(f"O valor da conta de água é: R$ {valor_conta:.2f}")

except ValueError:
    print("Erro: Por favor, digite um valor numérico válido.")
