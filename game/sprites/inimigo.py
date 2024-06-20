import pygame
import math

class inimigo:
    def __init__(self, screen, player):
        self.screen = screen
        self.player = player
        self.posX = 400
        self.posY = 50
        self.velocity = 2
        self.direction = 1
        self.in_radius = False
        self.life = 3
        self.sound_move = pygame.mixer.Sound("./audios/iSeeYou.mp3")
        self.sound_dano = pygame.mixer.Sound('./audios/dano.mp3')
        self.sound_kill = pygame.mixer.Sound('./audios/kill.mp3')
        self.dano_play = False
        self.kill_play = False

        # Carregar imagens para cada direção
        self.img_direita = pygame.image.load('./Texture/player direita.png')
        self.img_esquerda = pygame.image.load('./Texture/player esquerda.png')
        self.img_cima = pygame.image.load('./Texture/player cima.png')
        self.img_baixo = pygame.image.load('./Texture/player frente.png')
        self.inimigo_img = self.img_direita

    def render(self):
        if self.life > 0:
            self.screen.blit(self.inimigo_img, (self.posX, self.posY))
        else: 
            if not self.kill_play: 
                self.sound_kill.play()
                self.kill_play = True

    def calcular_distancia(self):
        jogador_centro_x = self.player.posX + self.player.player.get_width() // 2
        jogador_centro_y = self.player.posY + self.player.player.get_height() // 2
        inimigo_centro_x = self.posX + self.inimigo_img.get_width() // 2
        inimigo_centro_y = self.posY + self.inimigo_img.get_height() // 2
        distancia = math.sqrt((jogador_centro_x - inimigo_centro_x)**2 + (jogador_centro_y - inimigo_centro_y)**2)
        return distancia

    def mov_Ia(self):
        if self.life > 0:  # Verificar se o inimigo está vivo antes de mover
            distancia = self.calcular_distancia()

            if distancia < 200:
                if not self.in_radius:
                    self.sound_move.play()
                    self.in_radius = True
                # Perseguir o jogador
                if self.player.posX > self.posX:
                    self.inimigo_img = self.img_direita
                    self.direction = 1
                else:
                    self.inimigo_img = self.img_esquerda
                    self.direction = -1
                
                self.posX += self.velocity * self.direction

                if self.player.posY > self.posY:
                    self.inimigo_img = self.img_baixo
                    self.posY += self.velocity
                else:
                    self.inimigo_img = self.img_cima
                    self.posY -= self.velocity
            else:
                if self.in_radius:
                    self.in_radius = False
                # Movimento normal
                if self.posX >= 700:
                    self.inimigo_img = self.img_esquerda
                    self.direction = -1
                elif self.posX <= 300:
                    self.inimigo_img = self.img_direita
                    self.direction = 1
                
                self.posX += self.velocity * self.direction

    def kill_me(self): 
        if self.life > 0:  # Verificar se o inimigo está vivo antes de levar dano
            distancia = self.calcular_distancia()
            if distancia < 150: 
                self.life -= 1
                if self.life <= 0:
                    self.sound_kill.play()
                    self.kill_play = True
                elif not self.dano_play and self.life > 0:
                    self.sound_dano.play()
                    self.dano_play = True
                self.dano_play = False 
