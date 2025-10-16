import pygame as pg
from configuracoes import *
from entidades import Cobra, Comida, CIMA, BAIXO, ESQUERDA, DIREITA

class Jogo:
    def __init__(self):
        self.recorde = 0
        self.reiniciar()

    def reiniciar(self):
        cx, cy = LARGURA_GRADE // 2, ALTURA_GRADE // 2
        corpo = [(cx - i, cy) for i in range(TAMANHO_INICIAL)]
        self.cobra = Cobra(corpo, DIREITA)

        self.comida = Comida()
        self.comida.reposicionar(ocupadas=set(self.cobra.corpo))

        self.pontuacao = 0
        self.viva = True
        self.passos_por_segundo = PASSOS_POR_SEGUNDO_INICIO
        self._acumulador = 0.0

    def _direcao_via_teclado(self, teclas):
        m = {
            pg.K_UP: CIMA,    pg.K_w: CIMA,
            pg.K_DOWN: BAIXO, pg.K_s: BAIXO,
            pg.K_LEFT: ESQUERDA, pg.K_a: ESQUERDA,
            pg.K_RIGHT: DIREITA, pg.K_d: DIREITA,
        }
        for tecla, direcao in m.items():
            if teclas[tecla]:
                return direcao
        return None

    def _aplicar_bordas(self):
        x, y = self.cobra.cabeca()
        if ATRAVESSAR_BORDAS:
            self.cobra.corpo = [((px % LARGURA_GRADE), (py % ALTURA_GRADE))
                                for (px, py) in self.cobra.corpo]
            return True
        else:
            return (0 <= x < LARGURA_GRADE) and (0 <= y < ALTURA_GRADE)

    def _passo(self):
        if not self.viva: return
        self.cobra.andar()
        if not self._aplicar_bordas():
            self.viva = False; return
        if self.cobra.bateu_no_corpo():
            self.viva = False; return
        if self.cobra.cabeca() == self.comida.posicao:
            self.cobra.crescer(CRESCER_POR_COMIDA)
            self.pontuacao += 1
            self.recorde = max(self.recorde, self.pontuacao)
            self.comida.reposicionar(set(self.cobra.corpo))
            if self.pontuacao and self.pontuacao % AUMENTA_VELOCIDADE_A_CADA == 0:
                self.passos_por_segundo = min(
                    PASSOS_POR_SEGUNDO_MAXIMO,
                    self.passos_por_segundo * FATOR_AUMENTO_VELOCIDADE
                )

    def atualizar(self, delta_t, teclas):
        if not self.viva: return
        direcao = self._direcao_via_teclado(teclas)
        if direcao: self.cobra.virar(direcao)
        self._acumulador += delta_t
        tempo_por_passo = 1.0 / self.passos_por_segundo
        while self._acumulador >= tempo_por_passo:
            self._acumulador -= tempo_por_passo
            self._passo()

    def desenhar(self, tela, fonte):
        tela.fill(COR_FUNDO)
        for x in range(1, LARGURA_GRADE):
            pg.draw.line(tela, COR_GRADE, (x*TAMANHO_CELULA, 0), (x*TAMANHO_CELULA, ALTURA_JANELA))
        for y in range(1, ALTURA_GRADE):
            pg.draw.line(tela, COR_GRADE, (0, y*TAMANHO_CELULA), (LARGURA_JANELA, y*TAMANHO_CELULA))

        self.comida.desenhar(tela)
        self.cobra.desenhar(tela)

        txt_pts = fonte.render(f"Pontuação: {self.pontuacao}", True, COR_TEXTO)
        txt_rec = fonte.render(f"Recorde: {self.recorde}", True, COR_TEXTO)
        txt_vel = fonte.render(f"{self.passos_por_segundo:.1f} passos/s", True, COR_TEXTO)
        tela.blit(txt_pts, (10, 8))
        tela.blit(txt_rec, (LARGURA_JANELA - txt_rec.get_width() - 10, 8))
        tela.blit(txt_vel, ((LARGURA_JANELA - txt_vel.get_width()) // 2, 8))

        if not self.viva:
            msg = fonte.render("Game Over — R para reiniciar", True, COR_AVISO)
            tela.blit(msg, ((LARGURA_JANELA - msg.get_width()) // 2, ALTURA_JANELA // 2 - 14))
