from source.application.repositorio_de_jogadores import RepositorioDeJogadores


class ControladorDeBatalhas:
    def __init__(self, jogadores_repositorio: RepositorioDeJogadores):
        self.jogadores_repositorio = jogadores_repositorio

    def iniciar_batalha(self, nickname_jogador1: str, nickname_jogador2: str):
        print(f'Batalha iniciada entre {nickname_jogador1} e {nickname_jogador2}')