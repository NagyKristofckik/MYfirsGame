
import sys,os,keyboard,time

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
    jelenlegipont=0
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
        if keyboard.is_pressed('up') and jelenlegipont > 0:
            jelenlegipont -= 1
            kepfrisites(menu_items, jelenlegipont)

        if keyboard.is_pressed('down') and jelenlegipont < len(menu_items) - 1:
            jelenlegipont += 1
            kepfrisites(menu_items, jelenlegipont)

        if keyboard.is_pressed('enter'):
            if jelenlegipont == 2:
                print("Kilépés...")
                sys.exit()

        time.sleep(0.1) 
