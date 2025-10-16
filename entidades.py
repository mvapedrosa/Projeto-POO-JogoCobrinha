import random
import pygame as pg
from configuracoes import *

class Direcao:
    def __init__(self, dx, dy):
        # TODO: inicialize os atributos de instância dx e dy
        raise NotImplementedError

    def eh_oposta_de(self, outra):
        """
        Função que indica se duas direções são opostas.

        TODO: retorne True se esta direção for oposta à direção "outra".
        Dica: para descobrir se duas direções são opostas, compare seus
        deslocamentos (dx, dy). 
        - Se a soma das componentes horizontais (dx) der 0, significa
          que uma aponta para a direita (+1) e a outra para a esquerda (-1).
        - Se a soma das componentes verticais (dy) der 0, significa
          que uma aponta para cima (-1) e a outra para baixo (+1).
        Portanto, duas direções são opostas se a soma dos seus deslocamentos
        (dx e dy) resultar em (0, 0).
        """
        # TODO: implementar conforme a explicação acima
        raise NotImplementedError

# Constantes globais (direções possíveis)
"""
O par (dx, dy) indica o quanto a cobra se move na grade em cada passo:
- dx =  1 → anda 1 célula para a direita
- dx = -1 → anda 1 célula para a esquerda
- dy = -1 → anda 1 célula para cima
- dy =  1 → anda 1 célula para baixo

TODO: Crie 4 objetos fixos (constantes globais) da classe Direcao.
Eles devem ter exatamente os nomes abaixo e representar os movimentos:
- CIMA     → deslocamento (0, -1)
- BAIXO    → deslocamento (0,  1)
- ESQUERDA → deslocamento (-1, 0)
- DIREITA  → deslocamento (1,  0)
"""
# TODO: implementar as constantes de direção conforme a explicação acima

class Cobra:
    def __init__(self, corpo_inicial, direcao_inicial):
        """
        Inicializa a cobra.

        TODO:
        - Guarde uma cópia de `corpo_inicial` em `self.corpo` como 
          `list(corpo_inicial)`.
        - Guarde a direção inicial em `self.direcao`.
        - Crie `self.crescer_pendente` e comece em 0. Esse contador indica quantos
          passos futuros a cobra ainda vai crescer (unidades por passo definida em 
          configuração).

        Parâmetros do método:
        - corpo_inicial: iterável de tuplas (x, y) onde corpo[0] é a cabeça.
        - direcao_inicial: objeto direção (possui `dx` e `dy`).
        """
        # TODO: implementar conforme a explicação acima
        raise NotImplementedError

    def cabeca(self):
        """
        Retorna a posição (x, y) da cabeça da cobra.

        TODO:
        - Devolva o primeiro elemento da lista `self.corpo`.
          Dica: a cabeça sempre é `self.corpo[0]`.
          Não é necessário tratar lista vazia aqui porque a cobra nunca fica sem
          segmentos durante o jogo.
        """
        # TODO: retornar a cabeça
        raise NotImplementedError

    def virar(self, nova_direcao):
        """
        Troca a direção atual da cobra, sem permitir reversão de 180º.

        TODO:
        - Altere `self.direcao` para `nova_direcao` apenas se ela não
          for oposta à direção atual.
          Dica: use o método `eh_oposta_de` da própria direção, que 
          retorna True se as direções são opostas e False caso contrário.
          Isso evita "auto-colisão instantânea" (virar de DIREITA para
          ESQUERDA no mesmo passo, por exemplo).
        """
        # TODO: aplicar a troca segura de direção
        raise NotImplementedError

    def andar(self):
        """
        Avança a cobra um passo na direção atual.

        Sequência de passos (recomendado):

        TODO:
        1) Descubra a posição atual da cabeça: `x, y = self.cabeca()`.
        2) Calcule a nova cabeça somando os deltas da direção:
           `nova_cabeca = (x + self.direcao.dx, y + self.direcao.dy)`.
           Explicação: `dx` altera a coluna (x), `dy` altera a linha (y).
        3) Insira a nova cabeça no início da lista:
           `self.corpo.insert(0, nova_cabeca)`.
           Observação: a ordem importa: cabeça é sempre índice 0.
        4) Crescimento: se `self.crescer_pendente > 0`, não remova a cauda
           neste passo e apenas redefina `self.crescer_pendente` consumindo 
           1 unidade:
           `self.crescer_pendente -= 1`.
           Caso contrário (`== 0`), remova o último segmento:
           `self.corpo.pop()`.
           Por quê? O efeito de "crescer" é simplesmente deixar de remover
           a cauda, aumentando o comprimento total.
        """
        # TODO: implementar a lógica de avanço + crescimento
        raise NotImplementedError

    def crescer(self, passos=1):
        """
        Agenda crescimento futuro.

        TODO:
        - Aumente `self.crescer_pendente` em `passos`.
          Dica: o crescimento não acontece imediatamente aqui.
          Ele será aplicado aos poucos, 1 segmento por passo, dentro do método
          `andar` (quando você deixa de remover a cauda).
        """
        # TODO: incrementar o contador de crescimento pendente
        raise NotImplementedError

    def bateu_no_corpo(self):
        """
        Verifica auto-colisão: a cabeça tocou algum outro segmento?

        TODO:
        - Compare a cabeça (`self.cabeca()`) com os demais segmentos do corpo.
          Dica: use `self.corpo[1:]` para ignorar a cabeça e checar só o
          "resto" do corpo.
          Ex.: `return self.cabeca() in self.corpo[1:]`
        - Por que funciona? Porque cada célula ocupada é uma tupla (x, y) e a
          checagem de pertencimento (`in`) funciona para listas de tuplas.
        """
        # TODO: retornar True/False conforme colisão com o próprio corpo
        raise NotImplementedError

    def desenhar(self, tela):
        """
        Desenha a cobra na tela (um retângulo por segmento).

        - Percorre `self.corpo` com `enumerate` para saber índice e posição:
            for i, (x, y) in enumerate(self.corpo):
        - Constrói um retângulo alinhado à grade:
            ret = pg.Rect(x*TAMANHO_CELULA, y*TAMANHO_CELULA,
                          TAMANHO_CELULA, TAMANHO_CELULA)
        - Desenha com `pg.draw.rect` usando a cor `COR_COBRA`.
        - Usa um `border_radius` maior na cabeça para destacar:
            `border_radius=5 if i == 0 else 3`

        Explicação:
        - O modelo (lista de posições) está separado da renderização:
          aqui você só converte cada posição (x, y) em um quadradinho.
        - Multiplicar por `TAMANHO_CELULA` transforma coordenadas da grade
          (em células) para coordenadas de pixels na janela.
        """
        for i, (x, y) in enumerate(self.corpo):
            ret = pg.Rect(x*TAMANHO_CELULA, y*TAMANHO_CELULA, TAMANHO_CELULA, TAMANHO_CELULA)
            pg.draw.rect(tela, COR_COBRA, ret, border_radius=5 if i == 0 else 3)


