print ('Bem Vindo a calculadora custo-benefício')
print('O custo benefício será dado por: Proteína total/Preço')
print('Por favor, insira os dados')
print('Lembre-se de colocar todas as unidades de peso em gramas')
WN = input('Nome do Whey: ' )
BN = input('Marca do Whey: ')
WP_input = input('Preço do Whey: ')
WT_input = input('Peso total: ')
WPS_input = input('Peso por porção: ')
PPS_input= input('Proteína por porção: ')
WT = float(WT_input)
WP = float(WP_input)
WPS = float(WPS_input)
PPS = float(PPS_input)
NP =  WT/WPS
TP = PPS*NP
CB = TP/WP
print((WN) + ' da marca ' + (BN) + ' tem razão de ' + str(CB))
