AULA10 - 18/10/2024###
#
# Pandas (pandas.pydata.orgphyto)
#
import pandas as pd #(pd=alias)
print(pd.__version__)

#CRIAÇÃO DE UM DATASET:

data = {'Cargo': ['Analista', 'Gerente', 'Estagiário'],
        'Salário': [4500, 9000, 2000]}
cargos_salarios = pd.DataFrame(data)
print(cargos_salarios)

#CRIAÇÃO DE UMA SÉRIE:

cargos = pd.Series(['Analista', 'Gerente', 'Estagiário'], index=[1, 2, 3])
print(cargos)

#ATIVIDADE ASSISTIDA:

#Crie um dataset de 3 colunas com as seguintes informações: 'nome de um filme', 'ano de lançamento' e 'gênero'.

#Resolução:
import pandas as pd

data_cinema={'Título':['Cidade de Deus','Divertidamente 2','Uma Linda Mulher'],
        'Ano de Lançamento':[2002, 2024, 1990],
        'Gênero':['Drama', 'Animação','Romance']
}
cinema=pd.DataFrame(data_cinema)
print(cinema)

#ACESSO À DATASETS EXTERNOS:

https://www.kaggle.com/datasets/thebumpkin/700-classic-disco-tracks-with-spotify-data

df_disco = pd.read_csv('path_to_dataset.csv')
print(df_disco.head())  # Exibe as primeiras linhas
print(df_disco.tail())  # Exibe as cinco últimas linhas

#Leitura de Arquivos e Filtragem:

print(df_disco.to_string()) #Exibe o DataFrame completo como uma string, útil para visualização.

pd.set_option('display.max_rows',3) #Define o número máximo de linhas a ser exibido.

#Filtragem de Dados: Exemplo de filtragem por colunas e linhas específicas:

df_filtrado = df_disco[df_disco['Year'] == 1979]
print(df_filtrado)