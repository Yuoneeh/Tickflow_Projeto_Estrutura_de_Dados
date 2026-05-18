"""
ESTRUTURA DE DADOS: PILHA (LIFO) DE AÇÕES
Implementação manual para histórico e desfazimento de ações.
Último a entrar, primeiro a sair.
"""


class NodePilha:
    """Nó da pilha."""
    def __init__(self, acao: dict):
        self.acao = acao
        self.abaixo = None


class PilhaAcoes:
    """
    Pilha LIFO para registrar e desfazer ações do usuário.

    Complexidade:
        - push (empilhar):      O(1)
        - pop (desempilhar):    O(1)
        - peek (ver topo):      O(1)
        - está_vazia:           O(1)
    """

    def __init__(self):
        self.topo_no = None
        self.tamanho = 0

    def push(self, acao: dict) -> None:
        """
        Empilha uma ação no topo.
        Complexidade: O(1)
        """
        novo = NodePilha(acao)
        novo.abaixo = self.topo_no
        self.topo_no = novo
        self.tamanho += 1

    def pop(self) -> dict | None:
        """
        Remove e retorna a ação do topo (desfazer).
        Complexidade: O(1)
        """
        if self.esta_vazia():
            return None
        acao = self.topo_no.acao
        self.topo_no = self.topo_no.abaixo
        self.tamanho -= 1
        return acao

    def peek(self) -> dict | None:
        """
        Retorna a ação do topo sem remover.
        Complexidade: O(1)
        """
        return self.topo_no.acao if self.topo_no else None

    def esta_vazia(self) -> bool:
        """Verifica se a pilha está vazia. Complexidade: O(1)"""
        return self.tamanho == 0

    def para_lista(self) -> list:
        """
        Converte para lista (do topo para a base).
        Complexidade: O(n)
        """
        resultado = []
        atual = self.topo_no
        while atual:
            resultado.append(atual.acao)
            atual = atual.abaixo
        return resultado

    def exibir(self) -> None:
        """Exibe o estado da pilha no console."""
        if self.esta_vazia():
            print("  [Pilha vazia]")
            return
        atual = self.topo_no
        i = 0
        while atual:
            prefixo = " ← TOPO" if i == 0 else ""
            print(f"  [{self.tamanho - i}] {atual.acao.get('descricao', '?')}{prefixo}")
            atual = atual.abaixo
            i += 1

    def __len__(self):
        return self.tamanho