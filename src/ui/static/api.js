/**
 * api.js — Camada de comunicação com o backend Python (Flask)
 * Todos os fetch() do projeto passam por aqui.
 * trocar BASE_URL para apontar para o servidor.
 */

const BASE_URL = "http://localhost:5000";

async function apiFetch(path, options = {}) {
  const res = await fetch(BASE_URL + path, {
    credentials: "include",
    headers: { "Content-Type": "application/json", ...(options.headers || {}) },
    ...options,
  });
  const data = await res.json().catch(() => ({}));
  return { ok: res.ok, status: res.status, data };
}

// ── AUTH ──────────────────────────────────────────
export const api = {
  login: (email, senha) =>
    apiFetch("/api/login", { method: "POST", body: JSON.stringify({ email, senha }) }),

  cadastrar: (nome, email, senha) =>
    apiFetch("/api/cadastrar", { method: "POST", body: JSON.stringify({ nome, email, senha }) }),

  visitante: () =>
    apiFetch("/api/visitante", { method: "POST" }),

  logout: () =>
    apiFetch("/api/logout", { method: "POST" }),

  me: () =>
    apiFetch("/api/me"),

  // ── EVENTOS (Lista Encadeada) ──────────────────
  eventos: (busca = "", genero = "", ordenar = "data") =>
    apiFetch(`/api/eventos?busca=${encodeURIComponent(busca)}&genero=${encodeURIComponent(genero)}&ordenar=${ordenar}`),

  evento: (id) =>
    apiFetch(`/api/eventos/${id}`),

  adicionarEvento: (dados) =>
    apiFetch("/api/eventos", { method: "POST", body: JSON.stringify(dados) }),

  // ── FILA (FilaCompra FIFO) ─────────────────────
  entrarFila: (evento_id) =>
    apiFetch("/api/fila/entrar", { method: "POST", body: JSON.stringify({ evento_id }) }),

  estadoFila: () =>
    apiFetch("/api/fila/estado"),

  proximoFila: () =>
    apiFetch("/api/fila/proximo", { method: "POST" }),

  // ── COMPRA (PilhaAcoes LIFO) ───────────────────
  iniciarCompra: (evento_id, quantidade) =>
    apiFetch("/api/compra/iniciar", { method: "POST", body: JSON.stringify({ evento_id, quantidade }) }),

  alterarQuantidade: (quantidade) =>
    apiFetch("/api/compra/quantidade", { method: "POST", body: JSON.stringify({ quantidade }) }),

  desfazer: () =>
    apiFetch("/api/compra/desfazer", { method: "POST" }),

  confirmarCompra: (evento_id, quantidade) =>
    apiFetch("/api/compra/confirmar", { method: "POST", body: JSON.stringify({ evento_id, quantidade }) }),

  estadoPilha: () =>
    apiFetch("/api/pilha/estado"),
};
