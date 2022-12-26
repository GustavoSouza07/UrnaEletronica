from tkinter import *
from tkinter import ttk
import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt

# import pygame

df_gov = pd.read_csv('dados_gov.csv')
df_pres = pd.read_csv('dados_pres.csv')

arq = open('titulos_cadastrados.txt')
titulos_cadastrados = arq.readlines()
titulos_usados = [titulo.replace('\n', '') for titulo in titulos_cadastrados]

menu_inicial = Tk()
menu_inicial.title("URNA")
menu_inicial.configure(background="#808080")
menu_inicial.geometry("600x600+420+50")
menu_inicial.resizable(False, False)

def resultado_gov():

    plt.style.use('bmh')
    df = pd.read_csv('dados_gov.csv')

    x = df['Nome']
    y = df['Votos']

    plt.title("Eleições 2022")
    plt.xlabel('votos', fontsize=14, color='blue')
    plt.ylabel('candidatos', fontsize=14, color='blue')
    plt.barh(x, y)

    plt.show()
def resultado_pres():
    plt.style.use('bmh')
    df = pd.read_csv('dados_pres.csv')

    x = df['Nome']
    y = df['Votos']

    plt.title("Eleições 2022")
    plt.xlabel('votos', fontsize=14, color='blue')
    plt.ylabel('candidatos', fontsize=14, color='blue')
    plt.barh(x, y)

    plt.show()

def encerrar():
    resultados = Tk()
    resultados.title("URNA")
    resultados.configure(background="white")
    resultados.geometry("600x600+420+50")
    resultados.resizable(False, False)

    bt_pres = Button(resultados, text="PRESIDENTE", font="Arial 18 bold", bg="#44CE50",
                       command= resultado_pres)
    bt_pres.place(relx=0.1, rely=0.1, relwidth=0.3, relheight=0.2)

    bt_gov = Button(resultados, text="GOVERNADOR", font="Arial 18 bold", bg="#44CE50",
                         command= resultado_gov)
    bt_gov.place(relx=0.6, rely=0.1, relwidth=0.3, relheight=0.2)
def fim():
    fim = Tk()
    fim.title("Urna eletronica 2022")
    fim.configure(background="white")
    fim.geometry("600x600+420+50")
    fim.resizable(False, False)

    label_fim = Label(fim, text="FIM", font="Arial 90 bold", bg="white")
    label_fim.place(relx=0.25, rely=0.3, relwidth=0.5, relheight=0.2)
    label_voltar = Label(bg="white")
    label_voltar.place(relx=0.22, rely=0.7, relwidth=0.6, relheight=0.2)

    bt_voltar = Button(label_voltar, text="NOVA SEÇÃO", font="Arial 15 bold", bg="#32CD32",
                       command=lambda: [fim.destroy(), titulo()])
    bt_voltar.place(relx=0.0, rely=0.0, relwidth=0.5, relheight=0.6)

    bt_encerrar = Button(label_voltar, text="ENCERRAR", font="Arial 15 bold", bg="#ff0000",
                         command=lambda: [fim.destroy(), encerrar()])
    bt_encerrar.place(relx=0.5, rely=0, relwidth=0.5, relheight=0.6)


