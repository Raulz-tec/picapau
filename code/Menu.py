import pygame
import sys

from code.const import COLOR_RED, MENU_OPTION


class Menu:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((500, 800))
        pygame.display.set_caption("Menu")
        self.font = pygame.font.SysFont('arial black', 40)
        self.bg = pygame.image.load('MenuBg.png')
        self.clock = pygame.time.Clock()

    def draw_text(self, text, x, y):
        surface = self.font.render(text, True, (COLOR_RED))
        rect = surface.get_rect(center=(x, y))
        self.window.blit(surface, rect)
        return rect

    def run(self):
        while True:
            self.clock.tick(60)
            self.window.blit(self.bg, (0, 0))
            title = self.draw_text('WOODPECKER', 250, 150)
            btn_start = self.draw_text("Iniciar", 250, 600)
            btn_quit = self.draw_text("Sair", 250, 700)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if btn_start.collidepoint(event.pos):
                        return "start"
                    if btn_quit.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()