import pygame
import random


class Word: 
    def __init__(self,screen) -> None:
        self.word_image = pygame.image.load('./Texture/word.png')
        self.word_image = pygame.transform.scale(self.word_image, (500,600))
        self.word_image2 = pygame.transform.flip(self.word_image,True,False)
        self.screen = screen

    def render(self): 
        self.screen.blit(self.word_image,(0,0))
        self.screen.blit(self.word_image2,(500,0))

class arvores: 
    def __init__(self,screen) -> None:
        self.arvore_grande = pygame.image.load('./Texture/arvore.png')
        self.arvore_pequena = pygame.image.load('./Texture/arvorePequena.png')
        self.screen = screen
        self.vecX = 200 
        self.vecY = -10

        self.vecX2 = 670
        self.vecY2 = -10

    def render(self):
        spacing = 0
        spacing2 = 0 
        for _ in range(3): 
            self.screen.blit(self.arvore_grande, (self.vecX,self.vecY + spacing))
            spacing += 60
        for _ in range(3): 
            self.screen.blit(self.arvore_grande, (self.vecX2, self.vecY + spacing2))
            spacing2 += 60

class Caixa: 
    def __init__(self, screen, player):
        self.player = player
        self.caixa = pygame.image.load('./Texture/caixa.png')
        self.screen = screen
        self.vecX = 400
        self.vecY = 500
        self.life = 1

        self.audios = [
            pygame.mixer.Sound('./audios/wood-smash-3.mp3'),
            pygame.mixer.Sound('./audios/box-chash.mp3'),
            pygame.mixer.Sound('./audios/wood-crash.mp3')
        ]
        self.audio_playing = False

    def render(self):
        if self.life > 0: 
           self.screen.blit(self.caixa, (self.vecX, self.vecY))
           largura = self.caixa.get_width()
           altura = self.caixa.get_height()
           player_largura = self.player.player.get_width()
           player_altura = self.player.player.get_height()

           self.caixa_rect = pygame.Rect(self.vecX, self.vecY, largura, altura)
           self.player_rect = pygame.Rect(self.player.posX, self.player.posY, player_largura, player_altura-20)

           if self.caixa_rect.colliderect(self.player_rect): 
              deltaX = self.player_rect.centerx - self.caixa_rect.centerx
              deltaY = self.player_rect.centery - self.caixa_rect.centery

              if abs(deltaX) > abs(deltaY): 
                   if deltaX > 0:  
                      if self.vecX > 15:
                         self.vecX -= 5
                   else: 
                      if self.vecX < 960:
                         self.vecX += 5
              else:  
                   if deltaY > 0:  
                      if self.vecY > 15: 
                        self.vecY -= 5
                   else: 
                      if self.vecY < 550:
                        self.vecY += 5

        else: 
            if not self.audio_playing:
                audio_index = random.randint(0, len(self.audios) - 1)
                selected_audio = self.audios[audio_index]
                
                selected_audio.play()
                self.audio_playing = True

class bancos: 
    def __init__(self,screen) -> None:
        self.banco_frente = pygame.image.load('./Texture/banco.png')
        self.screen = screen
        self.vecX = 320

    def render(self): 
        spacing = 0
        for vecX in range(5): 
            self.screen.blit(self.banco_frente, (self.vecX + spacing,295))
            spacing += 80

class Pilar: 
    def __init__(self,screen) -> None:
        self.pilar = pygame.image.load('./Texture/pilar.png')
        self.screen = screen
        self.posX = 250
        self.posY = 260
        self.posX2 = 720

    def render(self): 
        self.screen.blit(self.pilar, (self.posX,self.posY))
        self.screen.blit(self.pilar, (self.posX2,self.posY))

class templo:
    def __init__(self,screen) -> None:
        self.templo = pygame.image.load('./Texture/templo.png')
        self.screen = screen
    def render(self): 
        self.screen.blit(self.templo, (450,410))

