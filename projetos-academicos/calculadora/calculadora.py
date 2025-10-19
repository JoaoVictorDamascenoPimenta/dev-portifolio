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

# Janela principal
janela = tk.Tk()
janela.title("Calculadora de Soma")
janela.geometry("300x200")

# Campos de entrada
tk.Label(janela, text="Número 1:").pack(pady=5)
entry1 = tk.Entry(janela)
entry1.pack()

tk.Label(janela, text="Número 2:").pack(pady=5)
entry2 = tk.Entry(janela)
entry2.pack()

# Botão de soma
tk.Button(janela, text="Somar", command=somar).pack(pady=10)

# Label do resultado
label_resultado = tk.Label(janela, text="Resultado:")
label_resultado.pack(pady=5)

# Executa a janela
janela.mainloop()