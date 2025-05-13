import tkinter as tk
import random

def atualizar_lista():
    nome = entry_nome.get()
    idade = int(entry_idade.get())
    peso = float(entry_peso.get())
    lista_exercicios = []
    if idade < 30:
        lista_exercicios = [
            "Segunda-feira - Membros Superiores:",
            "Supino reto (4x10) - Descanso: 1 minuto",
            "Rosca direta (3x12) - Descanso: 45 segundos",
            "Supino fechado (4x10) - Descanso: 1 minuto",
            "Tríceps francês (3x12) - Descanso: 45 segundos",
            "",
            "Terça-feira - Membros Inferiores:",
            "Agachamento (4x10) - Descanso: 1 minuto",
            "Leg press 45° (3x12) - Descanso: 45 segundos",
            "Cadeira extensora (3x12) - Descanso: 45 segundos",
            "Banco romano (4x10) - Descanso: 1 minuto",
            "",
            "Quarta-feira - Membros Superiores:",
            "Desenvolvimento de ombros (4x10) - Descanso: 1 minuto",
            "Tríceps pulley (3x12) - Descanso: 45 segundos",
            "Rosca Martelo (3x12) - Descanso: 45 segundos",
            "",
            "Quinta-feira - Membros Inferiores:",
            "Cadeira extensora (3x12) - Descanso: 45 segundos",
            "Flexora deitado (3x12) - Descanso: 45 segundos",
            "",
            "Sexta-feira - Abdômen:",
            "Prancha (3x30 segundos) - Descanso: 30 segundos",
            "Crunch",
            ""
        ]
    else:
        lista_exercicios = [
            "Segunda-feira - Membros Superiores:",
            "Supino inclinado (4x10) - Descanso: 1 minuto",
            "Rosca alternada (3x12) - Descanso: 45 segundos",
            "",
            "Terça-feira - Membros Inferiores:",
            "Agachamento livre (4x10) - Descanso: 1 minuto",
            "Cadeira extensora (3x12) - Descanso: 45 segundos",
            "Elevação de glúteo (3x12) - Descanso: 45 segundos",
            "",
            "Quarta-feira - Membros Superiores:",
            "Desenvolvimento militar (4x10) - Descanso: 1 minuto",
            "Tríceps francês (3x12) - Descanso: 45 segundos",
            "Elevação frontal (3x12) - Descanso: 45 segundos",
            "Elevação lateral (3x12) - Descanso: 45 segundos",
            "Desenvolvimento (3x12) - Descanso: 1 minuto",
            "",
            "Quinta-feira - Membros Inferiores:",
            "Leg press 45° (3x12) - Descanso: 45 segundos",
            "Stiff (3x12) - Descanso: 45 segundos",
            "Agachamento livre (3x12) - Descanso: 45 segundos",
            "Levantamento terra romeno",
            "",
            "Sexta-feira - Abdômen:",
            "Prancha lateral (3x30 segundos) - Descanso: 30 segundos",
            "Elevação de pernas suspenso",
            "Abdominal supra",
            "Abdominal infra"
        ]
    listbox_exercicios.delete(0, tk.END)
    for exercicio in lista_exercicios:
        listbox_exercicios.insert(tk.END, exercicio)

    
    with open("lista_exercicios.txt", "w") as arquivo:
        for exercicio in lista_exercicios:
            arquivo.write(exercicio + "\n")
    def realizar_pesquisa():
        resultado_label.config(text="Atualizar Lista")
        janela = tk.Tk()
janela.title("Ficha de Treino")

largura = 902
altura = 564

background_photo = tk.PhotoImage(file="FUNDOOO.png")

background_label = tk.Label(janela, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()
pos_x = int((largura_tela / 1) - (largura / 1))
pos_y = int((altura_tela / 1) - (altura / 1))
janela.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")

label_nome = tk.Label(janela, text="Nome:")
label_nome.pack()
entry_nome = tk.Entry()
entry_nome.pack()

label_idade = tk.Label(janela, text="Idade:")
label_idade.pack(pady=5)
entry_idade = tk.Entry(janela, font=("TkDefaultFont", 10))
entry_idade.pack(pady=5)

label_peso = tk.Label(janela, text="Peso:")
label_peso.pack(pady=5)
entry_peso = tk.Entry(janela, font=("TkDefaultFont", 10))
entry_peso.pack(pady=5)

botao_atualizar = tk.Button(janela, text="Atualizar Lista", command=atualizar_lista)
botao_atualizar.pack(pady=10)

listbox_exercicios = tk.Listbox(janela, font=("TkDefaultFont", 20))
listbox_exercicios.pack()
resultado_label = tk.Label(janela)
resultado_label.pack()

janela.mainloop()
