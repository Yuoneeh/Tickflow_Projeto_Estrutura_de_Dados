"""
SERVICE: AuthService
Autenticação simples em memória para fins de demonstração.
"""

import json
import os

USERS_PATH = os.path.join(os.path.dirname(__file__), "../../data/usuarios.json")


class AuthService:
    def __init__(self):
        self.usuarios = {}
        self._carregar()

    def _carregar(self):
        try:
            with open(USERS_PATH, "r", encoding="utf-8") as f:
                self.usuarios = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.usuarios = {"demo@tickflow.com": {"nome": "Demo User", "senha": "123456", "id": "user_demo"}}

    def _salvar(self):
        os.makedirs(os.path.dirname(USERS_PATH), exist_ok=True)
        with open(USERS_PATH, "w", encoding="utf-8") as f:
            json.dump(self.usuarios, f, ensure_ascii=False, indent=2)

    def login(self, email: str, senha: str) -> dict | None:
        user = self.usuarios.get(email)
        if user and user["senha"] == senha:
            return {"id": user["id"], "nome": user["nome"], "email": email}
        return None

    def cadastrar(self, nome: str, email: str, senha: str) -> dict | None:
        if email in self.usuarios:
            return None
        user_id = "user_" + email.split("@")[0]
        self.usuarios[email] = {"nome": nome, "senha": senha, "id": user_id}
        self._salvar()
        return {"id": user_id, "nome": nome, "email": email}

    def login_visitante(self) -> dict:
        return {"id": "visitante_" + str(id(self)), "nome": "Visitante", "email": ""}