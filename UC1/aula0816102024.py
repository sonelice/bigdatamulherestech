# #Funções:

# def somar(parametro1,parametro2):
#     return(parametro1+parametro2)
# print(somar(20,30))

# def subtrair():
#     parametro1=int(input('número 1:'))
#     parametro2=int(input('número 2:'))
#     return parametro1-parametro2

# print(subtrair())

# #exemplo aula 

# 5) Escreva um programa que leia as notas das duas avaliações normais e a nota da avaliação optativa dos estudantes de uma turma. Caso o estudante não tenha feito a optativa, deve ser fornecido o valor -1. Calcular a média do semestre considerando que a prova optativa substitui a 
# # nota mais baixa entre as duas primeiras avaliações. Escrever a média e mensagens que indiquem se o estudante foi aprovado, reprovado ou se 
# # está em exame, de acordo com as informações abaixo: 
# # Aprovado: média >= 6.0, Reprovado: média < 3.0, Exame: média >= 3.0 e < 6.0;

# def boletim():
#     nota1=float(input('Primeira Nota:'))
#     nota2=float(input('Segunda Nota:'))
#     nota_opt=float(input('Nota Optativa:'))

#     if nota_opt != -1: 
#         menor_nota=min(nota1,nota2)
#         if nota_opt>menor_nota:
#             if nota1==menor_nota:
#                 nota1=nota_opt
#             else:
#                 nota2=nota_opt

#     media=(nota1+nota2)/2
#     print(f'Média:{media}')

#     if media >= 6.0:
#         print("Aprovado")
#     elif media < 3.0:  

#         print("Reprovado")
#     else:
#         print("Exame de Recuperação")

# boletim()

# #ATIVIDADE ASSISTIDA:

# #crie uma função para multiplicar dois números quaisquer:

# def multiplicar(num1=1,num2=2): #Default
#     num1=float(input('digite o primeiro número:'))
#     num2=float(input('digite o seguno número:'))
#     return f'o resultado dos dois números multiplicado é {num1*num2}.'

# print(multiplicar())''


# #ATIVIDADES 1

# #1) Um pescador precisa pagar uma multa caso o peso dos peixes exceda 100 quilos. Crie uma função para calcular a multa, se aplicável.

# def calcular_multa(peso_peixes):
#     limite_peso = 100  # Limite de peso em quilos
#     multa_por_quilo_excedente = 20 # Valor da multa por quilo excedente

#     if peso_peixes > limite_peso:
#         excesso = peso_peixes - limite_peso
#         multa = excesso * multa_por_quilo_excedente
#         return f'A multa a ser paga é: R$ {multa:.2f}.'
#     else:
#         return  f'Não possui multa' # Sem multa
    
# print(calcular_multa(10))

# Atividade 2
#  Crie um programa que faça a leitura da altura e do peso de N pessoas para o cálculo do IMC, mostrando ao final a classificação de acordo
# com a tabela de IMC.

# def calcular_imc(peso,altura): #https://aps.bvs.br/apps/calculadoras/?page=6
#     return peso / (altura ** 2)

# def classificar_imc(imc):
#     if imc < 18.5:
#         return "baixo peso"
#     elif 18.5 <= imc < 24.9:
#         return "Peso normal"
#     elif 25 <= imc < 29.9:
#         return "Sobrepeso"
#     elif 30 <= imc < 34.9:
#         return "Obesidade grau 1"
#     elif 35 <= imc < 39.9:
#         return "Obesidade grau 2"
#     else: 
#         return "Obesidade grau 3"

# def main():
#     n = int(input("Quantas pessoas você deseja cadastrar? "))
#     for i in range(n):
#         print(f"\nPessoa {i + 1}:")
#         peso = float(input("Digite o peso (kg): "))
#         altura = float(input("Digite a altura (m): "))
        
#         imc = calcular_imc(peso, altura)
#         classificacao = classificar_imc(imc)
        
#         print(f"IMC: {imc:.2f} - Classificação: {classificacao}")

# if __name__ == "__main__":
#     main()


#Atividade 3
 

# Função para exibir o cardápio
def exibir_cardapio():
    cardapio = {
        1: {"item": "Hambúrguer", "preco": 20.00},
        2: {"item": "Pizza", "preco": 30.00},
        3: {"item": "Salada", "preco": 15.00},
        4: {"item": "Suco", "preco": 8.00}
    }
    
    print("Cardápio:")
    for codigo, dados in cardapio.items():
        print(f"{codigo} - {dados['item']}: R${dados['preco']:.2f}")
    
    return cardapio

# Função para realizar o pedido (sem while, try, except ou break)
def realizar_pedido(cardapio, pedidos=[]):
    print("\nDigite o código do item que deseja pedir (0 para encerrar):")
    codigo = int(input())
    
    if codigo == 0:
        return pedidos  # Encerra quando o usuário digita 0
    
    if codigo in cardapio:
        pedidos.append(cardapio[codigo])
        print(f"Você pediu {cardapio[codigo]['item']}")
    else:
        print("Código inválido. Tente novamente.")
    
    return realizar_pedido(cardapio, pedidos)  # Chamada recursiva para continuar os pedidos

# Função para fechar a conta
def fechar_conta(pedidos):
    if not pedidos:
        print("\nVocê não fez nenhum pedido.")
        return
    
    total = sum(item['preco'] for item in pedidos)
    print("\nSeus pedidos:")
    for item in pedidos:
        print(f"- {item['item']}: R${item['preco']:.2f}")
    
    print(f"\nTotal a pagar: R${total:.2f}")

# Função principal para rodar o sistema
def restaurante():
    cardapio = exibir_cardapio()
    pedidos = realizar_pedido(cardapio)
    fechar_conta(pedidos)

# Executar o sistema
restaurante()


