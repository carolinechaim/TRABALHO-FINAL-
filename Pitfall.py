# -*- coding: utf-8 -*-

# Importando as bibliotecas necessárias.
import pygame
import random
import time
from os import path

# Estabelece a pasta que contem as figuras e sons.
img_dir = path.join(path.dirname(__file__), 'Imagens')
#snd_dir = path.join(path.dirname(__file__), 'snd')
#fnt_dir = path.join(path.dirname(__file__), 'font')

# Dados gerais do jogo.
WIDTH = 1000 # Largura da tela
HEIGHT = 700 # Altura da tela
FPS = 60 # Frames por segundo

# Define algumas variáveis com as cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Estados para controle do fluxo da aplicação
INIT = 0
GAME = 1
QUIT = 2

# Classe Jogador que representa a nave
class Player(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self,player_img):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        self.image =pygame.transform.scale(player_img, (60, 103))
        
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        self.image.set_colorkey(BLACK)
        
        # Centraliza embaixo da tela.
        self.rect.centerx = WIDTH - 800
        self.rect.bottom = HEIGHT - 300 
        
        # Velocidade da nave
        self.speedx = 0
        self.speedy= 0
        
        # Melhora a colisão estabelecendo um raio de um circulo
        self.radius = 25
    
    # Metodo que atualiza a posição da navinha
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
        # Mantem dentro da tela
        if self.rect.right >= WIDTH:
            self.rect.right = WIDTH
        if self.rect.left <= 0:
            self.rect.left = 0
            
            
            
        if self.rect.bottom <= 137:
            self.speedy = 10
        if self.rect.bottom >= 635:
            self.rect.bottom = 635
        if self.rect.bottom <= 500:
            self.speedy = 10
                    
# Classe Mob que representa os meteoros
class HOLE(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self, hole_img):
        
        x = random.randint(500,1000)
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
        
        # Melhora a colisão estabelecendo um raio de um circulo
        self.radius = int(self.rect.width * .85 / 2)
        
    # Metodo que atualiza a posição do meteoro
    def update(self):
        
        pass
            
## Classe Bullet que representa os tiros
#class Bullet(pygame.sprite.Sprite):
#    
#    # Construtor da classe.
#    def __init__(self, x, y, bullet_img):
#        
#        # Construtor da classe pai (Sprite).
#        pygame.sprite.Sprite.__init__(self)
#        
#        # Carregando a imagem de fundo.
#        self.image = bullet_img
#        
#        # Deixando transparente.
#        self.image.set_colorkey(BLACK)
#        
#        # Detalhes sobre o posicionamento.
#        self.rect = self.image.get_rect()
#        
#        # Coloca no lugar inicial definido em x, y do constutor
#        self.rect.bottom = y
#        self.rect.centerx = x
#        self.speedy = -10
#
#    # Metodo que atualiza a posição da navinha
#    def update(self):
#        self.rect.y += self.speedy
#        
#        # Se o tiro passar do inicio da tela, morre.
#        if self.rect.bottom < 0:
#            self.kill()
#
## Classe que representa uma explosão de meteoro
#class Explosion(pygame.sprite.Sprite):
#
#    # Construtor da classe.
#    def __init__(self, center, explosion_anim):
#        # Construtor da classe pai (Sprite).
#        pygame.sprite.Sprite.__init__(self)
#
#        # Carrega a animação de explosão
#        self.explosion_anim = explosion_anim
#
#        # Inicia o processo de animação colocando a primeira imagem na tela.
#        self.frame = 0
#        self.image = self.explosion_anim[self.frame]
#        self.rect = self.image.get_rect()
#        self.rect.center = center
#
#        # Guarda o tick da primeira imagem
#        self.last_update = pygame.time.get_ticks()
#
#        # Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos.
#        self.frame_ticks = 50
#
#    def update(self):
#        # Verifica o tick atual.
#        now = pygame.time.get_ticks()
#
#        # Verifica quantos ticks se passaram desde a ultima mudança de frame.
#        elapsed_ticks = now - self.last_update
#
#        # Se já está na hora de mudar de imagem...
#        if elapsed_ticks > self.frame_ticks:
#
#            # Marca o tick da nova imagem.
#            self.last_update = now
#
#            # Avança um quadro.
#            self.frame += 1
#
#            # Verifica se já chegou no final da animação.
#            if self.frame == len(self.explosion_anim):
#                # Se sim, tchau explosão!
#                self.kill()
#            else:
#                # Se ainda não chegou ao fim da explosão, troca de imagem.
#                center = self.rect.center
#                self.image = self.explosion_anim[self.frame]
#                self.rect = self.image.get_rect()
#                self.rect.center = center

