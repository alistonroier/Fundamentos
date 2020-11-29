import pygame
import random
import time

pygame.init()

pygame.display.set_caption("Corre Cascão")

icon = pygame.image.load("assets/ico.png")
pygame.display.set_icon(icon)


relogio = pygame.time.Clock()
largura = 900
altura = 700
display = pygame.display.set_mode( (largura, altura))
backgroud = pygame.image.load("assets/cascaoFundo.jpg")#imagem de fundo
cascaoCorre = pygame.image.load("assets/corre.png")#colocando o cascão para correr
molhouEnd = pygame.image.load("assets/molhou.jpg")#mensagem de fim

balde = pygame.image.load("assets/ba.png")# balde para molha o cascao
baldeLargura = 81
baldeAltura = 120
baldePosicaoX = 250
baldePosicaoY = 10 - baldeAltura # = 110
baldeMovimento = 0

cascaoLargura = 82
cascaoAltura = 108
cascaoPosicaoX = 320
cascaoPosicaoY = 550
cascaoMovimento = 0

velocidadeCascao = 5
velocidadeBalde = 5

pygame.mixer.music.load("assets/audio.mp3") #musica de fundo
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.05)

banhoSound = pygame.mixer.Sound("assets/banho.wav")#som do bnaho
banhoSound.set_volume(0.08)


def contaPlacar(contador):
    font = pygame.font.SysFont(None, 25)
    texto = font.render("Desvios: "+str(contador), True, (255,255,255))
    display.blit(texto, (40,10))

def molhou():
    display.blit(molhouEnd, (140,160))
    pygame.display.update()
    pygame.mixer.Sound.play(banhoSound)
    pygame.mixer.music.stop()
    time.sleep(5)



contador = 0
while True:

    #trabalhar com background
    display.fill((255,255,255))
    display.blit(backgroud, (largura - 1254,(altura - 708)))

    font = pygame.font.SysFont(None, 100)#buscar como alterar fonte

    #devolve uma lista de evento []
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                cascaoMovimento = - velocidadeCascao
            elif evento.key == pygame.K_RIGHT:
                cascaoMovimento = velocidadeCascao
        if evento.type == pygame.KEYUP:
            cascaoMovimento = 0
    
    cascaoPosicaoX = cascaoPosicaoX + cascaoMovimento
    if cascaoPosicaoX < 27:
        cascaoPosicaoX = 27
    elif cascaoPosicaoX > 620:
        cascaoPosicaoX = 620


    display.blit(cascaoCorre, (cascaoPosicaoX,cascaoPosicaoY))  

    baldePosicaoY = baldePosicaoY + velocidadeBalde
    contaPlacar(contador) # controla a quantidade de vezes que o cascão desvio do balde de água
    if baldePosicaoY > altura:
        baldePosicaoY = 10 - baldeAltura
        velocidadeBalde = velocidadeBalde + 1
        baldePosicaoX = random.randrange(40,550)
        contador += 1


    display.blit(balde, (baldePosicaoX, baldePosicaoY)) 

    #Verificando banho
    if cascaoPosicaoY < baldePosicaoY + (baldeAltura - 30 ):
        if cascaoPosicaoX < baldePosicaoX and cascaoPosicaoX + cascaoLargura > baldePosicaoX or baldePosicaoX + (baldeLargura - 30) > cascaoPosicaoX and baldePosicaoX + baldeLargura < cascaoPosicaoX + baldeLargura:
            molhou()
            velocidadeBalde = 5
            baldePosicaoY = 0 - baldeAltura
            contador = 0

    pygame.display.update()
    relogio.tick(60)

print("Volte Sempre!!!!")