def votacao_pres():
    vot_pres = Tk()
    vot_pres.title("Urna eletronica 2022")
    vot_pres.configure(background="#808080")
    vot_pres.geometry("600x600+420+50")
    vot_pres.resizable(False, False)

    def deletar():
        visor.delete(0, END)

    def clicar(numero):
        '''função clicar'''
        atual = visor.get()
        visor.delete(0, END)
        visor.insert(END, str(atual) + str(numero))
    frame_1 = Frame(vot_pres, bd=4, bg="#F5F5F5",
                    highlightbackground="#000000", highlightthickness=3)
    frame_1.place(relx=0.002, rely=0.002, relwidth=0.70, relheight=0.2)

    frame_3 = Frame(vot_pres, bd=4, bg="#2b2a2a",
                    highlightbackground="#000000", highlightthickness=3)
    frame_3.place(relx=0.001, rely=0.205, relwidth=0.7, relheight=0.79)

    frame_4 = Frame(vot_pres, bd=4, bg="#F5F5F5",
                    highlightbackground="#000000", highlightthickness=3)
    frame_4.place(relx=0.71, rely=0.6, relwidth=0.287, relheight=0.395)

    frame_5 = Frame(vot_pres, bd=4, bg="#F5F5F5",
                    highlightbackground="#000000", highlightthickness=3)
    frame_5.place(relx=0.71, rely=0.0001, relwidth=0.287, relheight=0.595)

    bt_one = Button(frame_3, text="1", bd=4, bg="black", fg="white", font=("arial", 40, "bold"),
                    command=lambda: clicar(1),
                    highlightbackground="#000000", highlightthickness=3)

    bt_one.place(relx=0.00999, rely=0.0, relwidth=0.3, relheight=0.2)

    bt_two = Button(frame_3, text="2", bd=4, bg="black", fg="white", font=("arial", 40, "bold"),
                    command=lambda: clicar(2),
                    highlightbackground="#000000", highlightthickness=3)

    bt_two.place(relx=0.36, rely=0.0, relwidth=0.3, relheight=0.2)

    bt_three = Button(frame_3, text="3", bd=4, bg="black", fg="white", font=("arial", 40, "bold"),
                      command=lambda: clicar(3),
                      highlightbackground="#000000", highlightthickness=3)
    bt_three.place(relx=0.7, rely=0.0, relwidth=0.3, relheight=0.2)

    bt_four = Button(frame_3, text="4", bd=4, bg="black", fg="white", font=("arial", 40, "bold"),
                     command=lambda: clicar(4),
                     highlightbackground="#000000", highlightthickness=3)
    bt_four.place(relx=0.00999, rely=0.25, relwidth=0.3, relheight=0.2)

    bt_five = Button(frame_3, text="5", bd=4, bg="black", fg="white", font=("arial", 40, "bold"),
                     command=lambda: clicar(5),
                     highlightbackground="#000000", highlightthickness=3)
    bt_five.place(relx=0.36, rely=0.25, relwidth=0.3, relheight=0.2)

    bt_six = Button(frame_3, text="6", bd=4, bg="black", fg="white", font=("arial", 40, "bold"),
                    command=lambda: clicar(6),
                    highlightbackground="#000000", highlightthickness=3)
    bt_six.place(relx=0.7, rely=0.25, relwidth=0.3, relheight=0.2)

    bt_seven = Button(frame_3, text="7", bd=4, bg="black", fg="white", font=("arial", 40, "bold"),
                      command=lambda: clicar(7),
                      highlightbackground="#000000", highlightthickness=3)
    bt_seven.place(relx=0.00999, rely=0.5, relwidth=0.3, relheight=0.2)

    bt_eight = Button(frame_3, text="8", bd=4, bg="black", fg="white", font=("arial", 40, "bold"),
                      command=lambda: clicar(8),
                      highlightbackground="#000000", highlightthickness=3)
    bt_eight.place(relx=0.36, rely=0.5, relwidth=0.3, relheight=0.2)

    bt_nine = Button(frame_3, text="9", bd=4, bg="black", fg="white", font=("arial", 40, "bold"),
                     command=lambda: clicar(9),
                     highlightbackground="#000000", highlightthickness=3)
    bt_nine.place(relx=0.7, rely=0.5, relwidth=0.3, relheight=0.2)

    bt_zero = Button(frame_3, text="0", bd=4, bg="black", fg="white", font=("arial", 40, "bold"),
                     command=lambda: clicar(0),
                     highlightbackground="#000000", highlightthickness=3)
    bt_zero.place(relx=0.36, rely=0.75, relwidth=0.3, relheight=0.2)

    def comp_voto_pres_branc():
        if visor.get() != "":
            voto_presidente = int(visor.get())
        else:
            voto_presidente = 0
        df_pres.loc[df_pres['Número'] == voto_presidente, 'Votos'] = df_pres['Votos'] + 1
        df_pres.to_csv('dados_pres.csv', index=False)

    def comp_voto_nulo_pres():
        #adicionar 1 somente
        df_pres.loc[df_pres['Número'] == "nulo", 'Votos'] = df_pres['Votos'] + 1
        df_pres.to_csv('dados_pres.csv', index=False)

    def confirma_pres():
        bt_confirm = Button(frame_4, text="CONFIRMA", bd=4, bg="#32CD32", font=("arial", 20, "bold"),
                            command=lambda: [comp_voto_pres_branc(), vot_pres.destroy(), fim()],
                            # armazenar os dados apartir daqui
                            highlightbackground="#000000", highlightthickness=3)

        bt_confirm.place(relx=0.001, rely=0.7, relwidth=1.0, relheight=0.3)

        bt_corre = Button(frame_4, text="CORRIGE", bd=4, bg="#FF4500", font=("arial", 20, "bold"),
                          command=lambda: [comp_voto_pres_branc(), bt_confirm.destroy(), deletar()],
                          highlightbackground="#000000", highlightthickness=3, )
        bt_corre.place(relx=0.001, rely=0.35, relwidth=1.0, relheight=0.3)

    def nomes_pres():
        labelteste2 = Label(vot_pres)
        labelteste2["text"] = visor.get()
        if labelteste2["text"] == "33":
            label_partido = Label(frame_5, text="MATHEUS \n RUFINO \n PARTIDO: \n PR \n VICE:\n FLÁVIO \n FREITAS", bd=4,
                                  bg="#F5F5F5", font=("arial", 20, "bold"),
                                  highlightbackground="#000000", highlightthickness=3)
            label_partido.pack()
            comp_voto_pres_branc()
        elif labelteste2["text"] == "5":
            label_partido = Label(frame_5, text="JOÃO \n PEDRO \n  PARTIDO: \n PG \n VICE:\n JORGE \n RAMOS",
                                  bd=4, bg="#F5F5F5",
                                  font=("arial", 20, "bold"),
                                  highlightbackground="#000000", highlightthickness=3)
            label_partido.pack()
            comp_voto_pres_branc()
        else:
            label_partido = Label(frame_5, text="VOTO \n NULO", bd=4, bg="#F5F5F5",
                                  font=("arial", 20, "bold"),
                                  highlightbackground="#000000", highlightthickness=3)
            label_partido.pack()

        
        bt_confirm = Button(frame_4, text="CONFIRMA", bd=4, bg="#32CD32", font=("arial", 20, "bold"),
        command=lambda: [vot_pres.destroy(), fim(),comp_voto_nulo_pres()],
                            # armazenar os dados apartir daqui
        highlightbackground="#000000", highlightthickness=3)

        bt_confirm.place(relx=0.001, rely=0.7, relwidth=1.0, relheight=0.3)

        bt_corre = Button(frame_4, text="CORRIGE", bd=4, bg="#FF4500", font=("arial", 20, "bold"),
                          command=lambda: [bt_confirm.destroy(), deletar(), label_partido.destroy()],
                          highlightbackground="#000000", highlightthickness=3, )
        bt_corre.place(relx=0.001, rely=0.35, relwidth=1.0, relheight=0.3)

    def TEXT_branco_pres():
        label_vot_branc = Label(frame_5, text="VOTO \n BRANCO", bd=4, bg="#F5F5F5", font=("arial", 20, "bold"),
                                highlightbackground="#000000", highlightthickness=3)
        label_vot_branc.pack()

        bt_confirm = Button(frame_4, text="CONFIRMA", bd=4, bg="#32CD32", font=("arial", 20, "bold"),
                            command=lambda: [comp_voto_pres_branc(), vot_pres.destroy(), fim()],
                            # armazenar os dados apartir daqui
                            highlightbackground="#000000", highlightthickness=3)

        bt_confirm.place(relx=0.001, rely=0.7, relwidth=1.0, relheight=0.3)

        bt_corre = Button(frame_4, text="CORRIGE", bd=4, bg="#FF4500", font=("arial", 20, "bold"),
                          command=lambda: [deletar(), label_vot_branc.destroy(), bt_confirm.destroy()],
                          highlightbackground="#000000", highlightthickness=3, )
        bt_corre.place(relx=0.001, rely=0.35, relwidth=1.0, relheight=0.3)

    bt_verif = Button(frame_3, text="VERIFICAR", bd=4, bg="black", fg="white", font=("arial", 15, "bold"),
                      command=lambda: [confirma_pres(), nomes_pres()],  # mostrar a foto
                      highlightbackground="#000000", highlightthickness=3)
    bt_verif.place(relx=0.7, rely=0.75, relwidth=0.3, relheight=0.2)

    bt_corre = Button(frame_4, text="CORRIGE", bd=4, bg="#FF4500", font=("arial", 20, "bold"), command=deletar,
                      highlightbackground="#000000", highlightthickness=3, )
    bt_corre.place(relx=0.001, rely=0.35, relwidth=1.0, relheight=0.3)

    bt_branco = Button(frame_4, text="BRANCO", bd=4, bg="#FFFFFF", font=("arial", 20, "bold"),
                       command=lambda: [comp_voto_nulo_pres(),TEXT_branco_pres()],
                       highlightbackground="#000000", highlightthickness=3)
    bt_branco.place(relx=0.001, rely=0.0, relwidth=1.0, relheight=0.3)

    lb_codigo = Label(frame_1, text="PRESIDENTE: ", bd=4, bg="#F5F5F5", font=("arial", 20, "bold"),
                      highlightbackground="#000000", highlightthickness=3)
    lb_codigo.place(relx=0.0, rely=0.0, relwidth=1.0, relheight=0.3)

    visor = Entry(frame_1, bd=4, bg="#F5F5F5", font=("Arial", 40, "bold"),
                  highlightbackground="#000000", highlightthickness=3)
    visor.place(relx=0.0, rely=0.32, relwidth=1.0, relheight=0.7)

    vot_pres.mainloop()


