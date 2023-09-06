import keyboard
import time

carros = ['bmw', 'fusca', 'corvete', 'dodge ram', 'f250']
motos = ['r1', 's1000rr', 'cbr600', 'zx10r', 'r3']
precos_carros = [56.700, 56.766, 23.500, 157.300, 99.459]
precos_motos = [32.899, 74.802, 41.456, 29.700, 21.670]



print('loja de carros')


nome = str(input('Insira seu nome: '))
idade = str(input('Insira sua data nascimento: '))
user = ...
senha = ...

gostaria = str(input('gostaria de ver os carros ou motos? ')).lower()
if 'carros' in gostaria:
    print(carros)
    interessado_carros = str(input('gostaria de comprar algum ?'))
    if 'sim' or 'gostaria' in interessado_carros:
     modelo = str(input('qual vc gostaria: '))
    if 'bmw' in modelo:
        print('otimo carro apenas R$%f'%precos_carros[0])
        if 'fusca' in modelo:
         print('apenas R$%f'% precos_carros[1])
        if 'corvete' in modelo:
         print('muito bom R$%f'% precos_carros[2])
        if 'dodge ram' in modelo:
         print('este carro custa R$%f '%precos_carros[3])
        if "f250" in modelo:
            print('otimo carro, bom custo beneficio apenas R$%f '%precos_carros[4])
          
        
    
elif 'motos' in gostaria:
    print(motos)
    interessados_motos = str(input('gostaria de comprar algum: '))
    if 'sim' or 'gostaria' in interessados_motos:
        modelo = str(input('qual vc gostaria: '))
        if 'r1' in modelo:
            print('otima moto apenas R$%f'%precos_motos[0])
        if 's1000r' in modelo:
            print('apenas R$%f'% precos_motos[1])
        if 'cbr600' in modelo:
            print('muito bom esta moto R$%f'% precos_motos[2])
        if 'zx10r' in modelo:
            print(f'Esta moto é incrivel apenas R${precos_motos[3]}')
        if 'r3' in modelo:
            print(f'ótima moto para iniciantes, por R${precos_motos[4]}')
         
         
         
pagar_gostaria = str(input('gostaria de seguir para o pagamento:    S/N')).upper()
if 'S' or "sim" in pagar_gostaria:
    print('Insira o Usuario e Senha') 
    user = str(input('Insira seu nome; Usuario: '))
    senha = str(input('Insira sua senha; Data de nascimento: '))
    if user and senha == nome and idade:
        print('Aperte "p" para pagar: ')
        while True:
         if keyboard.is_pressed("p"):
            time.sleep(1)
            print('processando')
            time.sleep(1)
            print('pagamento concluido')
            break
    elif user and senha != nome and idade:
        print(f'User e senha incorretos ')
        while user and senha  != nome and idade:
            user = str(input('Insira seu nome; Usuario: '))
            senha = str(input('Insira sua senha; Data de nascimento: '))
              
else:
    print('obrigado por comparecer a nossa loja')
    
    
print('obrigado!')
    



    
