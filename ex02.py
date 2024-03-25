#Faça um Programa que pergunta quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no mês específico, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, 
# faça um programa que nos dê: salário bruto. quanto pagou ao INSS. quanto pagou ao sindicato. o salário líquido. calcule os descontos e o salário líquido, conforme tabela abaixo:

#+ Salário Bruto : R$
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
#= Salário Liquido : R$





print('-----------DESCONTOS TRIBUTÁRIOS--------------')

reaisHora = float(input('Valor $ por hora trabalhada: '))
numHorasTrabalhadasMes = float(input('Horas trabalhadas por mês: '))
salarioBruto = reaisHora * numHorasTrabalhadasMes
impostoRenda = (salarioBruto / 10)
inss = (salarioBruto / 8)
sindicato = (salarioBruto / 5)
salarioFinal = salarioBruto - (impostoRenda + inss + sindicato)



print('-------------TABELA MENSAL: -------------------')
print(f'Salário Bruto: R${salarioBruto}')
print(f'Ir(10%): -R${impostoRenda}')
print(f'Inss(8%): -R${inss}')
print(f'Sindicato(5%): -R${sindicato}')
print(f'Salário final: R${salarioFinal}')




















print('-----------------------------------------------')

