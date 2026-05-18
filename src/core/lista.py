"""
ESTRUTURA DE DADOS: LISTA ENCADEADA DE EVENTOS
Implementação manual — sem uso de list nativa para ordenação.
Inserção sempre ordenada por data crescente.
"""

from datetime import datetime


class NodeEvento:
    """Nó da lista encadeada."""
    def __init__(self, evento: dict):
        self.evento = evento
        self.proximo = None


class ListaEventos:
    """
    Lista encadeada simples para armazenar eventos ordenados por data.

    Complexidade:
        - Inserção ordenada: O(n)
        - Busca por ID:      O(n)
        - Remoção por ID:    O(n)
        - Exibição:          O(n)
    """

    def __init__(self):
        self.cabeca = None
        self.tamanho = 0

    def _parse_data(self, data_str: str) -> datetime:
        """Converte string de data para datetime."""
        try:
            return datetime.strptime(data_str, "%Y-%m-%d")
        except ValueError:
            return datetime.max

    def inserir_ordenado(self, evento: dict) -> None:
        """
        Insere um evento mantendo a lista ordenada por data crescente.
        Complexidade: O(n)
        """
        novo = NodeEvento(evento)
        self.tamanho += 1

        # Lista vazia ou novo evento é o mais antigo
        if self.cabeca is None or self._parse_data(evento["data"]) <= self._parse_data(self.cabeca.evento["data"]):
            novo.proximo = self.cabeca
            self.cabeca = novo
            return

        # Encontra posição correta
        atual = self.cabeca
        while atual.proximo and self._parse_data(atual.proximo.evento["data"]) < self._parse_data(evento["data"]):
            atual = atual.proximo

        novo.proximo = atual.proximo
        atual.proximo = novo

    def buscar_por_id(self, evento_id: int) -> dict | None:
        """
        Busca evento pelo ID.
        Complexidade: O(n)
        """
        atual = self.cabeca
        while atual:
            if atual.evento["id"] == evento_id:
                return atual.evento
            atual = atual.proximo
        return None

    def remover_por_id(self, evento_id: int) -> bool:
        """
        Remove evento pelo ID.
        Complexidade: O(n)
        """
        if self.cabeca is None:
            return False

        if self.cabeca.evento["id"] == evento_id:
            self.cabeca = self.cabeca.proximo
            self.tamanho -= 1
            return True

        atual = self.cabeca
        while atual.proximo:
            if atual.proximo.evento["id"] == evento_id:
                atual.proximo = atual.proximo.proximo
                self.tamanho -= 1
                return True
            atual = atual.proximo

        return False

    def para_lista(self) -> list:
        """
        Converte para lista Python para serialização.
        Complexidade: O(n)
        """
        resultado = []
        atual = self.cabeca
        while atual:
            resultado.append(atual.evento)
            atual = atual.proximo
        return resultado

    def exibir(self) -> None:
        """Exibe todos os eventos no console."""
        if self.cabeca is None:
            print("  [Lista vazia]")
            return
        atual = self.cabeca
        i = 1
        while atual:
            e = atual.evento
            print(f"  [{i}] {e['nome']} — {e['data']} — R${e['preco']:.2f}")
            atual = atual.proximo
            i += 1

    def __len__(self):
        return self.tamanho