def votacao_gov():
    # import pygame

    vot_gov = Tk()
    vot_gov.title("Urna eletronica 2022")
    vot_gov.configure(background="#808080")
    vot_gov.geometry("600x600+420+50")
    vot_gov.resizable(False, False)

    # pygame.mixer.init()
    # def play():
    # pygame.mixer.music.load("")

    def deletar():
        visor.delete(0, END)

    def clicar(numero): #EXPLICAR DE NOVO DEPOIS
        atual = visor.get()
        visor.delete(0, END)
        visor.insert(END, str(atual) + str(numero))

    frame_1 = Frame(vot_gov, bd=4, bg="#F5F5F5",
                    highlightbackground="#000000", highlightthickness=3)
    frame_1.place(relx=0.002, rely=0.002, relwidth=0.70, relheight=0.2)

    frame_3 = Frame(vot_gov, bd=4, bg="#2b2a2a",
                    highlightbackground="#000000", highlightthickness=3)
    frame_3.place(relx=0.001, rely=0.205, relwidth=0.7, relheight=0.79)

    frame_4 = Frame(vot_gov, bd=4, bg="#F5F5F5",
                    highlightbackground="#000000", highlightthickness=3)
    frame_4.place(relx=0.71, rely=0.6, relwidth=0.287, relheight=0.395)

    frame_5 = Frame(vot_gov, bd=4, bg="#F5F5F5",
                    highlightbackground="#000000", highlightthickness=3)
    frame_5.place(relx=0.71, rely=0.0001, relwidth=0.287, relheight=0.595)

    bt_one = Button(frame_3, text="1", bd=4, bg="black", fg="white", font=("arial", 40, "bold"),
                    command=lambda: clicar(1),
                    highlightbackground="#000000", highlightthickness=3)

    bt_one.place(relx=0.00999, rely=0.0, relwidth=0.3, relheight=0.2)

    bt_two = Button(frame_3, text="2", bd=4, bg="black", fg="white", font=("arial", 40, "bold"),
                    command=lambda: clicar(2),
                    highlightbackground="#000000", highlightthickness=3)

    bt_two.place(relx=0.36, rely=0.0, relwidth=0.3, relheight=0.2)

    bt_three = Button(frame_3, text="3", bd=4, bg="black", fg="white", font=("arial", 40, "bold"),
                      command=lambda: clicar(3),
                      highlightbackground="#000000", highlightthickness=3)
    bt_three.place(relx=0.7, rely=0.0, relwidth=0.3, relheight=0.2)

    bt_four = Button(frame_3, text="4", bd=4, bg="black", fg="white", font=("arial", 40, "bold"),
                     command=lambda: clicar(4),
                     highlightbackground="#000000", highlightthickness=3)
    bt_four.place(relx=0.00999, rely=0.25, relwidth=0.3, relheight=0.2)

    bt_five = Button(frame_3, text="5", bd=4, bg="black", fg="white", font=("arial", 40, "bold"),
                     command=lambda: clicar(5),
                     highlightbackground="#000000", highlightthickness=3)
    bt_five.place(relx=0.36, rely=0.25, relwidth=0.3, relheight=0.2)

    bt_six = Button(frame_3, text="6", bd=4, bg="black", fg="white", font=("arial", 40, "bold"),
                    command=lambda: clicar(6),
                    highlightbackground="#000000", highlightthickness=3)
    bt_six.place(relx=0.7, rely=0.25, relwidth=0.3, relheight=0.2)

    bt_seven = Button(frame_3, text="7", bd=4, bg="black", fg="white", font=("arial", 40, "bold"),
                      command=lambda: clicar(7),
                      highlightbackground="#000000", highlightthickness=3)
    bt_seven.place(relx=0.00999, rely=0.5, relwidth=0.3, relheight=0.2)

    bt_eight = Button(frame_3, text="8", bd=4, bg="black", fg="white", font=("arial", 40, "bold"),
                      command=lambda: clicar(8),
                      highlightbackground="#000000", highlightthickness=3)
    bt_eight.place(relx=0.36, rely=0.5, relwidth=0.3, relheight=0.2)

    bt_nine = Button(frame_3, text="9", bd=4, bg="black", fg="white", font=("arial", 40, "bold"),
                     command=lambda: clicar(9),
                     highlightbackground="#000000", highlightthickness=3)
    bt_nine.place(relx=0.7, rely=0.5, relwidth=0.3, relheight=0.2)

    bt_zero = Button(frame_3, text="0", bd=4, bg="black", fg="white", font=("arial", 40, "bold"),
                     command=lambda: clicar(0),
                     highlightbackground="#000000", highlightthickness=3)
    bt_zero.place(relx=0.36, rely=0.75, relwidth=0.3, relheight=0.2)

    def comp_voto_gov():
        if visor.get() != "":
            voto_governador = int(visor.get())
        else:
            voto_governador = 0
        df_gov.loc[df_gov['Número'] == voto_governador, 'Votos'] = df_gov['Votos'] + 1
        df_gov.to_csv('dados_gov.csv', index=False)

    def comp_voto_nulo_gov():
        #adicionar 1 somente
        df_gov.loc[df_gov['Número'] == "nulo", 'Votos'] = df_gov['Votos'] + 1
        df_gov.to_csv('dados_gov.csv', index=False)

    def nomes_gov():
        labelteste2 = Label(vot_gov)
        labelteste2["text"] = visor.get()
        if labelteste2["text"] == "7":
            label_partido = Label(frame_5, text="LUIS \n GUSTAVO \n PARTIDO: \n PVA \n VICE:\n ARTHUR \n MARQUES", bd=4, bg="#F5F5F5", font=("arial", 20, "bold"),
                  highlightbackground="#000000", highlightthickness=3)
            label_partido.pack()
        elif labelteste2["text"] == "80":
            label_partido = Label(frame_5, text="ALISSOM \n GUSTAVO \n  PARTIDO: \n PCV \n VICE:\n NEYMAR \n JÚNIOR", bd=4, bg="#F5F5F5",
                                  font=("arial", 20, "bold"),
                                  highlightbackground="#000000", highlightthickness=3)
            label_partido.pack()
        else:
            label_partido = Label(frame_5, text="VOTO \n NULO", bd=4, bg="#F5F5F5",
                                  font=("arial", 20, "bold"),
                                  highlightbackground="#000000", highlightthickness=3)
            label_partido.pack()

        bt_confirm = Button(frame_4, text="CONFIRMA", bd=4, bg="#32CD32", font=("arial", 20, "bold"),
                            command=lambda: [comp_voto_gov(), vot_gov.destroy(), votacao_pres(),comp_voto_nulo_gov()],
                            # armazenar os dados apartir daqui
                            highlightbackground="#000000", highlightthickness=3)

        bt_confirm.place(relx=0.001, rely=0.7, relwidth=1.0, relheight=0.3)

        bt_corre = Button(frame_4, text="CORRIGE", bd=4, bg="#FF4500", font=("arial", 20, "bold"),
                          command=lambda: [bt_confirm.destroy(), deletar(), label_partido.destroy()],
                          highlightbackground="#000000", highlightthickness=3, )
        bt_corre.place(relx=0.001, rely=0.35, relwidth=1.0, relheight=0.3)

    def TEXT_branco_gov():
        label_vot_branc = Label(frame_5, text= "VOTO \n BRANCO", bd=4, bg="#F5F5F5", font=("arial", 20, "bold"),
                      highlightbackground="#000000", highlightthickness=3)
        label_vot_branc.pack()

        bt_confirm = Button(frame_4, text="CONFIRMA", bd=4, bg="#32CD32", font=("arial", 20, "bold"),
                            command=lambda: [comp_voto_gov(), vot_gov.destroy(), votacao_pres()],
                            # armazenar os dados apartir daqui
                            highlightbackground="#000000", highlightthickness=3)

        bt_confirm.place(relx=0.001, rely=0.7, relwidth=1.0, relheight=0.3)

        bt_corre = Button(frame_4, text="CORRIGE", bd=4, bg="#FF4500", font=("arial", 20, "bold"),
                          command=lambda: [deletar(),label_vot_branc.destroy(),bt_confirm.destroy()],
                          highlightbackground="#000000", highlightthickness=3, )
        bt_corre.place(relx=0.001, rely=0.35, relwidth=1.0, relheight=0.3)

    bt_verif = Button(frame_3, text="VERIFICAR", bd=4, bg="black", fg="white", font=("arial", 15, "bold"),
                      command=lambda: [nomes_gov()],  # mostrar a foto
                      highlightbackground="#000000", highlightthickness=3)
    bt_verif.place(relx=0.7, rely=0.75, relwidth=0.3, relheight=0.2)

    bt_corre = Button(frame_4, text="CORRIGE", bd=4, bg="#FF4500", font=("arial", 20, "bold"),
                      command=deletar,
                      highlightbackground="#000000", highlightthickness=3, )
    bt_corre.place(relx=0.001, rely=0.35, relwidth=1.0, relheight=0.3)

    bt_branco = Button(frame_4, text="BRANCO", bd=4, bg="#FFFFFF", font=("arial", 20, "bold"),
                       command=lambda: [TEXT_branco_gov()],
                       highlightbackground="#000000", highlightthickness=3)
    bt_branco.place(relx=0.001, rely=0.0, relwidth=1.0, relheight=0.3)

    lb_codigo = Label(frame_1, text="GOVERNADOR: ", bd=4, bg="#F5F5F5", font=("arial", 20, "bold"),
                      highlightbackground="#000000", highlightthickness=3)
    lb_codigo.place(relx=0.0, rely=0.0, relwidth=1.0, relheight=0.3)

    visor = Entry(frame_1, bd=4, bg="#F5F5F5", font=("Arial", 40, "bold"),
                  highlightbackground="#000000", highlightthickness=3)
    visor.place(relx=0.0, rely=0.32, relwidth=1.0, relheight=0.7)

    vot_gov.mainloop()