# Carrega todos os assets uma vez só.
def load_assets(img_dir):
    assets = {}
    assets["player_img"] = pygame.image.load(path.join(img_dir, "boneco pulando.png")).convert()
    assets["game_over"] = pygame.image.load(path.join(img_dir, "game_over.png")).convert()
    assets["hole_img"] = pygame.image.load(path.join(img_dir, "buraco.png")).convert()
    assets ["background_init"] = pygame.image.load(path.join(img_dir, 'inicio.png')).convert()
#    assets["bullet_img"] = pygame.image.load(path.join(img_dir, "laserRed16.png")).convert()
    assets["background"] = pygame.image.load(path.join(img_dir, 'imagem de fundo_ 1.jpg')).convert()
#    assets["boom_sound"] = pygame.mixer.Sound(path.join(snd_dir, 'expl3.wav'))
#    assets["destroy_sound"] = pygame.mixer.Sound(path.join(snd_dir, 'expl6.wav'))
#    assets["pew_sound"] = pygame.mixer.Sound(path.join(snd_dir, 'pew.wav'))
#    explosion_anim = []
#    for i in range(15):
#        filename = 'frame_{}.png'.format(i)
#        img = pygame.image.load(path.join(img_dir, filename)).convert()
#        img = pygame.transform.scale(img, (60, 103))        
#        img.set_colorkey(BLACK)
#        explosion_anim.append(img)
#    assets["explosion_anim"] = explosion_anim
#    assets["score_font"] = pygame.font.Font(path.join(fnt_dir, "PressStart2P.ttf"), 28)
    return assets

def init_screen(screen):
    # Carrega todos os assets uma vez só e guarda em um dicionário
    assets = load_assets(img_dir)
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo da tela inicial
    background_init = assets["background_init"]
    background_rect = background_init.get_rect()
        
