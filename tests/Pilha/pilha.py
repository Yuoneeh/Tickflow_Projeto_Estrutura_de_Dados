
class PilhaEncadeada:
    def __init__(self):
        self.topo = None
        self.tam = 0


    def __repr__ (self):
      return "["+str(self.topo)+"]"

    def is_empty(self):
        if self.topo == None:
          print(f'UnderFlow Reconhecido, Encerrando Processamento.')
          return True
        else:
          return False

    def push(self, dado):
        
        novo = No(dado)
        novo.prox = self.topo
        self.topo = novo
        self.tam += 1


    def pop(self):
        
        
          self.is_empty()
          T = self.topo
          topo = T.prox
          T.prox = None
          self.tam -= 1

    def peek(self):
        self.is_empty()
        print(self.topo)

    def size(self):
       
        print(f'Tamanho da Pilha: {self.tam}')

    def listar(self):
       

        self.atual = self.topo

      #for i in range(self.tam):  
       #  print(self)