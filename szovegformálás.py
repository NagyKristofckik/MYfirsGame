import os
import shutil

def kozepreszoveg(szoveg):
    os.system("")
    szelesseg = shutil.get_terminal_size().columns
    elotag = " " * max(0, (szelesseg - len(szoveg)) // 2)
    print(elotag + szoveg)
