'''#variáveis simplles são as que calculam a entrada de dados
lampada_potencia=float(input('Digite a potencia da lampada (watts):'))  
largura_comodo=float(input('Digite a largura do cômdo:') )
comprimento_comodo=float(input('Digite a potencia da lampada (watts):'))

#variáveis para o cálculo de area e de potencia
area_comodo=largura_comodo*comprimento_comodo
potencia_real=3*lampada_potencia

#variáveis para o calculo do número de lâmpadas e bocais
numero_lampadas=potencia_real/lampada_potencia
bocais=area_comodo/3

#exibição do resultados (quaisquer das formataçoes são validas)
print('lâmpada:',numero_lampadas) #para ser mais simples para o usuario
print(f"número de lâmpadas necessárias:{numero_lampadas: .2f}")
print(F"número de bocais necessários:{bocais}")'''



