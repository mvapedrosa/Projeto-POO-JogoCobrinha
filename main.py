import pygame as pg
from configuracoes import *
from jogo import Jogo

def main():
    pg.init()
    tela = pg.display.set_mode((LARGURA_JANELA, ALTURA_JANELA))
    pg.display.set_caption("Jogo Cobrinha")
    relogio = pg.time.Clock()
    fonte = pg.font.SysFont("Consolas", 22)

    jogo = Jogo()
    rodando, pausado = True, False

    while rodando:
        delta_t = relogio.tick(FPS) / 1000.0
        teclas = pg.key.get_pressed()

        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                rodando = False
            elif evento.type == pg.KEYDOWN:
                if evento.key == pg.K_r:
                    jogo.reiniciar(); pausado = False
                elif evento.key == pg.K_p:
                    pausado = not pausado

        if not pausado:
            jogo.atualizar(delta_t, teclas)

        jogo.desenhar(tela, fonte)

        if pausado:
            aviso = fonte.render("Pausado — P para retomar", True, COR_TEXTO)
            tela.blit(aviso, ((LARGURA_JANELA - aviso.get_width()) // 2, ALTURA_JANELA - 36))

        pg.display.flip()

    pg.quit()


if __name__ == "__main__":
    main()
