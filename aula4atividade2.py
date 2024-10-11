'''def calcular_caixas_azulejos():
    # Lendo as dimensões da cozinha
    comprimento = float(input("Digite o comprimento da cozinha (em metros): "))
    largura = float(input("Digite a largura da cozinha (em metros): "))
    altura = float(input("Digite a altura da cozinha (em metros): "))
    
    # Calculando a área total das paredes
    area_parede1 = altura * comprimento  # parede maior
    area_parede2 = altura * largura       # parede menor

    # Existem 2 paredes de cada tipo
    area_total_paredes = 2 * (area_parede1 + area_parede2)

    # Cada caixa de azulejos cobre 1,5 m²
    area_por_caixa = 1.5
    quantidade_caixas = area_total_paredes / area_por_caixa

    # Arredondando para cima para garantir que tenha azulejos suficientes
    quantidade_caixas = int(quantidade_caixas) + (1 if quantidade_caixas % 1 > 0 else 0)

    # Exibindo o resultado
    print(f"A quantidade de caixas de azulejos necessárias é: {quantidade_caixas}")

# Chamando a função
calcular_caixas_azulejos()'''