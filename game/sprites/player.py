import pygame

class Player: 
    def __init__(self, screen, pilar, caixa, barril) -> None:
        self.player_image = pygame.image.load('./Texture/player frente.png')
        self.pilar = pilar
        self.caixa = caixa
        self.barril = barril
        self.VecX = 20
        self.VecY = self.VecX + 30
        self.player = pygame.transform.scale(self.player_image, (self.VecX, self.VecY))
        self.screen = screen
        self.posX = 485
        self.posY = 405
        self.velocity = 4
        self.sound_move = pygame.mixer.Sound("./audios/sand-walk-106366.mp3")
        self.sound_playing = False
        self.attack_song = pygame.mixer.Sound('./audios/attack.mp3')
        self.attack_playing = False
        self.criar = False

        self.attack_imgs = [
            pygame.image.load('./Texture/SP203_01.png'),
            pygame.image.load('./Texture/SP203_02.png'),
            pygame.image.load('./Texture/SP203_03.png'),
            pygame.image.load('./Texture/SP203_04.png'),
            pygame.image.load('./Texture/SP203_05.png'),
            pygame.image.load('./Texture/SP203_06.png'),
            pygame.image.load('./Texture/SP203_07.png')
        ]

        self.attack_imgs = [pygame.transform.scale(img, (120, 100)) for img in self.attack_imgs]
        self.player_height_adjustment = 15  
        self.is_attacking = False  
        self.attack_frame = 0
        self.attack_duration = len(self.attack_imgs)
        self.attack_timer = 0  

    def attack(self):
        self.is_attacking = True
        self.attack_timer = self.attack_duration
        self.attack_frame = 0
        if not self.attack_playing:
           self.attack_song.play()
           self.attack_playing = True

        self.attack_playing = False

    def render(self): 
        self.screen.blit(self.player, (self.posX, self.posY))
        player_width = self.player.get_width()
        player_height = self.player.get_height()
        caixa_width = self.caixa.caixa.get_width()
        caixa_height = self.caixa.caixa.get_height()
        player_rect = pygame.Rect(self.posX, self.posY, player_width, player_height)
        caixa_rect = pygame.Rect(self.caixa.vecX, self.caixa.vecY, caixa_width + 120, caixa_height + 100)
        barril_rect = pygame.Rect(self.barril.VecX, self.barril.VecY, self.barril.barril.get_width() + 120, self.barril.barril.get_height()+ 100)

        if self.is_attacking:
            if self.attack_frame < len(self.attack_imgs):
                self.screen.blit(self.attack_imgs[self.attack_frame], (self.posX - 60, self.posY - 50))
                self.attack_frame += 1 
                if player_rect.colliderect(caixa_rect):
                    self.caixa.life -= 1
                elif player_rect.colliderect(barril_rect):
                    self.barril.life -= 1  
            else:
                self.is_attacking = False

    def mov(self): 
        keys = pygame.key.get_pressed()
        moved = False
        dx, dy = 0, 0
        pilar_width = self.pilar.pilar.get_width()
        player_width = self.player.get_width()
        
        pilar_rect = pygame.Rect(self.pilar.posX, self.pilar.posY, pilar_width, self.pilar.pilar.get_height())
        player_rect = pygame.Rect(self.posX, self.posY, player_width, self.player.get_height())
        
        if keys[pygame.K_a]:
            self.player = pygame.image.load('./Texture/player esquerda.png')
            self.player = pygame.transform.scale(self.player, (self.VecX, self.VecY))
            if self.posX > 10:
                dx -= self.velocity
            moved = True
            
        if keys[pygame.K_d]:
            self.player = pygame.image.load('./Texture/player direita.png')
            self.player = pygame.transform.scale(self.player, (self.VecX, self.VecY))
            if self.posX < 980:
                dx += self.velocity
            moved = True
            
        if keys[pygame.K_w]:
            self.player = pygame.image.load('./Texture/player cima.png')
            self.player = pygame.transform.scale(self.player, (self.VecX, self.VecY))
            if self.posY > 10: 
                dy -= self.velocity
            moved = True
            
        if keys[pygame.K_s]:
            self.player = pygame.image.load('./Texture/player frente.png')
            self.player = pygame.transform.scale(self.player, (self.VecX, self.VecY))
            if self.posY < 550:
                dy += self.velocity
            moved = True
            
        # Mover e verificar colisões separadamente em cada eixo
        self.posX += dx
        player_rect.x = self.posX
        if player_rect.colliderect(pilar_rect):
            self.posX -= dx

        self.posY += dy
        player_rect.y = self.posY
        if player_rect.colliderect(pilar_rect):
            self.posY -= dy

        if moved:
            if not self.sound_playing:
                self.sound_move.play(loops=-1)
                self.sound_playing = True
        else:
            self.sound_move.stop()
            self.sound_playing = False
