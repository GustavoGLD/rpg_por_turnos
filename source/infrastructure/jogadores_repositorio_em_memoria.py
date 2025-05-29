from source.application.repositorio_de_jogadores import RepositorioDeJogadores
from source.domain.Jogador import Jogador


class RepositorioDeJogadoresEmMemoria(RepositorioDeJogadores):
    def __init__(self):
        self.jogadores = {}

    def adicionar_jogador(self, jogador: Jogador):
        self.jogadores[jogador.nickname] = jogador

    def obter_jogador(self, nickname) -> Jogador:
        return self.jogadores.get(nickname)

    def remover_jogador(self, nickname):
        if nickname in self.jogadores:
            del self.jogadores[nickname]

    def listar_jogadores(self):
        return list(self.jogadores.values())