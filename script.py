import pandas as pd
import pyautogui
import time
import os

#Configure antes de usar!

#Pega o endereco desse script e baixa em uma pasta "crachas"
pasta_script = os.path.dirname(os.path.abspath(__file__))
pasta_crachas = os.path.join(pasta_script, "crachas")
os.makedirs(pasta_crachas, exist_ok=True)

# Lê a planilha que deve estar na mesma pasta do script
caminho_planilha = os.path.join(pasta_script, "dados.xlsx")
df = pd.read_excel(caminho_planilha)

#Coordenadas dos textos canva, o primeiro valor e o X, e o segundo Y
campo_nome = (512, 457)
campo_turma = (508, 591)
campo_cargo = (506, 697)

#Coordenadas do download canva
botao_compartilhar = (721, 112)
botao_baixar_menu = (597, 580)
botao_baixar_confirmar = (646, 554)

TEMPO_ESPERA_DOWNLOAD = 6  #Em segundos, mude de acordo com seu pc/internet


print("Você tem 5 segundos para deixar o canva na tela")
time.sleep(5) #Espera 5 segundos

total_linhas = len(df)
processados = 0
pulados = 0

for index, row in df.iterrows():
    nome = str(row["Nome"]).strip()
    turma = str(row["Turma"]).strip()
    cargo = str(row["Cargo"]).strip()

    #Monta o caminho completo, pasta + nome do arquivo
    caminho_completo = os.path.join(pasta_crachas, f"{nome}.png")

    #Verifica se esse cracha ja existe
    if os.path.exists(caminho_completo):
        print(f"Já existe {nome}, indo para o proximo")
        pulados += 1
        continue

    try:
        #Preenche campo nome
        pyautogui.doubleClick(*campo_nome)
        time.sleep(0.4)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.write(nome, interval=0.02)
        pyautogui.press('esc')
        time.sleep(0.4)

        #Preenche campo turma
        pyautogui.doubleClick(*campo_turma)
        time.sleep(0.4)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.write(turma, interval=0.02)
        pyautogui.press('esc')
        time.sleep(0.4)

        #Preenche campo cargo
        pyautogui.doubleClick(*campo_cargo)
        time.sleep(0.4)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.write(cargo, interval=0.02)
        pyautogui.press('esc')
        time.sleep(0.4)

        #Download
        pyautogui.click(*botao_compartilhar)
        time.sleep(1)
        pyautogui.click(*botao_baixar_menu)
        time.sleep(1)
        pyautogui.click(*botao_baixar_confirmar)

        print("Aguardando janela 'Salvar como'...")
        time.sleep(TEMPO_ESPERA_DOWNLOAD)

        # Digita o caminho completo na caixa de nome do arquivo e confirma
        pyautogui.hotkey('ctrl', 'a')  # seleciona o nome padrão sugerido
        pyautogui.write(caminho_completo, interval=0.02)
        time.sleep(0.3)
        pyautogui.press('enter')
        time.sleep(1.5)  # tempo para o arquivo terminar de salvar

        print(f"Salvo em: {caminho_completo}")
        processados += 1

    except Exception as erro:
        print(f"ERRO ao processar {nome}: {erro}")

    print("-" * 40)
    time.sleep(1)

print(f"Crachas gerados: {processados}")
