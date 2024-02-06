import tkinter as tk
from tkinter import ttk
from decimal import Decimal

def calcular_apostas(valor_total, odd_aposta1, odd_aposta2):
    melhor_retorno = Decimal('0.00')
    melhor_aposta1 = Decimal('0.00')
    melhor_aposta2 = Decimal('0.00')

    for centavos_aposta1 in range(1, int(valor_total * 100)):
        aposta1 = Decimal(centavos_aposta1) / Decimal(100)
        aposta2 = valor_total - aposta1

        retorno_aposta1 = aposta1 * odd_aposta1
        retorno_aposta2 = aposta2 * odd_aposta2

        retorno_total = min(retorno_aposta1, retorno_aposta2)
        if retorno_total > melhor_retorno:
            melhor_retorno = retorno_total
            melhor_aposta1 = aposta1
            melhor_aposta2 = aposta2

    if melhor_retorno > valor_total:
        return melhor_aposta1, melhor_aposta2, melhor_retorno
    else:
        return None

def calcular_e_mostrar_resultado(event=None):
    try:
        valor_total = Decimal(valor_total_entry.get().replace(',', '.'))
        odd_aposta1 = Decimal(odd_aposta1_entry.get().replace(',', '.'))
        odd_aposta2 = Decimal(odd_aposta2_entry.get().replace(',', '.'))

        resultado = calcular_apostas(valor_total, odd_aposta1, odd_aposta2)

        if resultado:
            aposta1, aposta2, melhor_retorno = resultado
            resultado_label.config(text=f"Aposta 1: Apostei {aposta1:.2f}, Retorno: {melhor_retorno:.2f}\n"
                                        f"Aposta 2: Apostei {aposta2:.2f}, Retorno: {melhor_retorno:.2f}")
        else:
            resultado_label.config(text=f"Não é possível realizar as apostas para obter um retorno acima de {valor_total}.")
    except ValueError:
        resultado_label.config(text="Por favor, insira valores válidos.")

# Criar a janela principal
window = tk.Tk()
window.title("Calculadora de Apostas")

# Criar widgets
frame = ttk.Frame(window, padding="20")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

valor_total_label = ttk.Label(frame, text="Valor Total para Apostar:")
valor_total_entry = ttk.Entry(frame)
valor_total_entry.insert(0, "10.00")  # Valor padrão com ponto
odd_aposta1_label = ttk.Label(frame, text="Odd Aposta 1:")
odd_aposta1_entry = ttk.Entry(frame)
odd_aposta2_label = ttk.Label(frame, text="Odd Aposta 2:")
odd_aposta2_entry = ttk.Entry(frame)
calcular_button = ttk.Button(frame, text="Calcular", command=calcular_e_mostrar_resultado)

# Rótulo de resultado
resultado_label = ttk.Label(frame, text="", font=("Helvetica", 12), wraplength=300)

# Posicionar widgets na janela
valor_total_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
valor_total_entry.grid(row=0, column=1, padx=10, pady=10, sticky=tk.E)
odd_aposta1_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
odd_aposta1_entry.grid(row=1, column=1, padx=10, pady=10, sticky=tk.E)
odd_aposta2_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
odd_aposta2_entry.grid(row=2, column=1, padx=10, pady=10, sticky=tk.E)
calcular_button.grid(row=3, column=0, columnspan=2, pady=10)
resultado_label.grid(row=4, column=0, columnspan=2, pady=(10, 0))

# Adicionando vinculação da tecla Enter ao evento de calcular
window.bind('<Return>', calcular_e_mostrar_resultado)

# Iniciar a aplicação
window.mainloop()
