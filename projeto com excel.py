
import pandas as pd
import keyboard
import time

tabela = pd.read_excel("carros.xlsx")
tabela2 = pd.read_excel("motos.xlsx")

print("---------------| LP CONCESSIONÁRIA |---------------")
print("tabela carros: aperte Espaço")
print("tabela Motos: aperte Tab")


def mostralinha():
    print("="*50)
    
    
while True:
    while True:
        if keyboard.is_pressed("space"):    
            print("===================| CARROS |======================")
            display(tabela)
            break

    while True:     
        if keyboard.is_pressed("tab"):
            print("====================| MOTOS |======================")
            display(tabela2)
            mostralinha()
            break

    break


time.sleep(5)
gostaria = str(input("qual categoria o senhor gostou mais ?  motos ou carros")).upper
time.sleep(2)
gostaria1 = int(input("digite o numero do veiculo que vc gostou mais: "))
# condiçoes se for carros
if gostaria == "carros":
    print("muito bem, carros sao o maximooo!!!")
    if gostaria1 == 0:
        # bmw 328i
        print("bmw 328i: 205 cv, ano 2013, sem duvidas é um carro muito bom e veloz ")
    if gostaria1 == 1:
        # ford mustang
        print("ford mustang 460cv, ano 2016, otimo carro para quem quer uma tocada mais agressiva ")
    if gostaria1 == 2:
        # porsche
        print( "porsche gt3 rs: 510cv, ano 2020, um dos carros mais luxuosos e fortes do mundo")
    if gostaria1 == 3:
        # bmw 118i
        print("bmw 118i: 170cv, ano 2011, esse carro é muito bom forte e ecomico")
    if gostaria1 == 4:
        # vw golf
        print(
            "vw golf gti: 230vc, ano 2014, muito parecido em questao de comforto com a bmw")
    if gostaria1 == 5:
        # vw fusca
        print("vw fusca: 46cv, ano 1972, esse aqui é pra quem ama mesmo, 46vc...")
    if gostaria1 == 6:
        # kia cerato
        print("kia cerato: 130cv, ano 2010, otima opçao como primeiro carro, nem tao forte e nem tao fraco")
    if gostaria1 == 7:
        # kia sorento
        print("kia sorento: 150cv, ano 2011, carro otimo e em bom estado, bom de motor")

# condiçoes se a escolha for motos
if gostaria == "motos":
    print("muito bem, motos sao o maximooo!!!")
    if gostaria1 ==  0:
        # bmw s1000rr   
        print("bmw s1000rr: 205cv, 1000cc, ano 2013, otima escolha esta s1000rr é muito forte")
    if gostaria1 == 1:
        # kw z900
        print("kw z900: 157cv, 950cc, ano 2019, que boa escolha esta z900 está novinha!!")
    if gostaria1 == 2:
        # bmw f800
        print("bmw f800r: 75cv. 800cc, ano 2014, sem duvidas a melhor moto 800cc do mundo")
    if gostaria1 == 3:
        # kw zx6
        print("kw zx6: 125cv, 600cc, ano 2015, otima escolha a zx6 é uma moto muito boa")
    if gostaria1 == 4:
        # gsx 1000
        print("suzuki gsxr 1000: 195cv, 1000cc, ano 2012, boaaa a famosa srad 1000")
    if gostaria1 == 5:
        # yamaha r1
        print("yamaha r1: 201cv, 1000cc, ano 2008, otima escolha amigo, r1 nao te deixa na mao")
    if gostaria1 == 6:
        # yamaha r6
        print( "yamaha r6: 130cv, 600cc, ano 2011, essa com certeza nao te deixa na mao...r6 ")
    if gostaria1 == 7:
        # honda cb500f
        print("honda cb500f: 48cv, 500cc, ano 2021, motaoooo cb500taoo")
    if gostaria1 == 8:
        # ducati v4s
        print("ducati v4s: 210cv, 1001cc, ano 2018, essa tem que saber tocar, ducati v4s n tem pra ninguem...")

        
        

time.sleep(2)
pagamento = str(input("gostaria de seguir para o pagamento ? sim/nao:  "))
# se gostaria de pagar for nao
if pagamento == "nao":
    time.sleep(1)
    print("---------------------| consideraçoes | -------------------------")
    time.sleep(3)
    print("se o senhor mudar de ideia venha falar conosco, obrigado!")
    print("----------------------------------------------------------------")


# se gostaria de pagar for sim
if pagamento == "sim":
    pagar = str(
        input(f"como o senhor deseja pagar o veiculo: pix, cartao ou transferencia ?"))
    if pagar == "pix":
        # if pagar == op_pagamentos[0]:
        print("-----------------------| total |----------------------------")
        print("valor total: ")
        meiop = str(
            input("prefere efetuar o pagamento com o qr code ou cnpj ? "))
        if meiop == ("qr code"):
            print("aproxime o celular: aperte A")
            while True:
                if keyboard.is_pressed("a"):
                    time.sleep(2)
                    print("escaneando codigo...")
                    time.sleep(2)
                    print("pagamento efetuado!")
                    break
        if meiop == "cnpj":
            print("cnpj=141415516-09")
            print("cole o cnpj: aperte V")
            while True:
                if keyboard.is_pressed("v"):
                    time.sleep(1)
                    print("cnpj colado")
                    break
            print("conclua o pagamento: aperte S")
            while True:     

                if keyboard.is_pressed("s"):
                    time.sleep(2)
                    print("efetuando pagamento...")
                    time.sleep(2)
                    print("pagamento aprovado...")

                    print(
                        "---------------------| consideraçoes | -------------------------")
                    time.sleep(2)
                    print(
                        "muito obrigado pela compra, espero que aproveite bem o seu veiculo!!!")
                    time.sleep(2)
                    print("siga-nos nas redes socias @lp-concessionaria")
                    time.sleep(2)
                    print("a equipe  lp concessionaria deseja a ti uma ótima semana...")
                    print(
                        "----------------------------------------------------------------")

    if pagar == "cartao":
        # if pagar == op_pagamentos[1]:
        print("-----------------------| total |----------------------------")
        print("valor total: ")
        # if gostaria == "carros":
        print("insira o cartao: aperte SHIFT")
        while True:
            if keyboard.is_pressed("shift"):
                time.sleep(2)
                print("cartao inserido...")
                break
        time.sleep(2)
        print("aprovando pagamento...")
        time.sleep(3)
        print("pagamento aprovado!")
        time.sleep(1)
        print("retire seu cartao: aperte R ")
        while True:
            if keyboard.is_pressed("r"):
                time.sleep(1)
                print("cartao retirado...")
                break


    if pagar == "transferencia":
        # if pagar == op_pagamentos[2]:
        print("-----------------------| total |----------------------------")
        print("total compra: ")
        time.sleep(2)
        print("-----------------------| conta |----------------------------")
        time.sleep(2)
        print("agencia: 0019-1")
        time.sleep(2)
        print("banco: 1")
        time.sleep(2)
        print("num conta corrente: 77912-4")
        time.sleep(2)
        print("obs: pagamento deve ser realizado em no maximo 3 dias uteis!")

       


print("---------------------| consideraçoes | -------------------------")
time.sleep(2)
print("muito obrigado pela compra, espero que aproveite bem o seu veiculo!!!")
time.sleep(2)
print("siga-nos nas redes socias @lp-concessionaria")
time.sleep(2)
print("a equipe  lp concessionaria deseja a ti uma ótima semana...")
print("----------------------------------------------------------------")


op_pagamentos1 = ("pix, cartao, transferencia")
    