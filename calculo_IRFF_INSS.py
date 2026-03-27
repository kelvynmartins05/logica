salario_bruto = float(input("Digite o valor do salário bruto (R$): "))

# Alíquotas simplificadas
aliquota_inss = 0.11  # 11%
aliquota_irrf = 0.075 # 7,5%

# Cálculos
desconto_inss = salario_bruto * aliquota_inss
# O IRRF geralmente incide após o desconto do INSS
desconto_irrf = (salario_bruto - desconto_inss) * aliquota_irrf
salario_liquido = salario_bruto - desconto_inss - desconto_irrf

# Exibição dos resultados
print("-" * 30)
print(f"Salário Bruto: R$ {salario_bruto:.2f}")
print(f"Desconto INSS (11%): R$ {desconto_inss:.2f}")
print(f"Desconto IRRF (7,5%): R$ {desconto_irrf:.2f}")
print("-" * 30)
print(f"Salário Líquido: R$ {salario_liquido:.2f}")
