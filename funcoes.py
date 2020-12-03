import pygame
import time

def cjBaldes():
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
    return lista

def cadastro(nome,email):
    arquivo = open("cadastroJogo.txt", "a")
    texto = ("Nome do jogador -> "+nome+", E-mail -> "+email)
    arquivo.write(texto+"\n")
    arquivo.close()
    pygame.init()

def varGeral():
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
    return(baldeLargura, baldeAltura, baldePosicaoX, baldePosicaoY, baldeMovimento, cascaoLargura, cascaoAltura, cascaoPosicaoX, cascaoPosicaoY, cascaoMovimento, velocidadeCascao, velocidadeBalde)

def tratamentoImagens():
    largura = 900
    altura = 700
    display = pygame.display.set_mode( (largura, altura))
    backgroud = pygame.image.load("assets/cascaoFundo.jpg")#imagem de fundo
    pedeNome = pygame.image.load("assets/pedeNome.jpg")# tela de fundo para pedir o nome
    cascaoCorre = pygame.image.load("assets/corre.png")#colocando o cascão para correr
    molhouEnd = pygame.image.load("assets/molhou.jpg")#mensagem de fim
    intro = pygame.image.load("assets/intro.jpg")#mensagem de boas vindas
    return(display, backgroud, pedeNome, cascaoCorre, molhouEnd, intro, altura, largura)

def configuracoesSom():
    pygame.mixer.music.load("assets/audio.mp3") #musica de fundo
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.1)
    banhoSound = pygame.mixer.Sound("assets/banho.wav")#som do banho no cascão
    banhoSound.set_volume(0.2)
    return banhoSound

