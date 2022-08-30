import platform
if platform.system() != "Windows":
    exit()
import os
import subprocess
import glob

appdata = os.getenv('LOCALAPPDATA')

if appdata != None:
    nooo = [f for f in os.listdir(appdata) if os.path.isdir(appdata + f'\{f}') and 'Discord' in f]
    for lmao in nooo:
        kk = glob.glob(appdata + f'\{lmao}\**\*.js', recursive=True)
        for lol in kk:
            if open(lol, "r").read().__contains__('mfa.'):
                print(f'\n[!] possible token grabber in {lol}, opening...')
                subprocess.run(f"notepad.exe {lol}")
