"""
Service: Compra Service

Controla: 
Fila de Compra (FIFO)
Historico de Ações (LIFO Pilha)

"""

from collections import deque
from datetime import datetime

class CompraService :
    def __init__(self, evento_service):
        self.evento_service = evento_service

        #Fila
        self.fila = deque()

        #Pilha
        self.pilha = []

    def topo_pilha(self):
        pass