class barril:
    def __init__(self, screen, player) -> None:
        self.barril = pygame.image.load('./Texture/barril.png')
        self.screen = screen
        self.player = player
        self.VecX = 200
        self.VecY = 300
        self.life = 1
        self.audios = [
            pygame.mixer.Sound('./audios/wood-smash-3.mp3'),
            pygame.mixer.Sound('./audios/box-chash.mp3'),
            pygame.mixer.Sound('./audios/wood-crash.mp3')
        ]
        self.audio_playing = False


    def render(self): 
        if self.life > 0:
            self.screen.blit(self.barril, (self.VecX, self.VecY))
            barril_height = self.barril.get_height()
            barril_width = self.barril.get_width()
            player_height = self.player.player.get_height()
            player_width = self.player.player.get_width()

            barril_rect = pygame.Rect(self.VecX, self.VecY, barril_width, barril_height - 20)
            player_rect = pygame.Rect(self.player.posX, self.player.posY, player_width, player_height)

            if player_rect.colliderect(barril_rect):
                deltaX = player_rect.centerx - barril_rect.centerx
                deltaY = player_rect.centery - barril_rect.centery
            
                if abs(deltaX) > abs(deltaY): 
                   if deltaX > 0:  
                       if self.VecX > 15:
                          self.VecX -= 5
                   else:  
                       if self.VecX < 960:
                         self.VecX += 5
                else:  
                   if deltaY > 0:  
                     if self.VecY > 15: 
                        self.VecY -= 5
                   else:  
                     if self.VecY < 550:
                        self.VecY += 5    
        else:
            if not self.audio_playing:
                audio_index = random.randint(0, len(self.audios) - 1)
                selected_audio = self.audios[audio_index]
                
                selected_audio.play()
                self.audio_playing = True

class Bau: 
    def __init__(self, screen, player) -> None:
        self.bau_image = pygame.image.load('./Texture/bau_fechado.png')
        self.screen = screen
        self.player = player
        self.vecX = 500
        self.vecY = 10
        self.draw_items = False
        self.chester_song = pygame.mixer.Sound('./audios/abrir_bau.mp3')
        self.audio_playing = False
        self.coins = []
        self.coin_max_distance = 50
        self.coin_radius = 10

    def spawn_coins(self):
        screen_width, screen_height = self.screen.get_size()
        for _ in range(random.randint(3,10)):  # Number of coins
            angle = random.uniform(0, 2 * 3.14159)  # Random angle
            vector = pygame.math.Vector2(self.coin_max_distance, 0).rotate_rad(angle)
            final_x = self.vecX + vector.x
            final_y = self.vecY + vector.y

            # Ensure coins don't spawn outside the screen
            if final_x < 20: final_x = random.randint(20,50)
            if final_y < 20: final_y = random.randint(20,50)

            self.coins.append({
                'x': self.vecX,
                'y': self.vecY,
                'target_x': final_x,
                'target_y': final_y,
                'dx': (final_x - self.vecX) / 30,  # Smooth movement
                'dy': (final_y - self.vecY) / 30   # Smooth movement
            })

    def update_coins(self):
        for coin in self.coins:
            if (abs(coin['x'] - coin['target_x']) > abs(coin['dx']) or 
                abs(coin['y'] - coin['target_y']) > abs(coin['dy'])):
                coin['x'] += coin['dx']
                coin['y'] += coin['dy']
            else:
                coin['x'] = coin['target_x']
                coin['y'] = coin['target_y']

    def render(self):
        self.screen.blit(self.bau_image, (self.vecX, self.vecY))
        keys = pygame.key.get_pressed()
        bau_rect = pygame.Rect(self.vecX, self.vecY, self.bau_image.get_width() + 200, self.bau_image.get_height() + 200)
        player_rect = pygame.Rect(self.player.posX, self.player.posY, self.player.player.get_width(), self.player.player.get_height())
        
        if keys[pygame.K_e]:
            if player_rect.colliderect(bau_rect):
                self.bau_image = pygame.image.load('./Texture/bau_aberto.png')
                self.draw_items = True
                if not self.audio_playing:
                    self.chester_song.play()
                    self.audio_playing = True
                if not self.coins:  # Spawn coins only once
                    self.spawn_coins()

        if self.draw_items:
            self.update_coins()
            for coin in self.coins:
                pygame.draw.circle(self.screen, (255, 255, 0), (int(coin['x']), int(coin['y'])), self.coin_radius)