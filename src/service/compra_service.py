"""
SERVICE: CompraService
Orquestra a FilaCompra (FIFO) e a PilhaAcoes (LIFO).
Controla o fluxo de compra: entrar na fila → ser atendido → confirmar.
"""

import random
import string
from datetime import datetime
from src.core.fila import FilaCompra
from src.core.pilha import PilhaAcoes


class CompraService:
    def __init__(self, evento_service):
        self.evento_service = evento_service
        self.fila = FilaCompra()
        self.pilha = PilhaAcoes()

    # ── FILA ────────────────────────────────────────────────────

    def entrar_na_fila(self, usuario: dict, evento_id: int) -> dict:
        """
        Coloca usuário no final da fila (enqueue).
        Retorna a posição e o timestamp de entrada.
        """
        entrada = {
            "id": usuario["id"],
            "nome": usuario["nome"],
            "evento_id": evento_id,
            "timestamp": datetime.now().strftime("%H:%M:%S"),
            "usuario_atual": usuario.get("usuario_atual", False),
        }
        self.fila.enqueue(entrada)

        # Registra na pilha
        self.pilha.push({
            "tipo": "ENTRAR_FILA",
            "descricao": f"Entrou na fila do evento #{evento_id}",
            "payload": entrada,
        })

        posicao = self.fila.posicao_do(usuario["id"])
        return {"posicao": posicao, "timestamp": entrada["timestamp"]}

    def proximo_da_fila(self) -> dict | None:
        """Remove e retorna o próximo da fila (dequeue). O(1)"""
        return self.fila.dequeue()

    def ver_frente(self) -> dict | None:
        """Peek na fila — ver quem é o próximo sem remover. O(1)"""
        return self.fila.frente()

    def estado_fila(self) -> list:
        """Retorna a fila como lista para serialização."""
        return self.fila.para_lista()

    def tamanho_fila(self) -> int:
        return len(self.fila)

    # ── COMPRA ──────────────────────────────────────────────────

    def iniciar_compra(self, usuario_id: str, evento_id: int, quantidade: int) -> dict:
        """Registra início de compra na pilha."""
        acao = {
            "tipo": "INICIAR_COMPRA",
            "descricao": f"Iniciou compra: {quantidade}x ingresso(s) — evento #{evento_id}",
            "payload": {"usuario_id": usuario_id, "evento_id": evento_id, "quantidade": quantidade},
        }
        self.pilha.push(acao)
        return acao

    def alterar_quantidade(self, quantidade_nova: int) -> dict:
        """Registra alteração de quantidade na pilha."""
        acao = {
            "tipo": "ALTERAR_QUANTIDADE",
            "descricao": f"Alterou quantidade para {quantidade_nova}",
            "payload": {"quantidade": quantidade_nova},
        }
        self.pilha.push(acao)
        return acao

    def desfazer(self) -> dict | None:
        """
        Pop da pilha — desfaz última ação (LIFO). O(1)
        """
        return self.pilha.pop()

    def confirmar_compra(self, evento_id: int, quantidade: int, usuario: dict) -> dict | None:
        """
        Confirma a compra: atualiza o estoque e gera código do ingresso.
        """
        sucesso = self.evento_service.registrar_venda(evento_id, quantidade)
        if not sucesso:
            return None

        codigo = "TF-" + "".join(random.choices(string.ascii_uppercase + string.digits, k=6))
        resultado = {
            "codigo": codigo,
            "evento_id": evento_id,
            "quantidade": quantidade,
            "usuario": usuario["nome"],
            "timestamp": datetime.now().strftime("%d/%m/%Y %H:%M"),
        }

        self.pilha.push({
            "tipo": "COMPRA_CONFIRMADA",
            "descricao": f"Compra confirmada: {quantidade}x evento #{evento_id} — {codigo}",
            "payload": resultado,
        })

        return resultado

    # ── PILHA ───────────────────────────────────────────────────

    def estado_pilha(self) -> list:
        """Retorna a pilha como lista (do topo para base)."""
        return self.pilha.para_lista()

    def topo_pilha(self) -> dict | None:
        return self.pilha.peek()