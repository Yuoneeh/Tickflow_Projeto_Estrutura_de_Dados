"""
ESTRUTURA DE DADOS: FILA (FIFO) DE COMPRAS
Implementação manual com nós encadeados.
Primeiro a entrar, primeiro a ser atendido.
"""


class NodeFila:
    """Nó da fila encadeada."""
    def __init__(self, dado: dict):
        self.dado = dado
        self.proximo = None


class FilaCompra:
    """
    Fila FIFO para gerenciar a ordem de atendimento de compras.

    Complexidade:
        - enqueue (entrar na fila): O(1)
        - dequeue (sair da fila):   O(1)
        - frente (peek):            O(1)
        - está_vazia:               O(1)
    """

    def __init__(self):
        self.frente_no = None   # Primeiro da fila (próximo a ser atendido)
        self.tras_no = None     # Último da fila (último a entrar)
        self.tamanho = 0

    def enqueue(self, usuario: dict) -> None:
        """
        Adiciona usuário ao final da fila.
        Complexidade: O(1)
        """
        novo = NodeFila(usuario)
        if self.tras_no is None:
            self.frente_no = self.tras_no = novo
        else:
            self.tras_no.proximo = novo
            self.tras_no = novo
        self.tamanho += 1

    def dequeue(self) -> dict | None:
        """
        Remove e retorna o usuário da frente da fila.
        Complexidade: O(1)
        """
        if self.esta_vazia():
            return None
        dado = self.frente_no.dado
        self.frente_no = self.frente_no.proximo
        if self.frente_no is None:
            self.tras_no = None
        self.tamanho -= 1
        return dado

    def frente(self) -> dict | None:
        """
        Retorna o usuário da frente sem remover (peek).
        Complexidade: O(1)
        """
        return self.frente_no.dado if self.frente_no else None

    def esta_vazia(self) -> bool:
        """Verifica se a fila está vazia. Complexidade: O(1)"""
        return self.tamanho == 0

    def posicao_do(self, usuario_id: str) -> int:
        """
        Retorna a posição de um usuário na fila (1-indexed).
        Retorna -1 se não encontrado.
        Complexidade: O(n)
        """
        atual = self.frente_no
        pos = 1
        while atual:
            if atual.dado.get("id") == usuario_id:
                return pos
            atual = atual.proximo
            pos += 1
        return -1

    def para_lista(self) -> list:
        """
        Converte a fila para lista Python (sem modificar a estrutura).
        Complexidade: O(n)
        """
        resultado = []
        atual = self.frente_no
        while atual:
            resultado.append(atual.dado)
            atual = atual.proximo
        return resultado

    def exibir(self) -> None:
        """Exibe o estado atual da fila no console."""
        if self.esta_vazia():
            print("  [Fila vazia]")
            return
        atual = self.frente_no
        pos = 1
        while atual:
            u = atual.dado
            status = " ← PRÓXIMO" if pos == 1 else ""
            print(f"  #{pos} {u.get('nome', 'Usuário')} — entrou às {u.get('timestamp', '?')}{status}")
            atual = atual.proximo
            pos += 1

    def __len__(self):
        return self.tamanho