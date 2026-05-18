class No:
    
    def __init__(self, dado):
        
        self.dado = dado
        self.prox = None

    def __repr__(self):
        return '%s -> %s' % (self.dado,self.prox)