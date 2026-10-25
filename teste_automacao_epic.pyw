import pyautogui
import time
import keyboard

# ============================================
# CONFIG
# ============================================

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 1

cancelado = False

# ============================================
# CANCELAR
# ============================================

def cancelar():
    global cancelado
    cancelado = True
    print("\n❌ AUTOMAÇÃO CANCELADA PELO USUÁRIO")


keyboard.add_hotkey(
    "f6",
    cancelar
)

# ============================================
# FUNÇÕES
# ============================================

def verificar_cancelamento():
    if cancelado:
        raise Exception("Execução cancelada")


def mover_click(x, y, texto=""):
    verificar_cancelamento()

    print(f"\n➡ Indo para {texto} ({x}, {y})")

    pyautogui.moveTo(
        x,
        y,
        duration=1.2
    )

    verificar_cancelamento()

    time.sleep(1)

    pyautogui.click()

    print(f"✅ Click realizado em {texto}")

    time.sleep(2)


def scroll_baixo(valor=500):
    verificar_cancelamento()

    print(f"\n🖱 Scrollando {valor}")

    pyautogui.scroll(-valor)

    time.sleep(2)

# ============================================
# INÍCIO
# ============================================

try:
    print("🚀 Automação iniciando em 5 segundos...")
    print("⚠ NÃO mexa no mouse!")
    print("🛑 Aperte F6 para cancelar")

    time.sleep(5)

    # ============================================
    # TESTE
    # ============================================

    mover_click(
        1143,
        151,
        "Botão exemplo 1"
    )

    scroll_baixo(3000)

    mover_click(
        677,
        434,
        "Botão exemplo 2"
    )

    mover_click(
        1449,
        882,
        "Botão exemplo 3"
    )

    scroll_baixo(700)

    mover_click(
        976,
        761,
        "Botão exemplo 4"
    )

    mover_click(
        503,
        182,
        "Botão exemplo 5"
    )

    scroll_baixo(800)

    print("\n✅ TESTE FINALIZADO")

except Exception as e:
    print(f"\n🛑 {e}")