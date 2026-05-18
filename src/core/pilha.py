
import core.No as No

class PilhaEncadeada:
    def __init__(self):
        # TODO: inicializar o topo da pilha como None
        # TODO: inicializar contador de tamanho (opcional)
        self.topo = None
        self.tam = 0


    def __repr__ (self):
      return "["+str(self.topo)+"]"

    def is_empty(self):
        # TODO: retornar True se o topo for None
        if self.topo == None:
          print(f'UnderFlow Reconhecido, Encerrando Processamento.')
          return True
        else:
          return False

    def push(self, dado):
        # TODO:
        # 1. criar um novo nó com o dado
        # 2. fazer o novo nó apontar para o topo atual
        # 3. atualizar o topo para o novo nó
        # 4. incrementar o tamanho
        #
        # IMPORTANTE: inserir no INÍCIO da lista (topo da pilha)

        novo = No(dado)
        novo.prox = self.topo
        self.topo = novo
        self.tam += 1


    def pop(self):
        # TODO:
        # 1. verificar se a pilha está vazia (underflow)
        # 2. guardar o valor do topo
        # 3. atualizar o topo para o próximo nó
        # 4. decrementar o tamanho
        # 5. retornar o valor guardado
        #
        # IMPORTANTE: remover do INÍCIO da lista (topo da pilha)
          #1
          self.is_empty()
          #2
          T = self.topo
          #3
          topo = T.prox
          #4
          T.prox = None
          #5
          self.tam -= 1

    def peek(self):
        # TODO:
        # 1. verificar se a pilha está vazia
        # 2. retornar o valor do topo SEM remover
        self.is_empty()
        print(self.topo)

    def size(self):
        # TODO:
        # retornar o tamanho da pilha
        # (pode usar atributo de controle ou contar dinamicamente)
        print(f'Tamanho da Pilha: {self.tam}')

    def listar(self):
        # TODO:
        # percorrer a pilha do topo até a base
        # armazenar os valores em uma lista Python
        # retornar ou exibir os dados
        # Formato sugerido: [30, 20, 10] (topo à esquerda)

        self.atual = self.topo

       # for i in range(self.tam):
        print(self)