class Comida:
    def __init__(self, posicao=(0, 0)):
        """
        Inicializa a comidinha do jogo.

        TODO:
        - Guarde em `self.posicao` a posição (x, y) inicial da comida.
        - Essa posição é dada em coordenadas da grade (não em pixels!).
        - Por padrão, começa em (0, 0), mas pode receber outra tupla.

        Observação:
        - A comidinha não é uma lista como a cobra, pois a comida ocupa
          sempre uma única célula da grade.
        """
        # TODO: armazenar a posição inicial
        raise NotImplementedError

    def reposicionar(self, ocupadas):
        """
        Escolhe aleatoriamente uma nova posição livre para a comida.

        TODO:
        1) Gere uma lista de todas as células da grade não ocupadas
           pela cobra.
           - Use compreensão de listas:
             [(x, y) for x in range(LARGURA_GRADE)
                      for y in range(ALTURA_GRADE)
                      if (x, y) not in ocupadas]
           - Aqui, `ocupadas` é um conjunto ou lista de posições (x, y).
        2) Se a lista não estiver vazia:
           - Use `random.choice(livres)` para escolher uma célula aleatória.
           - Atualize `self.posicao` com essa célula.

        Explicação:
        - Essa lógica garante que a comida nunca aparece em cima da cobra.
        - Caso extremo: se `livres` estiver vazio, significa que a grade
          está totalmente ocupada (cobra gigante). Nesse caso, não faz nada.
        """
        # TODO: implementar escolha de posição aleatória livre
        raise NotImplementedError

    def desenhar(self, tela):
        """
        Desenha a comida na tela como um quadradinho.

        - Pega `x, y = self.posicao`.
        - Constrói um retângulo alinhado à grade:
            ret = pg.Rect(x*TAMANHO_CELULA, y*TAMANHO_CELULA,
                          TAMANHO_CELULA, TAMANHO_CELULA)
        - Usa `pg.draw.rect` para desenhar o quadrado na cor `COR_COMIDA`.
        - Coloca `border_radius=6` para dar bordas arredondadas.

        Explicação:
        - Assim como a cobra, a comida está em coordenadas de grade.
          Multiplicar `x` e `y` por `TAMANHO_CELULA` converte para pixels.
        """
        x, y = self.posicao
        ret = pg.Rect(x*TAMANHO_CELULA, y*TAMANHO_CELULA, TAMANHO_CELULA, TAMANHO_CELULA)
        pg.draw.rect(tela, COR_COMIDA, ret, border_radius=6)
