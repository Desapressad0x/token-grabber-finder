import os
import platform
import subprocess
import glob
from typing import List

def main() -> None:
    diretorio_appdata = os.getenv('LOCALAPPDATA') if platform.system() == "Windows" else (os.path.expanduser('~/Library/Application Support') if platform.system() == "Darwin" else os.path.expanduser('~'))

    if diretorio_appdata is None:
        return

    diretorios_discord = encontrar_diretorios_discord(diretorio_appdata)
    encontrou = False
    for diretorio_discord in diretorios_discord:
        arquivos_js = encontrar_arquivos_js(diretorio_appdata, diretorio_discord)
        for arquivo_js in arquivos_js:
            if contem_token_mfa(arquivo_js):
                print(f'[!] Possible token grabber in {arquivo_js}, opening...')
                abrir(arquivo_js)
                encontrou = True
    if not encontrou:
        print('[!] No suspicious file was found.')

def encontrar_diretorios_discord(diretorio_main: str) -> List[str]:
    diretorios_discord = []
    for diretorio in os.listdir(diretorio_main):
        if os.path.isdir(os.path.join(diretorio_main, diretorio)) and 'Discord' in diretorio:
            diretorios_discord.append(diretorio)
    return diretorios_discord

def encontrar_arquivos_js(diretorio_appdata: str, diretorio_discord: str) -> List[str]:
    return glob.glob(os.path.join(diretorio_appdata, diretorio_discord, '**', '*.js'), recursive=True)

def contem_token_mfa(arquivo_js: str) -> bool:
    with open(arquivo_js, 'r') as f:
        conteudo = f.read()
        return 'mfa.' in conteudo

def abrir(arquivo: str) -> None:
    if platform.system() == "Windows":
        subprocess.run(["notepad.exe", arquivo])
    elif platform.system() == "Darwin":
        try:
            subprocess.run(["open", "-t", arquivo])
        except:
            subprocess.run(["nano", arquivo])
    elif platform.system() == "Linux":
        try:
            subprocess.run(["xdg-open", arquivo])
        except:
            subprocess.run(["vim", arquivo])

if __name__ == '__main__':
    main()
