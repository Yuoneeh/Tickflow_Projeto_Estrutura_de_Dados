class No:
    def __init__(self, dado):
        # TODO: armazenar o dado recebido
        # TODO: inicializar o ponteiro/referência para None
        self.dado = dado
        self.prox = None

    def __repr__(self):
        # TODO: retornar uma representação textual do nó
        # Exemplo: No(10)
        return '%s -> %s' % (self.dado,self.prox)