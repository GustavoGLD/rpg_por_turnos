from source.application.controlador_de_batalhas import ControladorDeBatalhas
from source.domain.Jogador import Jogador
from source.infrastructure.jogadores_repositorio_em_memoria import RepositorioDeJogadoresEmMemoria

repositorio_de_jogadores = RepositorioDeJogadoresEmMemoria()

repositorio_de_jogadores.adicionar_jogador(Jogador('Protagonista'))
repositorio_de_jogadores.adicionar_jogador(Jogador('Oponente1'))
repositorio_de_jogadores.adicionar_jogador(Jogador('Oponente2'))

batalhas = ControladorDeBatalhas(repositorio_de_jogadores)
batalhas.iniciar_batalha('Protagonista', 'Oponente1')

repositorio_de_jogadores.obter_jogador('Protagonista').incrementar_vitorias()

