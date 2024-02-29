import customtkinter
import sqlite3
import pandas as pd




def CadastrarClientes():
    
  conexao = sqlite3.connect('Clientes_LavaJato2.db')

  c = conexao.cursor()

    
  c.execute('INSERT INTO infoClientes Values (:nome, :veiculo, :placa, :entrada)',
           
           {
               'nome':EntNome.get(),
               'veiculo':EscolhaVeiculo.get(),
                'placa':PlacaVeiculo.get(),
                'entrada':DiaEntrada.get()
               
               
           }
           
           
           
           )
 
    
  conexao.commit()
  conexao.close()
           

def EnviaPlanilha():
    conexao = sqlite3.connect('Clientes_LavaJato2.db')

    c = conexao.cursor()
    
    global clientes
    
    c.execute('SELECT *,  oid FROM infoClientes')
    clientes = c.fetchall()
    clientes = pd.DataFrame(clientes, columns=['nome','veiculo','placa', 'entrada', 'Id_Cliente'])
    clientes.to_excel('Planilha_ClientesJato2.xlsx')
    print(clientes)
    
    conexao.commit()
    conexao.close()
     
     

def PegarDados():
    conexao = sqlite3.connect('Clientes_LavaJato2.db')

    c = conexao.cursor()
    
   
    
    c.execute('SELECT *,  oid FROM infoClientes')
    dados = c.fetchall()
    dados = pd.DataFrame(dados, columns=['nome','veiculo','placa', 'entrada', 'Id_Cliente'])
    print(clientes)
    
    conexao.commit()
    conexao.close()
   

 
janela = customtkinter.CTk()
janela.geometry(('300x600'))
janela.title('teste Lava-Jato')

TxtCadastro = customtkinter.CTkLabel(janela, anchor='center', text='Cadastre-se', height=50, width=300,  font=('Arial', 25), fg_color='#4559F5')
TxtCadastro.pack()


EntNome = customtkinter.CTkEntry(janela, corner_radius=15, placeholder_text='Nome Completo: ')
EntNome.place(x=80, y=160)


EscolhaVeiculo = customtkinter.CTkOptionMenu(janela , fg_color='#4559F5', values=['Carro' , 'Motocicleta', 'Caminhão'])
EscolhaVeiculo.place(x=80, y=210)


PlacaVeiculo = customtkinter.CTkEntry(janela, placeholder_text='Placa do veiculo: ', corner_radius=15)
PlacaVeiculo.place(x=80, y=260 )

DiaEntrada = customtkinter.CTkEntry(janela, placeholder_text='Data de hoje:', corner_radius=15)
DiaEntrada.place(x=80, y=310)


def mostrarMsg():
    txtCadastroConcluido = customtkinter.CTkLabel(janela, text='Cadastro concluído!')
    txtCadastroConcluido.place(x=90, y=410)
    
    if EscolhaVeiculo.get() == 'Carro':
        LbC = customtkinter.CTkLabel(janela, text=f'Seu veiculo estará pronto em 6 dias {EntNome.get()}', anchor='center', height=50, width=300, fg_color='#4559F5',  font=('Arial', 12))
        LbC.place(x=0, y=460)
        
        
    elif EscolhaVeiculo.get() == 'Motocicleta':
        LbM = customtkinter.CTkLabel(janela, text=f'Seu veiculo estará pronto em 3 dias {EntNome.get()}', anchor='center', height=50, width=300, fg_color='#4559F5',  font=('Arial', 12))
        LbM.place(x=0, y=460)
        
        
    elif EscolhaVeiculo.get() == 'Caminhão':
        LbCa = customtkinter.CTkLabel(janela, text=f'Seu veiculo estará pronto em 11 dias {EntNome.get()}', anchor='center', height=50, width=300, fg_color='#4559F5',  font=('Arial', 12))
        LbCa.place(x=0, y=460)

BotaoSalvar = customtkinter.CTkButton(janela, text='Salvar', command=lambda:[mostrarMsg(), CadastrarClientes(), EnviaPlanilha(), PegarDados()], corner_radius=15, fg_color='#4559F5')
BotaoSalvar.place(x=80, y=360)


BottomDiv = customtkinter.CTkLabel(janela, text='© 2023 Teste - Todos os direitos reservados.', anchor='center', height=50, width=300, fg_color='#4559F5',  font=('Arial', 15))
BottomDiv.pack(side='bottom')


def NovaJanela():
    janelaAdmin = customtkinter.CTk()
    janelaAdmin.geometry(('400x600'))
    janelaAdmin.title('Teste | Admin')
    
    
    Txt = customtkinter.CTkLabel(janelaAdmin, anchor='center', text='Admin | Dados', height=50, width=300,  font=('Arial', 25), fg_color='#4559F5')
    Txt.pack()
    
    
    
    dados = customtkinter.CTkLabel(janelaAdmin, text=clientes['nome', 'veiculo'], font=('Arial', 15))
    dados.pack(side='top')
    
    janelaAdmin.mainloop()


BotaoS = customtkinter.CTkButton(janela, text='Admin', command=lambda: [NovaJanela(), PegarDados()], corner_radius=15, fg_color='#4559F5', height=30, width=30)
BotaoS.place(x=10, y=160)



janela.mainloop()

