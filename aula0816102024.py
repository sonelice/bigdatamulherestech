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





    

# import random # trabalhar com dados gerados aleatoriamente

# # crie uma funçao que gere dois números aleatorios dentro do intervalo

# def doisnum_aleatorios(quantidade=2,numero_minimo=0,numero_maximo=1):
#         for i in range(2):
#             return random.randint(numero_minimo,numero_maximo)
        
# numeros=doisnum_aleatorios(20,1,100)
# print(numeros)
