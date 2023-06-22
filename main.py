import os
import platform
import subprocess
import glob
from typing import List

def main() -> None:
    if platform.system() != "Windows":
        exit()

    diretorio_appdata = os.getenv('LOCALAPPDATA')
    if diretorio_appdata is None:
        return

    diretorios_discord = encontrar_diretorios_discord(diretorio_appdata)
    encontrou = False
    for diretorio_discord in diretorios_discord:
        arquivos_js = encontrar_arquivos_js(diretorio_appdata, diretorio_discord)
        for arquivo_js in arquivos_js:
            if contem_token_mfa(arquivo_js):
                print(f'[!] Possible token grabber in {file_js}, opening...')
                subprocess.run(f"notepad.exe {arquivo_js}")
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

if __name__ == '__main__':
    main()
