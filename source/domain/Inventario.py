class Inventario:
    def __init__(self, max_itens=20):
        self.itens = []
        self.max_itens = max_itens

    def add_item(self, item, quantity=1):
        if len(self.itens) < self.max_itens:
            for _ in range(quantity):
                self.itens.append(item)
        else:
            raise Exception("Inventario cheio")