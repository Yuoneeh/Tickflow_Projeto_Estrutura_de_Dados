"""
UI: app.py — Servidor Flask
Expõe endpoints JSON que as páginas HTML consomem via fetch().
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../.."))

from flask import Flask, request, jsonify, send_from_directory, session
from flask_cors import CORS
from service.evento_service import EventoService
from service.compra_service import CompraService
from service.auth_service import AuthService

app = Flask(__name__, static_folder="static")
app.secret_key = "tickflow_secret_2025"
CORS(app, supports_credentials=True)

# ── Instâncias dos serviços ──────────────────────────────────
evento_svc = EventoService()
compra_svc = CompraService(evento_svc)
auth_svc   = AuthService()

# ── Helper ───────────────────────────────────────────────────

def usuario_logado():
    return session.get("usuario")

# ════════════════════════════════════════════════════════════
# ROTAS — PÁGINAS HTML
# ════════════════════════════════════════════════════════════

@app.route("/")
def index():
    return send_from_directory("static", "login.html")

@app.route("/home")
def home():
    return send_from_directory("static", "home.html")

@app.route("/evento")
def evento():
    return send_from_directory("static", "evento.html")

@app.route("/fila")
def fila_page():
    return send_from_directory("static", "fila.html")

@app.route("/sucesso")
def sucesso():
    return send_from_directory("static", "sucesso.html")

# ════════════════════════════════════════════════════════════
# API — AUTH
# ════════════════════════════════════════════════════════════

@app.route("/api/login", methods=["POST"])
def api_login():
    dados = request.json
    user  = auth_svc.login(dados.get("email", ""), dados.get("senha", ""))
    if user:
        session["usuario"] = user
        return jsonify({"ok": True, "usuario": user})
    return jsonify({"ok": False, "erro": "E-mail ou senha inválidos"}), 401

@app.route("/api/cadastrar", methods=["POST"])
def api_cadastrar():
    dados = request.json
    user  = auth_svc.cadastrar(dados["nome"], dados["email"], dados["senha"])
    if user:
        session["usuario"] = user
        return jsonify({"ok": True, "usuario": user})
    return jsonify({"ok": False, "erro": "E-mail já cadastrado"}), 409

@app.route("/api/visitante", methods=["POST"])
def api_visitante():
    user = auth_svc.login_visitante()
    session["usuario"] = user
    return jsonify({"ok": True, "usuario": user})

@app.route("/api/logout", methods=["POST"])
def api_logout():
    session.clear()
    return jsonify({"ok": True})

@app.route("/api/me")
def api_me():
    user = usuario_logado()
    if user:
        return jsonify({"ok": True, "usuario": user})
    return jsonify({"ok": False}), 401

# ════════════════════════════════════════════════════════════
# API — EVENTOS (Lista Encadeada)
# ════════════════════════════════════════════════════════════

@app.route("/api/eventos")
def api_eventos():
    busca   = request.args.get("busca", "")
    genero  = request.args.get("genero", "")
    ordenar = request.args.get("ordenar", "data")
    eventos = evento_svc.filtrar(busca=busca, genero=genero, ordenar_por=ordenar)
    stats   = evento_svc.estatisticas()
    return jsonify({"eventos": eventos, "stats": stats})

@app.route("/api/eventos/<int:evento_id>")
def api_evento_detalhe(evento_id):
    evento = evento_svc.buscar_por_id(evento_id)
    if evento:
        return jsonify(evento)
    return jsonify({"erro": "Evento não encontrado"}), 404

@app.route("/api/eventos", methods=["POST"])
def api_adicionar_evento():
    dados = request.json
    try:
        evento = evento_svc.adicionar_evento(dados)
        return jsonify({"ok": True, "evento": evento})
    except Exception as e:
        return jsonify({"ok": False, "erro": str(e)}), 400

# ════════════════════════════════════════════════════════════
# API — FILA (FilaCompra FIFO)
# ════════════════════════════════════════════════════════════

@app.route("/api/fila/entrar", methods=["POST"])
def api_entrar_fila():
    dados   = request.json
    usuario = usuario_logado() or {"id": "visitante", "nome": "Visitante"}
    usuario["usuario_atual"] = True

    # Adiciona usuários fictícios na frente para simular a fila
    import random, time
    nomes_ficticios = ["Ana Lima", "Bruno Costa", "Carlos Dias", "Diana Ramos", "Eduardo Souza"]
    qtd_ficticios   = random.randint(2, 4)
    for i, nome in enumerate(nomes_ficticios[:qtd_ficticios]):
        ficto = {"id": f"ficto_{i}_{time.time()}", "nome": nome, "usuario_atual": False}
        compra_svc.entrar_na_fila(ficto, dados["evento_id"])

    resultado   = compra_svc.entrar_na_fila(usuario, dados["evento_id"])
    fila_atual  = compra_svc.estado_fila()
    return jsonify({
        "ok":       True,
        "posicao":  resultado["posicao"],
        "timestamp":resultado["timestamp"],
        "fila":     fila_atual,
        "tamanho":  compra_svc.tamanho_fila(),
    })

@app.route("/api/fila/estado")
def api_estado_fila():
    return jsonify({
        "fila":    compra_svc.estado_fila(),
        "tamanho": compra_svc.tamanho_fila(),
        "proximo": compra_svc.ver_frente(),
    })

@app.route("/api/fila/proximo", methods=["POST"])
def api_proximo_fila():
    proximo = compra_svc.proximo_da_fila()
    return jsonify({
        "ok":      True,
        "atendido":proximo,
        "proximo": compra_svc.ver_frente(),
        "tamanho": compra_svc.tamanho_fila(),
    })

# ════════════════════════════════════════════════════════════
# API — COMPRA (Pilha LIFO)
# ════════════════════════════════════════════════════════════

@app.route("/api/compra/iniciar", methods=["POST"])
def api_iniciar_compra():
    dados   = request.json
    usuario = usuario_logado() or {"id": "visitante", "nome": "Visitante"}
    acao    = compra_svc.iniciar_compra(usuario["id"], dados["evento_id"], dados.get("quantidade", 1))
    return jsonify({"ok": True, "acao": acao, "pilha": compra_svc.estado_pilha()})

@app.route("/api/compra/quantidade", methods=["POST"])
def api_alterar_quantidade():
    dados = request.json
    acao  = compra_svc.alterar_quantidade(dados["quantidade"])
    return jsonify({"ok": True, "acao": acao, "pilha": compra_svc.estado_pilha()})

@app.route("/api/compra/desfazer", methods=["POST"])
def api_desfazer():
    acao = compra_svc.desfazer()
    if acao:
        return jsonify({"ok": True, "desfeito": acao, "pilha": compra_svc.estado_pilha()})
    return jsonify({"ok": False, "erro": "Pilha vazia — nada para desfazer"}), 400

@app.route("/api/compra/confirmar", methods=["POST"])
def api_confirmar_compra():
    dados     = request.json
    usuario   = usuario_logado() or {"id": "visitante", "nome": "Visitante"}
    resultado = compra_svc.confirmar_compra(
        dados["evento_id"], dados["quantidade"], usuario
    )
    if resultado:
        return jsonify({"ok": True, "resultado": resultado, "pilha": compra_svc.estado_pilha()})
    return jsonify({"ok": False, "erro": "Ingressos insuficientes ou evento não encontrado"}), 400

@app.route("/api/pilha/estado")
def api_estado_pilha():
    return jsonify({
        "pilha": compra_svc.estado_pilha(),
        "topo":  compra_svc.topo_pilha(),
    })

# ════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("=" * 50)
    print("  TICKFLOW — Servidor iniciado")
    print("  Acesse: http://localhost:5000")
    print("=" * 50)
    app.run(debug=True, port=5000)