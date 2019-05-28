# -*- coding: utf-8 -*-

# Importando as bibliotecas necessÃ¡rias.
import pygame
import random
import time
from os import path

# Estabelece a pasta que contem as figuras e sons.
img_dir = path.join(path.dirname(__file__), 'Imagens')
snd_dir = path.join(path.dirname(__file__), 'Sons')

# Dados gerais do jogo.
WIDTH = 1000 # Largura da tela
HEIGHT = 700 # Altura da tela
FPS = 60 # Frames por segundo

# Define algumas variÃ¡veis com as cores bÃ¡sicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Estados para controle do fluxo da aplicaÃ§Ã£o
INIT = 0
GAME = 1
QUIT = 2
FIM = 4


# Classe Jogador que representa a nave
class Player(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self,player_img):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        
        self.images = player_img
        self.currentimg = 0
        self.image = pygame.transform.scale(self.images[self.currentimg], (60, 103))
        
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        

        
        # Centraliza embaixo da tela.
        self.rect.centerx = WIDTH - 800
        self.rect.bottom = HEIGHT - 300 
        
        # Velocidade da nave
        self.speedx = 0
        self.speedy= 0
        
        # Melhora a colisÃ£o estabelecendo um raio de um circulo
        self.radius = 25
        
        # Guarda o tick da primeira imagem
        self.last_update = pygame.time.get_ticks()

        # Controle de ticks de animaÃ§Ã£o: troca de imagem a cada self.frame_ticks milissegundos.
        self.frame_ticks = 75
    
    # Metodo que atualiza a posiÃ§Ã£o da navinha
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
#Mantem dentro da tela
        if self.rect.right >= WIDTH:
            self.rect.right = 60

        if self.rect.left <= 0:
            self.rect.left = 0
            
            
        if self.rect.bottom <= 137:
            self.speedy = 10
        if self.rect.bottom >= 635:
            self.rect.bottom = 635
        if self.rect.bottom <= 500:
            self.speedy = 10
            
        now = pygame.time.get_ticks()

        # Verifica quantos ticks se passaram desde a ultima mudanÃ§a de frame.
        elapsed_ticks = now - self.last_update

        # Se jÃ¡ estÃ¡ na hora de mudar de imagem...
        if elapsed_ticks > self.frame_ticks:

            # Marca o tick da nova imagem.
            self.last_update = now

            # AvanÃ§a um quadro.
            self.currentimg += 1

            # Verifica se jÃ¡ chegou no final da animaÃ§Ã£o.
            if self.currentimg == len(self.images):
                # Se sim, tchau explosÃ£o!
                self.currentimg=0
            self.image = self.images[self.currentimg]


                    
# Classe Mob que representa os meteoros
class HOLE(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self, hole_img):
        
        x = random.randint(450,1000)
        y = 710
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Diminuindo o tamanho da imagem.
        self.image = pygame.transform.scale(hole_img, (70, 80))
        
#        # Deixando transparente.
#        self.image.set_colorkey(BLACK)
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Sorteia um lugar inicial em x
        self.rect.centerx = x
        # Sorteia um lugar inicial em y
        self.rect.bottom = y
        # Sorteia uma velocidade inicial
        self.speedx = 0
        self.speedy = 0
        
        # Melhora a colisÃ£o estabelecendo um raio de um circulo
        self.radius = int(self.rect.width * .85 / 2)
        
    # Metodo que atualiza a posiÃ§Ã£o do meteoro
    def update(self):
        
        pass


class UNIC(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self, uni_anim):
        
        x =  1000
        y = random.randint(635 - 160,635 - 110) 
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        self.images = uni_anim
        self.currentimg = 0
        self.image = pygame.transform.scale(self.images[self.currentimg], (50 , 70))
        
#        # Deixando transparente.
#        self.image.set_colorkey(BLACK)
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Sorteia um lugar inicial em x
        self.rect.centerx = x
        # Sorteia um lugar inicial em y
        self.rect.bottom = y
        # Sorteia uma velocidade inicial
        self.speedx = -5
        self.speedy = 0
        
        # Melhora a colisÃ£o estabelecendo um raio de um circulo
        self.radius = int(self.rect.width * .65 / 2)
    
        # Guarda o tick da primeira imagem
        self.last_update = pygame.time.get_ticks()

        # Controle de ticks de animaÃ§Ã£o: troca de imagem a cada self.frame_ticks milissegundos.
        self.frame_ticks = 75
        
    # Metodo que atualiza a posio do meteoro
    def update(self):
        
        if self.rect.left <= 0:
            self.rect.right = WIDTH
        else:
            self.rect.x += self.speedx
            self.rect.y += self.speedy
            
        now = pygame.time.get_ticks()

        # Verifica quantos ticks se passaram desde a ultima mudanÃ§a de frame.
        elapsed_ticks = now - self.last_update

        # Se jÃ¡ estÃ¡ na hora de mudar de imagem...
        if elapsed_ticks > self.frame_ticks:

            # Marca o tick da nova imagem.
            self.last_update = now

            # AvanÃ§a um quadro.
            self.currentimg += 1

            # Verifica se jÃ¡ chegou no final da animaÃ§Ã£o.
            if self.currentimg == len(self.images):
                # Se sim, tchau explosÃ£o!
                self.currentimg=0
            self.image = self.images[self.currentimg]





