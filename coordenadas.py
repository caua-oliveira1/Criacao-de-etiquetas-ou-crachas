import pyautogui
import time

print("Deixe o canva na tela! 5 segundos")
time.sleep(5)

print("Aperte ctrl+c para parar")
try:
    while True:
        x, y = pyautogui.position()
        print(f"Posição atual: x={x}, y={y}")
        time.sleep(1)
except KeyboardInterrupt:
    print("\nFinalizado")