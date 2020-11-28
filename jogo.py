import pygame

pygame.init()
relogio = pygame.time.Clock()
largura = 900
altura = 700
display = pygame.display.set_mode( (largura, altura))
backgroud = pygame.image.load("assets/cascao.jpg")#imagem de fundo
card = pygame.image.load("assets/card.jpg")#monica card
ironman = pygame



while True:

    #trabalhar com background
    display.fill((255,255,255))
    display.blit(backgroud, (largura - 1874,(altura - 868)))
    display.blit(card, (100,300))
    display.blit(card, (233,300))
    display.blit(card, (366,300))
    display.blit(card, (100,500))
    display.blit(card, (233,500))
    display.blit(card, (366,500))

    font = pygame.font.SysFont(None, 100)#buscar como alterar fonte
    texto = font.render("   CAÇA MATEMÁTICO", True, (255, 255, 255))
    texto1 = font.render("DA TURMA DA MÔNICA", True, (255,255,255))
    display.blit(texto, (10, 10))
    display.blit(texto1, (10, 90))

    #devolve uma lista de evento []
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break

    pygame.display.update()
    relogio.tick(60)

print("Volte Sempre!!!!")