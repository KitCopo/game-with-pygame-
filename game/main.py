import pygame
from sprites.player import Player
from sprites.mundo import *
from sprites.inimigo import inimigo

class Game: 
    def __init__(self) -> None:
        pygame.init()
        pygame.mixer.init()
        self.screen_size = (1000, 600)
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption("meu jogo")

        self.word = Word(self.screen)
        self.arvore = arvores(self.screen)
        self.pilar = Pilar(self.screen)
        self.barril = barril(self.screen, None)  # Inicializar barril primeiro
        self.player = Player(self.screen, self.pilar, None, self.barril)  # Passar barril para player
        self.caixa = Caixa(self.screen, self.player)  # Inicializar self.caixa com self.player
        self.player.caixa = self.caixa  # Definir self.caixa no player
        self.player.barril = self.barril  # Definir barril no player
        self.barril.player = self.player  # Definir player no barril
        self.inimigo = inimigo(self.screen, self.player)
        self.bancos = bancos(self.screen)
        self.templo = templo(self.screen)
        self.bau = Bau(self.screen,self.player)

    def render(self):
        self.screen.fill((255, 255, 255))
        self.word.render()
        self.bancos.render()
        self.templo.render()
        self.barril.render()
        self.caixa.render()
        self.player.render()
        self.inimigo.render()
        self.inimigo.mov_Ia()
        self.pilar.render()
        self.arvore.render()
        self.bau.render()

        pygame.display.flip()

    def update(self):
        running = True
        clock = pygame.time.Clock() 
        while running: 
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    running = False 
                
                elif event.type == pygame.MOUSEBUTTONDOWN: 
                    if event.button == 1: 
                        self.player.attack()
                        self.inimigo.kill_me()

            self.player.mov()
            self.render()
            clock.tick(60)

if __name__ == "__main__": 
    game = Game()
    game.update()
    pygame.quit()
