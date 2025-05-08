
import sys,os,keyboard,time,pyautogui

# Kurzor elrejtése
sys.stdout.write("\033[?25l")
sys.stdout.flush()


import os
from szovegformálás import kozepreszoveg as kozep
def kepfrisites(menu_items,jelenlegipont):
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(len(menu_items)):
                szoveg = menu_items[i]
                if jelenlegipont == i:
                    kozep(f"> {szoveg} <")
                else:
                    kozep(szoveg)

def menu():
    fut=True
    menu_items = ["Start", "Beállítások", "Kilépés"]
    jelenlegipont=-1
    kepfrisites(menu_items,jelenlegipont)
    # while fut:
    #     for event in pygame.event.get(): 
    #         if event.type == pygame.KEYDOWN:
    #                 if event.key == pygame.K_UP:
    #                     if jelenlegipont!=0:
    #                         jelenlegipont -= 1  
    #                         kepfrisites(menu_items,jelenlegipont)
    #                 elif event.key == pygame.K_DOWN:
    #                     if jelenlegipont !=2:
    #                         jelenlegipont += 1  
    #                         kepfrisites(menu_items,jelenlegipont)
    #                 elif event.key == pygame.K_RETURN:
    #                     if jelenlegipont ==2:
    #                         pygame.quit()
    #                         sys.exit()
    while fut:
        if keyboard.is_pressed('up') and jelenlegipont==-1:
             jelenlegipont=3
        if keyboard.is_pressed('up') and jelenlegipont > 0:
            jelenlegipont -= 1
            kepfrisites(menu_items, jelenlegipont)

        if keyboard.is_pressed('down') and jelenlegipont < len(menu_items) - 1:
            jelenlegipont += 1
            kepfrisites(menu_items, jelenlegipont)

        if keyboard.is_pressed('enter'):

            if jelenlegipont == 2 and menu_items[2]=="Vissza":
                menu_items = ["Start", "Beállítások", "Kilépés"]
                jelenlegipont=-1
                kepfrisites(menu_items, jelenlegipont)
                time.sleep(0.1) 

            elif jelenlegipont == 2:
                print("Kilépés...")
                sys.exit()

            if jelenlegipont == 1 and menu_items[1]=="Beállítások":
                jelenlegipont=-1
                menu_items = ["Valami", "Fullscreen", "Vissza"]
                kepfrisites(menu_items, jelenlegipont)

            if jelenlegipont == 1 and menu_items[1]=="Fullscreen":
                pyautogui.press('f11')
                kepfrisites(menu_items, jelenlegipont)
                 
           
                 

        time.sleep(0.1) 
