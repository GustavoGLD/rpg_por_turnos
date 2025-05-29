from abc import ABC, abstractmethod

from source.domain.Jogador import Jogador


# Apenas ‘interface’ porque o repositório pode ser implementado de várias formas,
# com array, json, sql, mongodb, etc... só adicionar na pasta /source/infrastructure
class RepositorioDeJogadores(ABC):

    @abstractmethod
    def adicionar_jogador(self, jogador):
        ...

    @abstractmethod
    def remover_jogador(self, nickname):
        ...

    @abstractmethod
    def obter_jogador(self, nickname) -> Jogador:
        ...

    @abstractmethod
    def listar_jogadores(self):
        ...