class LIVES(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self, lives_img,x):

        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Diminuindo o tamanho da imagem.
        self.image = pygame.transform.scale(lives_img, (35, 40))
       
        
#        # Deixando transparente.
        self.image.set_colorkey(BLACK)
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect() 
        
        # Sorteia um lugar inicial em x
        self.rect.left = x
        # Sorteia um lugar inicial em y
        self.rect.bottom = 635 +40  

        # Sorteia uma velocidade inicial
        self.speedx = 0
        self.speedy = 0
        
        # Melhora a colisÃ£o estabelecendo um raio de um circulo
        self.radius = int(self.rect.width * .85 / 2)
        
    # Metodo que atualiza a posiÃ§Ã£o do meteoro
    def update(self):        
        # Se o tiro passar do inicio da tela, morre.
#        if self.rect.bottom < 0:
            #self.kill()
        pass
    
    
    

class BARRIL(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self, bar_anim):
        
        x =  1000
        y =  670
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        self.images = bar_anim
        self.currentimg = 0
        self.image = pygame.transform.scale(self.images[self.currentimg], (40, 80))
        self.image.set_colorkey(BLACK)
##        # Deixando transparente.
#        self.image.set_colorkey(BLACK)
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Sorteia um lugar inicial em x
        self.rect.centerx = x
        # Sorteia um lugar inicial em y
        self.rect.bottom = y
        # Sorteia uma velocidade inicial
        self.speedx = -3
        self.speedy = 0
                                     
        # Melhora a colisão estabelecendo um raio de um circulo
        self.radius = int(self.rect.width * .85 / 2)
    
        # Guarda o tick da primeira imagem
        self.last_update = pygame.time.get_ticks()


        # Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos.
        self.frame_ticks = 75
        
    # Metodo que atualiza a posição do meteoro
    def update(self):
        
        if self.rect.left <= 0:
            self.rect.right = WIDTH
        else:
            self.rect.x += self.speedx
            self.rect.y += self.speedy
            
        now = pygame.time.get_ticks()

        # Verifica quantos ticks se passaram desde a ultima mudança de frame.
        elapsed_ticks = now - self.last_update
        self.image.set_colorkey(BLACK)

        # Se já está na hora de mudar de imagem...
        if elapsed_ticks > self.frame_ticks:

            # Marca o tick da nova imagem.
            self.last_update = now

            # Avança um quadro.
            self.currentimg += 1

            # Verifica se já chegou no final da animação.
            if self.currentimg == len(self.images):
                # Se sim, tchau explosão!
                self.currentimg=0
            self.image = self.images[self.currentimg]

    
class Back(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self,back_img):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        
        self.images = back_img
        self.currentimg = 0
        self.image = pygame.transform.scale(self.images[self.currentimg], (1000, 700))
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()

        
        # Guarda o tick da primeira imagem
        self.last_update = pygame.time.get_ticks()

        # Controle de ticks de animaÃ§Ã£o: troca de imagem a cada self.frame_ticks milissegundos.
        self.frame_ticks = 350
    
    # Metodo que atualiza a posiÃ§Ã£o da navinha
    def update(self):
        
        now = pygame.time.get_ticks()

        # Verifica quantos ticks se passaram desde a ultima mudanÃ§a de frame.
        elapsed_ticks = now - self.last_update

        # Se jÃ¡ estÃ¡ na hora de mudar de imagem...
        if elapsed_ticks > self.frame_ticks:
 
            # Marca o tick da nova imagem.
            self.last_update = now

            # AvanÃ§a um quadro.
            self.currentimg += 1
            # Verifica se jÃ¡ chegou no final da animaÃ§Ã£o.
            if self.currentimg == len(self.images):
                # Se sim, tchau explosÃ£o!
                self.currentimg=0
            self.image = self.images[self.currentimg]



