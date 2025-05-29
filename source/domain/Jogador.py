class Jogador:
    def __init__(self, nickname: str):
        self.nickname = nickname

        self.pontos = 0
        self.vitorias = 0
        self.derrotas = 0

    def acrescentar_pontos(self, pontos: int):
        self.pontos += pontos

    def incrementar_vitorias(self):
        self.vitorias += 1

    def incrementar_derrotas(self):
        self.derrotas += 1