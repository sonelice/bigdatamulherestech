'''def calcular_lampadas(potencia_lampada, largura, comprimento):
    # Calcula a área do cômodo
    area = largura * comprimento

    # Potência necessária (em watts) para a área do cômodo
    potencia_necessaria = area * 3  # 3 watts por m²

    # Número de bocais necessários (1 bocal a cada 3 m²)
    num_bocais = area // 3

    # Calcula o número de lâmpadas necessárias
    if potencia_lampada > 0:
        # Lâmpadas necessárias para atender a potência
        num_lampadas = -(-potencia_necessaria // potencia_lampada)  # Arredondamento para cima
    else:
        num_lampadas = 0  # Se a potência da lâmpada for inválida

    return num_lampadas, num_bocais

# Dados de entrada
potencia_lampada = float(input("Digite a potência da lâmpada (em watts): "))
largura = float(input("Digite a largura do cômodo (em metros): "))
comprimento = float(input("Digite o comprimento do cômodo (em metros): "))

# Chamada da função
lampadas, bocais = calcular_lampadas(potencia_lampada, largura, comprimento)

# Impressão dos resultados
print(f"Número de lâmpadas necessárias: {lampadas}")
print(f"Número de bocais necessários: {bocais}")'''