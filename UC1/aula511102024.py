# #RESOLUÇÃO EXERCÍCIO 5

# # Definindo o número de alunos
# num_alunos = 20

# # Estrutura de repetição para processar as notas de cada aluno
# for i in range(1, num_alunos + 1):
#     print(f"\nAluno {i}:")
    
#     # Entrada de dados
#     nota1 = float(input("Digite a nota da primeira avaliação: "))
#     nota2 = float(input("Digite a nota da segunda avaliação: "))
#     nota_optativa = float(input("Digite a nota da avaliação optativa (ou -1 se não fez): "))

#     # Substituir a menor nota pela optativa, se ela for maior
#     if nota_optativa != -1:
#         menor_nota = min(nota1, nota2)
#         if nota_optativa > menor_nota:
#             if nota1 == menor_nota:
#                 nota1 = nota_optativa
#             else:
#                 nota2 = nota_optativa

#     # Cálculo da média
#     media = (nota1 + nota2) / 2

#     # Exibindo resultado e status
#     print(f"Média do semestre: {media:.2f}")
    
#     if media >= 6.0:
#         print("Aprovado")
#     elif media < 3.0:
#         print("Reprovado")
#     else:
#         print("Exame")




#ATIVIDADE DE FIXAÇÃO:

#>>>Desenvolva um programa que guarde os dados de 10 pessoas que estão se candidatando a uma vaga de emprego, sabendo que candidatos 
#menores de 18 anos não podem participar. Os dados coletados são: nome, data de nascimento, telefone, e-mail, formação acadêmica e a 
#experiência profissional.


# #variável para armazenar os candidatos válidos
# from datetime import datetime

# # Função para calcular a idade a partir da data de nascimento
# def calcular_idade(data_nascimento):
#     hoje = datetime.now()
#     nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
#     idade = hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))
#     return idade

# # Lista para armazenar os candidatos
# candidatos = []
# contador = 0 #contador para garantir que 10 candidatos sejam processados

# # Coletar dados dos candidatos
# while contador < 10:
#     nome = input("Digite o nome do candidato: ")
#     data_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ")
#     idade = int(input("Digiti a idade do candidato: "))

#     # Verificar se o candidato tem 18 anos ou mais
#     if idade < 18:
#         print("Candidatos devem ter 18 anos ou mais. Tente novamente.")
       
#     else:
#         telefone = input("Digite o telefone do candidato: ")
#         email = input("Digite o e-mail do candidato: ")
#         formacao = input("Digite a formação acadêmica do candidato: ")
#         experiencia = input("Digite a experiência profissional do candidato: ")

#     candidato. append({
#         "nome": nome,
#         "data_nascimento": data_nascimento,
#         "telefone": telefone,
#         "email": email,
#         "formacao": formacao,
#         "experiencia": experiencia
#     })

#     contador += 1  #incremente o contato para processar o proximo  candidato
#     print("Candidato adicionado com sucesso!")

# # Exibir os dados dos candidatos
# print("\nCandidatos cadastrados:")
# for i, candidato in enumerate(candidatos, 1):
#     print(f"\nCandidato {i}:")
#     for chave, valor in candidato.items():
#         print(f"{chave.capitalize()}: {valor}")


#Estruturas de armazenamento

#LISTA 'conversão: list()'
candidato=[]#lista vazia
lista1=[2,4,6,8,10]
print(lista1)
print(lista1[0])
print(lista1[1])
print(lista1[2])
print(lista1[3])
print(lista1[4])
print(lista1[-1])
print(lista1[-2])
lista1.append(20)
lista1.insert(26,3)
lista1.insert(2,33)
print(lista1)
print(len(lista1))





#TUPLAS 'conversão: tuple()'
senhas=() #tuplas vazia

#DICIONARIOS 'conversão:dict()
estados_uf={} #dicionario vazio