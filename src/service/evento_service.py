"""
SERVICE: EventoService
Orquestra operações sobre a ListaEventos.
Carrega dados do JSON e expõe operações de negócio.
"""

import json
import os
from datetime import datetime
from src.core.lista import ListaEventos

DATA_PATH = os.path.join(os.path.dirname(__file__), "../../data/eventos.json")


class EventoService:
    def __init__(self):
        self.lista = ListaEventos()
        self._proximo_id = 100
        self._carregar_dados()

    def _carregar_dados(self) -> None:
        """Carrega eventos do arquivo JSON e insere na lista ordenada."""
        try:
            with open(DATA_PATH, "r", encoding="utf-8") as f:
                eventos = json.load(f)
            for e in eventos:
                self.lista.inserir_ordenado(e)
                if e["id"] >= self._proximo_id:
                    self._proximo_id = e["id"] + 1
        except (FileNotFoundError, json.JSONDecodeError):
            pass

    def _salvar_dados(self) -> None:
        """Persiste a lista atual no arquivo JSON."""
        os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)
        with open(DATA_PATH, "w", encoding="utf-8") as f:
            json.dump(self.lista.para_lista(), f, ensure_ascii=False, indent=2)

    def listar_todos(self) -> list:
        """Retorna todos os eventos em ordem de data."""
        return self.lista.para_lista()

    def buscar_por_id(self, evento_id: int) -> dict | None:
        return self.lista.buscar_por_id(evento_id)

    def adicionar_evento(self, dados: dict) -> dict:
        """Adiciona um novo evento à lista ordenada e persiste."""
        evento = {
            "id":        self._proximo_id,
            "nome":      dados["nome"],
            "artista":   dados["artista"],
            "genero":    dados.get("genero", "Outros"),
            "data":      dados["data"],
            "horario":   dados.get("horario", "20:00"),
            "local":     dados["local"],
            "preco":     float(dados["preco"]),
            "ingressos": int(dados["ingressos"]),
            "vendidos":  0,
            "emoji":     dados.get("emoji", "🎵"),
            "cor":       dados.get("cor", "#e8ff47"),
            "descricao": dados.get("descricao", ""),
        }
        self._proximo_id += 1
        self.lista.inserir_ordenado(evento)
        self._salvar_dados()
        return evento

    def registrar_venda(self, evento_id: int, quantidade: int) -> bool:
        """Atualiza o contador de ingressos vendidos."""
        evento = self.lista.buscar_por_id(evento_id)
        if not evento:
            return False
        disponivel = evento["ingressos"] - evento["vendidos"]
        if quantidade > disponivel:
            return False
        evento["vendidos"] += quantidade
        self._salvar_dados()
        return True

    def filtrar(self, busca: str = "", genero: str = "", ordenar_por: str = "data") -> list:
        """
        Filtra e ordena eventos.
        Ordenações extras usam Bubble Sort manual — sem sorted() nativo.
        """
        eventos = self.lista.para_lista()

        # Filtro por texto
        if busca:
            busca_low = busca.lower()
            eventos = [
                e for e in eventos
                if busca_low in e["nome"].lower() or busca_low in e["artista"].lower()
            ]

        # Filtro por gênero
        if genero and genero != "todos":
            eventos = [e for e in eventos if e["genero"].lower() == genero.lower()]

        # Ordenação manual (Bubble Sort) — proibido usar sort() ou sorted()
        if ordenar_por == "preco_asc":
            eventos = self._bubble_sort(eventos, key="preco", reverso=False)
        elif ordenar_por == "preco_desc":
            eventos = self._bubble_sort(eventos, key="preco", reverso=True)
        elif ordenar_por == "nome":
            eventos = self._bubble_sort(eventos, key="nome", reverso=False)
        # "data" já vem ordenado da lista encadeada

        return eventos

    def _bubble_sort(self, lista: list, key: str, reverso: bool) -> list:
        """
        Bubble Sort manual — O(n²).
        Implementação obrigatória conforme regras do projeto.
        Proibido usar sort() ou sorted().
        """
        arr = lista[:]
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                val_j    = arr[j][key]
                val_next = arr[j + 1][key]
                if isinstance(val_j, str):
                    condicao = val_j.lower() > val_next.lower()
                else:
                    condicao = val_j > val_next
                if (condicao and not reverso) or (not condicao and reverso):
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    def estatisticas(self) -> dict:
        """Retorna estatísticas gerais do catálogo."""
        eventos = self.lista.para_lista()
        total_disp = sum(e["ingressos"] - e["vendidos"] for e in eventos)
        return {
            "total_eventos":                 len(eventos),
            "total_ingressos_disponiveis":   total_disp,
        }