# Carrega todos os assets uma vez sÃ³.
def load_assets(img_dir):
    assets = {}
    assets["game_over"] = pygame.image.load(path.join(img_dir, "game_over.png")).convert()
    assets["hole_img"] = pygame.image.load(path.join(img_dir, "buraco.png")).convert()
    assets["lives_img"] = pygame.image.load(path.join(img_dir, "coracao.png")).convert()
    assets ["background_init"] = pygame.image.load(path.join(img_dir, 'imagem 1.jpeg')).convert()
    assets["background"] = pygame.image.load(path.join(img_dir, 'imagem de fundo_ 1.jpg')).convert()
    assets["background2"] = pygame.image.load(path.join(img_dir, 'imagem de fundo_ 2.png')).convert()
    assets["background3"] = pygame.image.load(path.join(img_dir, 'imagem de fundo_3.jpg')).convert()
    assets["musica_fim"] = pygame.mixer.Sound(path.join(snd_dir, 'Game Over Sound Effects High Quality-[AudioTrimmer.com].ogg'))
    assets["pulando"] = pygame.mixer.Sound(path.join(snd_dir, 'Mario Jump - Gaming Sound Effect (HD)-[AudioTrimmer.com].ogg'))
    assets["unicornio"] = pygame.mixer.Sound(path.join(snd_dir, 'Unicorn Puking Sound effect COPYRIGHT FREE-[AudioTrimmer.com]-[AudioTrimmer.com].ogg'))
    
    bar_anim=[]
    for i in range(4):
        filename ='barril_{}.png'.format(i)
        img3 = pygame.image.load(path.join(img_dir,filename)).convert()
        img3 = pygame.transform.scale(img3, (50, 45))
        bar_anim.append(img3)
    assets["bar_anim"]=bar_anim
    
    uni_anim = []
    for i in range (10):
        filename = 'uni_{}.png'.format(i)
        img2 = pygame.image.load(path.join(img_dir,filename)).convert()
        img2 = pygame.transform.scale(img2, (80, 70))
        uni_anim.append(img2)
    assets["uni_anim"]=uni_anim
    
    back_anim = []
    for i in range (2):
        filename = 'imagem {}.jpeg'.format(i)
        img1 = pygame.image.load(path.join(img_dir,filename)).convert()
        img1 = pygame.transform.scale(img1, (1000, 700))
        back_anim.append(img1)
    assets["back_anim"]=back_anim
        
    boneco_anim = []
    for i in range(5):
        filename = 'boneco_{}.png'.format(i)
        img0 = pygame.image.load(path.join(img_dir, filename)).convert()
        img0 = pygame.transform.scale(img0, (60, 103))        
        img0.set_colorkey(BLACK)
        boneco_anim.append(img0)
    assets["boneco_anim"] = boneco_anim
#    assets["score_font"] = pygame.font.Font(path.join(fnt_dir, "PressStart2P.ttf"), 28)
    return assets

def init_screen(screen):
    # Carrega todos os assets uma vez sÃ³ e guarda em um dicionÃ¡rio
    assets = load_assets(img_dir)
    # VariÃ¡vel para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo da tela inicial
    background_init = Back(assets["back_anim"])
    
    all_sprites = pygame.sprite.Group()
    all_sprites.add(background_init)
        
    running = True
    while running:
        
        # Ajusta a velocidade do jogo.
        clock.tick(FPS)
        
        # Processa os eventos (mouse, teclado, botÃ£o, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                running = False

            if event.type == pygame.KEYUP:
                state = GAME
                running = False
        all_sprites.update()
        # A cada loop, redesenha o fundo e os sprites
        all_sprites.draw(screen)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state


def end_game(screen):
    assets= load_assets(img_dir)
    background = assets["game_over"]
    background_rect = background.get_rect() 
    running = True
    while running:
        for event in pygame.event.get():
                        # Verifica se apertou alguma tecla.
            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                        # Dependendo da tecla, altera a velocidade.
                if event.key == pygame.K_y:
                    pygame.mixer.music.set_volume(0) 
                    state = GAME
                    running = False
                
                if event.key == pygame.K_n:
                    state = QUIT
                    running = False
        screen.fill(BLACK)
        screen.blit(background, background_rect)
        pygame.display.flip()
    return state
                
def game_screen(screen):
    # Carrega todos os assets uma vez sÃ³ e guarda em um dicionÃ¡rio
    assets = load_assets(img_dir)

    # VariÃ¡vel para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo do jogo
    background = assets["background"]
    background_rect = background.get_rect() 
 
    pygame.mixer.music.load(path.join(snd_dir, 'LightingGrass+Wind EffectSound Test-[AudioTrimmer.com].ogg'))
    pygame.mixer.music.set_volume(0.4)
    
  # Cria uma nave. O construtor serÃ¡ chamado automaticamente.
    player = Player(assets["boneco_anim"])

