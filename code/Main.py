import pygame
from Menu import Menu
from Jogo import executar_jogo

while True:
    pygame.init()
    menu = Menu()
    opcao = menu.run()

    if opcao == "start":
        executar_jogo()
    else:
        break