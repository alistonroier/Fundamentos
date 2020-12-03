import pygame
import random
import time
import os
from funcoes import cjBaldes, cadastro, varGeral, tratamentoImagens, configuracoesSom

DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) #iniciar o jogo maximizado 
pygame.display.set_caption("Corre Cascão")
icon = pygame.image.load("assets/ico.png")
pygame.display.set_icon(icon)
relogio = pygame.time.Clock()
display, backgroud, pedeNome, cascaoCorre, molhouEnd, intro, altura, largura = tratamentoImagens()#função com as imagens
lista = cjBaldes() #função com as imagens dos baldes com o alfabeto
escolhido = random.choice(lista)#escolhendo a imagem do balde com sua respectiva letra

baldeLargura, baldeAltura, baldePosicaoX, baldePosicaoY, baldeMovimento, cascaoLargura, cascaoAltura, cascaoPosicaoX, cascaoPosicaoY, cascaoMovimento, velocidadeCascao, velocidadeBalde = varGeral() # função com os dados das variaveis inic

def contaPlacar(contador):
    font = pygame.font.SysFont(None, 25)
    texto = font.render("Desvios: "+str(contador), True, (255,255,255))
    display.blit(texto, (40,10))

def molhou():
    display.blit(molhouEnd, (140,160))
    pygame.display.update()
    pygame.mixer.Sound.play(banhoSound)
    time.sleep(5)

contador = -1

nome = input("\nInforme o seu nome: ")
email = input("\nInforme seu e-mail: ")
os.system("pause")
cadastro(nome,email)#função log

banhoSound = configuracoesSom() #função com as configurações dos sons

while True:
    if contador == -1: #para apresentar a intro antes do jogo
        display.blit(intro, (-350,0))
        pygame.display.update()
        time.sleep(15) #tempo para ler a intro 
        contador = contador + 1 #para não repetir a intro dentro do jogo
  
    display.fill((255,255,255))
    display.blit(backgroud, (largura - 1254,(altura - 708)))#plano de fundo
 
    for evento in pygame.event.get(): #devolve uma lista de evento []
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
    contaPlacar(contador)# controla a quantidade de vezes que o cascão desvio do balde de água
    if baldePosicaoY > altura:
        baldePosicaoY = 10 - baldeAltura
        velocidadeBalde = velocidadeBalde + 0.5
        baldePosicaoX = random.randrange(40,590)
        contador += 1
        escolhido = random.choice(lista)

    display.blit(escolhido, (baldePosicaoX, baldePosicaoY))#ecolhe um dos baldes da lista para deixar cair no jogo
    
    if (cascaoPosicaoY + 30) < baldePosicaoY + baldeAltura: #Verificando banho
        if cascaoPosicaoX < baldePosicaoX and cascaoPosicaoX + cascaoLargura > baldePosicaoX or baldePosicaoX + (baldeLargura - 30) > cascaoPosicaoX and baldePosicaoX + baldeLargura < cascaoPosicaoX + baldeLargura:
            molhou()
            velocidadeBalde = 5
            baldePosicaoY = 0 - baldeAltura
            contador = 0

    pygame.display.update()
    relogio.tick(60)

print("Volte Sempre!!!!")