def titulo():
    titulo_senha = Tk()
    titulo_senha.title("Título e senha")
    titulo_senha.configure(background="#808080")
    titulo_senha.geometry("600x600+420+50")
    titulo_senha.resizable(False, False)
    borda = 5

    tk.Label(titulo_senha, bg="#808080",
             text="TÍTULO DE ELEITOR",
             font="Arial 25 bold", ).pack()
    textBox = tk.Entry(titulo_senha, width=20, font="Arial 23")

    textBox.place(relx=0.24, rely=0.3, relwidth=0.5, relheight=0.07)
    textBox.focus()

    def verificacao():
        labelteste["text"] = textBox.get()
        if labelteste["text"] in titulos_usados:  # df_titulo['titulos']:  # mudar para o banco de dados !!!!
            titulo_senha.destroy()
            votacao_gov()

        else:
            erro = Tk()
            erro.title("ERRO")
            erro.configure(bg="gray")
            erro.geometry("600x600+420+50")
            titulo_senha.destroy()
            label_erro = Label(erro, text="TÍTULO INVÁLIDO", font="Arial 25 bold", bg="gray")
            btn_erro = tk.Button(erro,
                                 text="TENTE NOVAMENTE", font="Arial 15 bold", bg="#59a1ff",
                                 command=lambda: [(erro.destroy()), (titulo())])
            label_erro.pack()
            btn_erro.place(relx=0.3, rely=0.2, relwidth=0.4, relheight=0.1)
            erro.mainloop()

    btn2 = tk.Button(titulo_senha, text="CONTINUAR", width=11, command=verificacao, font="Arial 20 bold", bg="#59a1ff")
    btn2.place(relx=0.3, rely=0.45, relwidth=0.4, relheight=0.1)
    btnBack = ttk.Button(titulo_senha, text="voltar", command=lambda: [(titulo_senha.destroy()), ()])
    labelteste = Label(titulo_senha)
    # labelteste.pack()674657
    titulo_senha.mainloop()

#BOTAO INICIAR
btn1 = tk.Button(menu_inicial, text="INICIAR",
                 width=20,
                 font=("Arial 30 bold"),
                 bg="#59a1ff",
                 activebackground="gray",
                 command=lambda: [(menu_inicial.destroy()), (titulo())])
btn1.place(relx=0.25, rely=0.3, relwidth=0.5, relheight=0.2)


menu_inicial.mainloop()