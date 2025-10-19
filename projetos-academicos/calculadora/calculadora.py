import tkinter as tk
from tkinter import messagebox

def somar():
    try:
        n1 = float(entry1.get())
        n2 = float(entry2.get())
        resultado = n1 + n2
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Digite apenas números!")

def subtrair():
    try:
        n1 = float(entry1.get())
        n2 = float(entry2.get())
        resultado = n1 - n2
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Digite apenas números!")

# Janela principal
janela = tk.Tk()
janela.title("Calculadora Simples")
janela.geometry("300x220")

# Campos de entrada
tk.Label(janela, text="Número 1:").pack(pady=5)
entry1 = tk.Entry(janela)
entry1.pack()

tk.Label(janela, text="Número 2:").pack(pady=5)
entry2 = tk.Entry(janela)
entry2.pack()

# Botões de operações
frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=10)

tk.Button(frame_botoes, text="Somar", width=10, command=somar).grid(row=0, column=0, padx=5)
tk.Button(frame_botoes, text="Subtrair", width=10, command=subtrair).grid(row=0, column=1, padx=5)

# Label do resultado
label_resultado = tk.Label(janela, text="Resultado:")
label_resultado.pack(pady=10)

# Executa a janela
janela.mainloop()