#        def __init__(self,player_img):
#        
#        # Construtor da classe pai (Sprite).
#        pygame.sprite.Sprite.__init__(self)
#        
#        self.image =pygame.transform.scale(player_img, (60, 103))
#        
#        
#        # Detalhes sobre o posicionamento.
#        self.rect = self.image.get_rect()
#        
#        self.image.set_colorkey(BLACK)
#        
#        # Centraliza embaixo da tela.
#        self.rect.centerx = WIDTH - 800
#        self.rect.bottom = HEIGHT - 300 
#        
#        # Velocidade da nave
#        self.speedx = 0
#        self.speedy= 0
#        
#        # Melhora a colisão estabelecendo um raio de um circulo
#        self.radius = 25

    running = True
    while running:
        
        # Ajusta a velocidade do jogo.
        clock.tick(FPS)
        
        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                running = False

            if event.type == pygame.KEYUP:
                state = GAME
                running = False
                    
        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(background_init, background_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state

def game_screen(screen):
    # Carrega todos os assets uma vez só e guarda em um dicionário
    assets = load_assets(img_dir)

    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo do jogo
    background = assets["background"]
    background_rect = background.get_rect()
    
#    # Carrega os sons do jogo
#    pygame.mixer.music.load(path.join(snd_dir, 'tgfcoder-FrozenJam-SeamlessLoop.ogg'))
#    pygame.mixer.music.set_volume(0.4)
#    boom_sound = assets["boom_sound"]
#    destroy_sound = assets["destroy_sound"]
#    pew_sound = assets["pew_sound"]

    # Cria uma nave. O construtor será chamado automaticamente.
    player = Player(assets["player_img"])

#    # Carrega a fonte para desenhar o score.
#    score_font = assets["score_font"]

    # Cria um grupo de todos os sprites e adiciona a nave.
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    # Cria um grupo só dos meteoros
    mobs = pygame.sprite.Group()

#    # Cria um grupo para tiros
#    bullets = pygame.sprite.Group()

    # Cria 2 meteoros e adiciona no grupo meteoros
    for i in range(2):
        m = HOLE(assets["hole_img"])
        all_sprites.add(m)
        mobs.add(m)

    # Loop principal.
#    pygame.mixer.music.play(loops=-1)

    score = 0

    lives = 3

    PLAYING = 0
    EXPLODING = 1
    DONE = 2

    state = PLAYING
    while state != DONE:
        
        # Ajusta a velocidade do jogo.
        clock.tick(FPS)
        
        if state == PLAYING:
            # Processa os eventos (mouse, teclado, botão, etc).
            for event in pygame.event.get():
                
                # Verifica se foi fechado.
                if event.type == pygame.QUIT:
                    state = DONE
                
                # Verifica se apertou alguma tecla.
                if event.type == pygame.KEYDOWN:
                    # Dependendo da tecla, altera a velocidade.
                    if event.key == pygame.K_LEFT:
                        player.speedx = -8
                    if event.key == pygame.K_RIGHT:
                        player.speedx = 8
#                     Se for um espaço atira!
                    if event.key == pygame.K_SPACE:
                        player.speedy =-10
                    

                        
                # Verifica se soltou alguma tecla.
                if event.type == pygame.KEYUP:
                    # Dependendo da tecla, altera a velocidade.
                    if event.key == pygame.K_LEFT:
                        player.speedx = 0
                    if event.key == pygame.K_RIGHT:
                        player.speedx = 0
                    if event.key == pygame.K_SPACE:
                        player.speedy = 10
                    
        # Depois de processar os eventos.
        # Atualiza a acao de cada sprite.
        all_sprites.update()
        
        if state == PLAYING:
##            # Verifica se houve colisão entre tiro e meteoro
##            hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
##            for hit in hits: # Pode haver mais de um
##                # O meteoro e destruido e precisa ser recriado
##                destroy_sound.play()
##                m = Mob(assets["mob_img"]) 
##                all_sprites.add(m)
##                mobs.add(m)
##
##                # No lugar do meteoro antigo, adicionar uma explosão.
##                explosao = Explosion(hit.rect.center, assets["explosion_anim"])
##                all_sprites.add(explosao)
##
##                # Ganhou pontos!
#                score += 100
            
            # Verifica se houve colisão entre nave e meteoro
            hits = pygame.sprite.spritecollide(player, mobs, True)
            if hits:
#                # Toca o som da colisão
#                boom_sound.play()
                player.kill()
                background = assets["game_over"]
                background_rect = background.get_rect()
#                lives -= 1
#                explosao = Explosion(player.rect.center, assets["explosion_anim"])
#                all_sprites.add(explosao)
#                state = EXPLODING
#                explosion_tick = pygame.time.get_ticks()
#                explosion_duration = explosao.frame_ticks * len(explosao.explosion_anim) + 400
            
#        if state == EXPLODING:
#            now = pygame.time.get_ticks()
#            if now - explosion_tick > explosion_duration:
#                if lives == 0:
#                    state = DONE
#                else:
#                    state = PLAYING
#                    player = Player(assets["player_img"])
#                    all_sprites.add(player)

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(background, background_rect)
        all_sprites.draw(screen)

#        # Desenha o score
#        text_surface = score_font.render("{:08d}".format(score), True, YELLOW)
#        text_rect = text_surface.get_rect()
#        text_rect.midtop = (WIDTH / 2,  10)
#        screen.blit(text_surface, text_rect)
#
#        # Desenha as vidas
#        text_surface = score_font.render(chr(9829) * lives, True, RED)
#        text_rect = text_surface.get_rect()
#        text_rect.bottomleft = (10, HEIGHT - 10)
#        screen.blit(text_surface, text_rect)
        
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
    return QUIT

# Inicialização do Pygame.
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
        else:
            state = QUIT
finally:
    pygame.quit()
