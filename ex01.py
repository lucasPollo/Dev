










#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps)
#calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).



print('----------TEMPO DE DOWLOAD---------')

tamArquivo = float(input('Tamanho do arquivo[mb/s]: '))
velocInternet = float(input('Velocidade internet[mb]: '))

velocDowload = tamArquivo * velocInternet
velocDowload = velocDowload / 3600
print(f'velocidade de dowload {velocDowload} minutos')

print('------------------------------------')