# Projeto: Implementar o Jogo Cobrinha 🐍

Este é um projeto de implementação do jogo Cobrinha (Snake Game) em Python, usando a biblioteca Pygame.
O projeto é voltado para alunos da disciplina de Análise de Sistemas Orientada a Objetos do Centro Universitário do Rio Grande do Norte (UNI-RN). 

## 🚀 Funcionalidades do Jogo

- Movimento da cobrinha em uma grade.
- Crescimento ao comer a comida.
- Colisão com paredes ou consigo mesma (resultando em Game Over).
- Opção de atravessar as bordas (teleporte).
- Pontuação e recorde de pontos.
- Aceleração automática a cada X pontos.
- Pausar e retomar o jogo.
- HUD com pontuação, recorde e velocidade.

## 📂 Estrutura do Projeto

```
📦 cobrinha/
┣ 📄 configuracoes.py   → constantes do jogo (tamanho, cores, FPS, etc.)
┣ 📄 entidades.py       → classes do domínio (Direcao, Cobra, Comida)
┣ 📄 jogo.py            → regras do jogo (classe Jogo)
┣ 📄 main.py            → loop principal
┗ 📄 README.md          → este arquivo
```

## 🔗 Diagrama de Dependências

```text
main.py
├─ importa → jogo.py
│  ├─ importa → entidades.py
│  │  └─ importa → configuracoes.py
│  └─ importa → configuracoes.py
└─ importa → configuracoes.py
```


Em Resumo:

* `main.py` é o **diretor** (loop principal).
* `jogo.py` é o **cérebro** (regras).
* `entidades.py` define os **atores** (cobra, comida, direções).
* `configuracoes.py` define o **palco** (tamanho, cores, FPS, etc.).


## 🖥️ Como rodar o jogo

1. **Clonar o repositório**

   ```bash
   git clone https://github.com/seu-usuario/cobrinha.git
   cd cobrinha
   ```

2. **Criar um ambiente virtual (opcional, mas recomendado)**

   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

3. **Instalar dependências**

   ```bash
   pip install pygame
   ```

4. **Rodar o jogo**

   ```bash
   python main.py
   ```


## 🎮 Controles

* **Setas ou WASD** → mover a cobrinha.
* **R** → reiniciar após Game Over.
* **P** → pausar / retomar.
* **Fechar janela** → encerrar o jogo.


## 📝 Tarefas

Em `entidades.py`, resolva todos os TODO:
* [ ] Implemente a classe Direcao
* [ ] Implemente as constantes de direção 
* [ ] Implemente a classe Cobra
* [ ] Implemente a classe Comida

## 📝 Exercícios extras

* [ ] Alterar cores da cobrinha e da comida.
* [ ] Mudar o tamanho das células (`TAMANHO_CELULA`).
* [ ] Ativar `ATRAVESSAR_BORDAS = True` e testar a diferença.
* [ ] Ajustar `PASSOS_POR_SEGUNDO_INICIO` para calibrar a dificuldade.
* [ ] Fazer a cobrinha começar maior (`TAMANHO_INICIAL = 4`).
* [ ] Criar **2 comidas simultâneas** no tabuleiro.
* [ ] Mostrar uma **tela inicial** com instruções antes de começar.
* [ ] Adicionar **efeitos sonoros** ao comer ou perder.
* [ ] Implementar **níveis de dificuldade** (fácil, médio, difícil).
* [ ] Guardar o recorde em **arquivo** para persistir entre execuções.




