import customtkinter

janela = customtkinter.CTk()
janela.geometry(('340x540'))
janela.title('Calculo de Impostos')
janela.resizable(width=False, height=False)

LbNavBar = customtkinter.CTkLabel(janela, bg_color='#6E84E6', text='Impostos Veiculares', width=340, font=('Arial', 22), text_color='white')
LbNavBar.pack()

EntValor = customtkinter.CTkEntry(janela, placeholder_text='Valor...', width=180, font=('Kufam', 18))
EntValor.place(x=80, y=80)

CbTipoVeiculo = customtkinter.CTkComboBox(janela, values=['Motocicleta','Carro'], width=180, font=('Kufam', 18))
CbTipoVeiculo.place(x=80, y=120)


def ColetaValorVeiculo():
    global ValorVeiculo
    ValorVeiculo = EntValor.get()
    print(ValorVeiculo)
    return ValorVeiculo


def ColetaModeloVeiculo():
    global ModeloVeiculo
    ModeloVeiculo = CbTipoVeiculo.get()
    print(ModeloVeiculo)
    return ModeloVeiculo
    
    
def CalculaImpostos():
    global ValorVeiculo
    global ModeloVeiculo
    
    if ModeloVeiculo== 'Motocicleta':
        ValorVeiculo = float(ValorVeiculo)
        Ipva = ValorVeiculo-(ValorVeiculo-(ValorVeiculo*5/100))
        LbResultadoIpva = customtkinter.CTkLabel(janela, text=f'{Ipva:.2f}', font=('Arial', 18))
        LbResultadoIpva.place(x=130, y=240)
        print(Ipva)
        Seguro = ValorVeiculo-(ValorVeiculo-(ValorVeiculo*11/100))
        LbResultadoSeguro = customtkinter.CTkLabel(janela, text=f'{Seguro:.2f}', font=('Arial', 18))
        LbResultadoSeguro.place(x=130, y=320)
        print(Seguro)
        return Ipva, Seguro
    
        
    elif ModeloVeiculo == 'Carro':
        ValorVeiculo = float(ValorVeiculo)
        Ipva = float(ValorVeiculo)-(ValorVeiculo-(ValorVeiculo*8/100))
        LbResultadoIpva = customtkinter.CTkLabel(janela, text=f'{Ipva:.2f}', font=('Arial', 18))
        LbResultadoIpva.place(x=130, y=240)
        print(Ipva)
        Seguro = float(ValorVeiculo)-(ValorVeiculo-(ValorVeiculo*11/100))
        LbResultadoSeguro = customtkinter.CTkLabel(janela, text=f'{Seguro:.2f}', font=('Arial', 18))
        LbResultadoSeguro.place(x=130, y=320)
        print(Seguro)
        return Ipva, Seguro
        
        
BtnSalvar = customtkinter.CTkButton(janela, text='Calcular', command=lambda:[ColetaModeloVeiculo(), ColetaValorVeiculo(), CalculaImpostos()], font=('Arial', 18), bg_color='#717FBD', width=180, hover_color='#3BBD5F')
BtnSalvar.place(x=80, y=160)

LbIpva = customtkinter.CTkLabel(janela, text='Ipva:', width=180, font=('Arial', 18), bg_color='#6E84E6')
LbIpva.place(x=80, y=200)

LbSeguro = customtkinter.CTkLabel(janela, text=f'Seguro:', width=180, font=('Arial', 18), bg_color='#6E84E6')
LbSeguro.place(x=80, y=280)
janela.mainloop()
