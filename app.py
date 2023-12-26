# Importando as bibliotecas necessárias
import pyautogui
import time

# Configurando pausas e ativação do "failsafe" no pyautogui
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

# Abrindo a execução do prompt de comando e digitando a URL
pyautogui.hotkey("win", "r")
pyautogui.typewrite("https://www.gabrielcasemiro.com.br/atividade_pyautogui \n")

# Esperando a página carregar (5 segundos)
time.sleep(5)

# Abrindo o arquivo CSV e ignorando o cabeçalho
with open("membros.csv") as f:
    next(f)  # Ignorando a primeira linha (cabeçalho)

    # Iterando sobre as linhas do arquivo CSV
    for line in f:
        line = line.strip()
        line = line.split(";")
        print("Dados: ", line)

        # Extraindo dados da linha
        name = line[0]
        sex = line[1]
        email = line[2]
        phone = line[3]

        # Preenchendo campos na página com base nos dados do CSV
        pyautogui.click(pyautogui.locateCenterOnScreen("img\\nome.png", confidence=0.8), duration=1)
        pyautogui.typewrite(name, interval=0.25)

        pyautogui.click(pyautogui.locateCenterOnScreen("img\\email.png", confidence=0.8), duration=1)
        pyautogui.typewrite(email, interval=0.25)

        pyautogui.click(pyautogui.locateCenterOnScreen("img\\telefone.png", confidence=0.8), duration=1)
        pyautogui.typewrite(phone, interval=0.25)

        pyautogui.click(pyautogui.locateCenterOnScreen("img\\sexo.png", confidence=0.8), duration=1)

        # Selecionando o sexo com base nos dados do CSV
        if sex == "Masculino":
            pyautogui.click(pyautogui.locateCenterOnScreen("img\\masculino.png", confidence=0.8), duration=1)
        else:
            pyautogui.click(pyautogui.locateCenterOnScreen("img\\feminino.png", confidence=0.8), duration=1)

        # Capturando uma screenshot do formulário preenchido
        pyautogui.screenshot(f"cadastro_{name}.png")

        # Clicando no botão de envio do formulário
        pyautogui.click(pyautogui.locateCenterOnScreen("img\\botao_enviar.png", confidence=0.8), duration=1)

        # Aguardando 3 segundos antes de prosseguir para a próxima iteração
        time.sleep(3)

# Exibindo um alerta indicando que o programa foi finalizado com sucesso
pyautogui.alert(text="Programa finalizado com sucesso!", title="Aviso do sistema", button="OK")
