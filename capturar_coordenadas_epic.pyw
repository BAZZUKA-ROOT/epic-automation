import tkinter as tk
import pyautogui
from pynput import keyboard
from datetime import datetime
import os

PASTA_PRINTS = os.path.join(os.path.expanduser("~"), "Desktop", "prints_epic")
os.makedirs(PASTA_PRINTS, exist_ok=True)

coordenadas = []


def pegar_posicao():
    x, y = pyautogui.position()
    return x, y


def atualizar_posicao():
    x, y = pegar_posicao()
    label_posicao.config(text=f"Mouse: X={x}  Y={y}")
    root.after(100, atualizar_posicao)


def salvar_coordenada():
    x, y = pegar_posicao()
    hora = datetime.now().strftime("%H:%M:%S")
    texto = f"{hora}  |  X={x}  Y={y}"
    coordenadas.append(texto)

    lista.insert(tk.END, texto)
    lista.see(tk.END)

    root.clipboard_clear()
    root.clipboard_append(f"{x}, {y}")

    label_status.config(
        text=f"Coordenada salva e copiada: X={x} Y={y}",
        fg="#4ade80"
    )


def tirar_print():
    x, y = pegar_posicao()
    nome = datetime.now().strftime("print_%Y-%m-%d_%H-%M-%S.png")
    caminho = os.path.join(PASTA_PRINTS, nome)

    img = pyautogui.screenshot()
    img.save(caminho)

    label_status.config(
        text=f"Print salvo na Área de Trabalho/prints_epic",
        fg="#60a5fa"
    )


def limpar_lista():
    coordenadas.clear()
    lista.delete(0, tk.END)
    label_status.config(text="Lista limpa.", fg="#facc15")


def sair():
    root.destroy()


def ao_apertar_tecla(key):
    try:
        if key == keyboard.Key.f8:
            root.after(0, salvar_coordenada)

        elif key == keyboard.Key.f9:
            root.after(0, tirar_print)

        elif key == keyboard.Key.f10:
            root.after(0, limpar_lista)

        elif key == keyboard.Key.esc:
            root.after(0, sair)

    except Exception:
        pass


root = tk.Tk()
root.title("Capturador de Coordenadas - Epic")
root.geometry("560x520")
root.resizable(False, False)
root.configure(bg="#121212")
root.attributes("-topmost", True)

largura = 560
altura = 520
x_tela = (root.winfo_screenwidth() // 2) - (largura // 2)
y_tela = (root.winfo_screenheight() // 2) - (altura // 2)
root.geometry(f"{largura}x{altura}+{x_tela}+{y_tela}")

card = tk.Frame(root, bg="#1f1f1f", padx=24, pady=22)
card.pack(fill="both", expand=True, padx=20, pady=20)

tk.Label(
    card,
    text="🎯 Capturador de Coordenadas",
    font=("Segoe UI", 22, "bold"),
    fg="#ffffff",
    bg="#1f1f1f"
).pack(pady=(0, 10))

tk.Label(
    card,
    text="Use isso para descobrir onde o mouse deve clicar no Launcher.",
    font=("Segoe UI", 11),
    fg="#cfcfcf",
    bg="#1f1f1f"
).pack(pady=(0, 18))

label_posicao = tk.Label(
    card,
    text="Mouse: X=0  Y=0",
    font=("Consolas", 18, "bold"),
    fg="#38bdf8",
    bg="#111827",
    padx=16,
    pady=12
)
label_posicao.pack(fill="x", pady=(0, 16))

atalhos = """
F8  = salvar coordenada atual
F9  = tirar print da tela
F10 = limpar lista
ESC = fechar programa
"""

tk.Label(
    card,
    text=atalhos,
    font=("Segoe UI", 11),
    fg="#e5e7eb",
    bg="#1f1f1f",
    justify="left"
).pack(anchor="w")

lista = tk.Listbox(
    card,
    height=9,
    font=("Consolas", 11),
    bg="#0f172a",
    fg="#ffffff",
    selectbackground="#2563eb",
    relief="flat"
)
lista.pack(fill="both", expand=True, pady=12)

label_status = tk.Label(
    card,
    text="Passe o mouse no lugar desejado e aperte F8.",
    font=("Segoe UI", 10),
    fg="#999999",
    bg="#1f1f1f"
)
label_status.pack(pady=(4, 0))

listener = keyboard.Listener(on_press=ao_apertar_tecla)
listener.daemon = True
listener.start()

atualizar_posicao()
root.mainloop()