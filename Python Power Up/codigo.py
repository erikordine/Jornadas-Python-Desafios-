import pyautogui
import time
import pandas as pd

# pyautogui.click -> clickar
# pyautogui.write -> escrever	
# pyautogui.press -> apertar uma tecla
# pyautogui.hotkey -> apertar varias teclas (ctrl + c)
# pyautogui.pause -> ira esperar 1 segundo

# Passo 1: Abrir o sistema da empresa
    # Sistema: https://dlp.hashtagtreinamentos.com/python/intensivao/login

pyautogui.PAUSE = 0.5
pyautogui.press('win')

# Escrever o nome do programa
pyautogui.write('microsoft edge')   

# Abrir o navegador
pyautogui.press('enter')

# Entrou no navegador
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

# Pedir pro computador esperar 3 segundos
time.sleep(1)


# Passo 2: Fazer login
pyautogui.click(x=1150, y=378)
pyautogui.write('teste@gmail.com')

pyautogui.press('tab')
pyautogui.write('ordineerik23456')

pyautogui.press('tab')
pyautogui.press('enter')



# Passo 3: Importar a base de dados de produtos
tabela = pd.read_csv('produtos.csv')

print(tabela)


time.sleep(2)
# Passo 4: Cadastrar 1 produto
for linha in tabela.index:
    pyautogui.click(x=1074, y=251) # primeiro campo

    # Codigo
    codigo = tabela.loc[linha, 'codigo'] # pega a linha e coluna codigo
    pyautogui.write(str(codigo))
    pyautogui.press('tab')

    # Marca
    marca = tabela.loc[linha, 'marca'] # pega a linha e coluna marca
    pyautogui.write(str(marca))
    pyautogui.press('tab')

    # Tipo
    tipo = tabela.loc[linha, 'tipo'] # pega a linha e coluna tipo
    pyautogui.write(str(tipo))
    pyautogui.press('tab')

    # categoria
    categoria = tabela.loc[linha, 'categoria'] # pega a linha e coluna categoria
    pyautogui.write(str(categoria))
    pyautogui.press('tab')

    # preco_unitario
    preco_unitario = tabela.loc[linha, 'preco_unitario'] # pega a linha e coluna 
    pyautogui.write(str(preco_unitario))
    pyautogui.press('tab')

    # custo
    custo = tabela.loc[linha, 'custo'] # pega a linha e coluna custo
    pyautogui.write(str(custo))
    pyautogui.press('tab')

    # obs
    obs = str(tabela.loc[linha, 'obs']) # pega a linha e coluna obs

    if obs != 'nan':
        pyautogui.write(obs)
    
    pyautogui.press('tab') # vai para o proximo campo

    pyautogui.press('enter') # cadastra o produto12.4   

    # numero positivo do scroll para cima
    # numero negativo do scroll para baixo
    pyautogui.scroll(10000)








# Passo 5: Repetir o passo 4 até o fim da base de dados

