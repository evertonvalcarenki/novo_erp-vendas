# models.py (atualizado)
import sqlite3
from datetime import datetime, timedelta
from flask_bcrypt import Bcrypt
from app import app  # Para usar o bcrypt

bcrypt = Bcrypt(app)

def get_db():
    return sqlite3.connect('banco.db')

# ... (o resto dos modelos: produtos, clientes, vendas, etc) ...

# 🔐 Usuários
def criar_usuario(username, senha, nome_completo):
    conn = get_db()
    hashed = bcrypt.generate_password_hash(senha).decode('utf-8')
    try:
        conn.execute(
            "INSERT INTO usuarios (username, senha, nome_completo) VALUES (?, ?, ?)",
            (username, hashed, nome_completo)
        )
        conn.commit()
        conn.close()
        return True
    except:
        conn.close()
        return False

def verificar_login(username, senha):
    conn = get_db()
    cursor = conn.execute(
        "SELECT senha FROM usuarios WHERE username = ?", (username,)
    )
    user = cursor.fetchone()
    conn.close()
    if user and bcrypt.check_password_hash(user[0], senha):
        return True
    return False