#    # Carrega a fonte para desenhar o score.
#    score_font = assets["score_font"]

    # Cria um grupo de todos os sprites e adiciona a nave.
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    # Cria um grupo dos meteoros

    mobs1 = pygame.sprite.Group()
    mobs2 = pygame.sprite.Group()
    mobs3 = pygame.sprite.Group()
    life = pygame.sprite.Group()


    # Cria 2 meteoros e adiciona no grupo meteoros

    m = HOLE(assets["hole_img"])
    all_sprites.add(m)
    mobs1.add(m)
        
    u = UNIC(assets["uni_anim"])
    all_sprites.add(u)
    mobs2.add(u)

    
    b = BARRIL(assets["bar_anim"])
    all_sprites.add(b)
    mobs3.add(b)

    lives = 3
    PLAYING =  0
    DONE = 2
    x = 00
    contador = 1
    pygame.mixer.music.play(loops=-1)
    
    for i in  range(lives):
            
            l = LIVES(assets["lives_img"],x)
            life.add(l)
            x+=40
                           
    state = PLAYING
    while state != DONE:
    # Ajusta a velocidade do jogo.
        clock.tick(FPS)
        if state == PLAYING:
            # Processa os eventos (mouse, teclado, botÃ£o, etc).
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    state = DONE
                
                # Verifica se apertou alguma tecla.
                if event.type == pygame.KEYDOWN:
                    # Dependendo da tecla, altera a velocidade.
                    if event.key == pygame.K_LEFT:
                        player.speedx = -8
                    if event.key == pygame.K_RIGHT:
                        player.speedx = 9
#                     Se for um espaÃ§o atira!
                    if event.key == pygame.K_SPACE:
                        player.speedy =-30
                        assets["pulando"].play()

                        
                # Verifica se soltou alguma tecla.
                if event.type == pygame.KEYUP:
                    # Dependendo da tecla, altera a velocidade.
                    if event.key == pygame.K_LEFT:
                        player.speedx = 0
                    if event.key == pygame.K_RIGHT:
                        player.speedx = 0
                    if event.key == pygame.K_SPACE:
                        player.speedy =50
                    
        # Depois de processar os eventos.
        # Atualiza a acao de cada sprite.
        all_sprites.update()
        
        if state == PLAYING:
#                  
            # Verifica se houve colisÃ£o entre nave e meteoro
            if player.rect.left >= 930:
                x = lives*40
                lives += 1
                l = LIVES(assets["lives_img"],x)
                life.add(l)
                life.draw(screen)
                b.rect.left = 1000 
                u.rect.left = 1000
                
                contador +=1
                if contador % 3 == 1:
                    background = assets["background"]
                    background_rect = background.get_rect() 
                            
                elif contador % 3 == 2:
                    background = assets["background2"]
                    background_rect = background.get_rect()
                
                elif contador % 3 == 0:
                    background = assets["background3"]
                    background_rect = background.get_rect()
                
            for e in [mobs1, mobs2, mobs3]:
                hits = pygame.sprite.spritecollide(player, e, True)
                if hits:

                    player.rect.left = 100 
                    lives -=1 
                    life.empty()
                    if e ==  mobs1:
                        m = HOLE(assets["hole_img"])
                        all_sprites.add(m)
                        mobs1.add(m)
                    if e ==  mobs2:
                        assets["unicornio"].play()
                        u = UNIC(assets["uni_anim"])
                        all_sprites.add(u)
                        mobs2.add(u)
                    if e ==  mobs3:  
                        b = BARRIL(assets["bar_anim"])
                        all_sprites.add(b)
                        mobs3.add(b)                        
                    a = 0
                    for i in  range(lives):
                         l = LIVES(assets["lives_img"],a)
                         life.add(l)
                         
                         a+=40
                    life.draw(screen)
                
                

            if lives <= 0:
                player.kill()
                pygame.mixer.music.stop()
                assets["musica_fim"].play()
                return FIM
                    
              
                
        # A cada loop, redesenha o fundo e os sprites
            screen.fill(BLACK)
            screen.blit(background, background_rect)
            all_sprites.draw(screen)
            life.draw(screen)
    
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
    return QUIT

# InicializaÃ§Ã£o do Pygame.
pygame.init()
pygame.mixer.init()

# Tamanho da tela.
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Nome do jogo
pygame.display.set_caption("Pitfall")

# Comando para evitar travamentos.
try:
    state = INIT
    while state != QUIT:
        if state == INIT:
            state = init_screen(screen)
        elif state == GAME:
            state = game_screen(screen)
        elif state == FIM:
            state = end_game(screen)
        else:
            state = QUIT
finally:
    pygame.quit()