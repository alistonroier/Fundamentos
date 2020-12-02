import pygame
import random
import time
import os

pygame.init()

pygame.display.set_caption("Corre Cascão")
icon = pygame.image.load("assets/ico.png")
pygame.display.set_icon(icon)


relogio = pygame.time.Clock()
largura = 900
altura = 700

display = pygame.display.set_mode( (largura, altura))
backgroud = pygame.image.load("assets/cascaoFundo.jpg")#imagem de fundo
pedeNome = pygame.image.load("assets/pedeNome.jpg")# tela de fundo para pedir o nome
cascaoCorre = pygame.image.load("assets/corre.png")#colocando o cascão para correr
molhouEnd = pygame.image.load("assets/molhou.jpg")#mensagem de fim
intro = pygame.image.load("assets/intro.jpg")#mensagem de boas vindas

ba = pygame.image.load("assets/ba.png")# balde para molha o cascao
bb = pygame.image.load("assets/bb.png")
bc = pygame.image.load("assets/bc.png")
bd = pygame.image.load("assets/bd.png")
be = pygame.image.load("assets/be.png")
bf = pygame.image.load("assets/bf.png")
bg = pygame.image.load("assets/bg.png")
bh = pygame.image.load("assets/bh.png")
bi = pygame.image.load("assets/bi.png")
bj = pygame.image.load("assets/bj.png")
bk = pygame.image.load("assets/bk.png")
bl = pygame.image.load("assets/bl.png")
bm = pygame.image.load("assets/bm.png")
bn = pygame.image.load("assets/bn.png")
bo = pygame.image.load("assets/bo.png")
bp = pygame.image.load("assets/bp.png")
bq = pygame.image.load("assets/bq.png")
br = pygame.image.load("assets/br.png")
bs = pygame.image.load("assets/bs.png")
bt = pygame.image.load("assets/bt.png")
bu = pygame.image.load("assets/bu.png")
bv = pygame.image.load("assets/bv.png")
by = pygame.image.load("assets/by.png")
bw = pygame.image.load("assets/bw.png")
bx = pygame.image.load("assets/bx.png")


lista = [ba,bb,bc,bd,be,bf,bg,bh,bi,bj,bk,bl,bm,bn,bo,bp,bq,br,bs,bt,bu,bv,bw,by,bx]
escolhido = random.choice(lista)

baldeLargura = 81
baldeAltura = 120
baldePosicaoX = 250
baldePosicaoY = 10 - baldeAltura # = 110
baldeMovimento = 0

cascaoLargura = 82
cascaoAltura = 108
cascaoPosicaoX = 320
cascaoPosicaoY = 580
cascaoMovimento = 0

velocidadeCascao = 5
velocidadeBalde = 5




def contaPlacar(contador):
    font = pygame.font.SysFont(None, 25)
    texto = font.render("Desvios: "+str(contador), True, (255,255,255))
    display.blit(texto, (40,10))

def molhou():
    display.blit(molhouEnd, (140,160))
    pygame.display.update()
    pygame.mixer.Sound.play(banhoSound)
    #pygame.mixer.music.stop()
    time.sleep(5)


contador = -1

nome = input("\nInforme o seu nome: ")
email = input("\nInforme seu e-mail: ")

arquivo = open("cadastroJogo.txt", "a")
texto = ("Nome do jogador -> "+nome+", E-mail -> "+email)
arquivo.write(texto+"\n")
arquivo.close()


pygame.mixer.music.load("assets/audio.mp3") #musica de fundo
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)

banhoSound = pygame.mixer.Sound("assets/banho.wav")#som do banho
banhoSound.set_volume(0.2)

while True:

    if contador == -1: #para apresentar a intro antes do jogo
        display.blit(intro, (-350,0))
        pygame.display.update()
        relogio.tick(60)
        time.sleep(10) #tempo para ler a intro 
        contador = contador + 1 #para não repetir a intro dentro do jogo
    else:
        pass


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
        escolhido = random.choice(lista)


    display.blit(escolhido, (baldePosicaoX, baldePosicaoY))


    #Verificando banho
    if (cascaoPosicaoY + 30) < baldePosicaoY + baldeAltura:
        if cascaoPosicaoX < baldePosicaoX and cascaoPosicaoX + cascaoLargura > baldePosicaoX or baldePosicaoX + (baldeLargura - 30) > cascaoPosicaoX and baldePosicaoX + baldeLargura < cascaoPosicaoX + baldeLargura:
            molhou()
            velocidadeBalde = 5
            baldePosicaoY = 0 - baldeAltura
            contador = 0

    pygame.display.update()
    relogio.tick(60)

print("Volte Sempre!!!!")