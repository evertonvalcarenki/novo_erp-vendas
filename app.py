# app.py (com login)
from flask import Flask, render_template, request, redirect, url_for, flash, session
import models
import database

app = Flask(__name__)
app.secret_key = 'chave_super_secreta_para_mensagens'

# 🔐 Verifica se o usuário está logado
@app.before_request
def require_login():
    allowed_routes = ['login', 'cadastro']
    if 'username' not in session and request.endpoint not in allowed_routes:
        return redirect(url_for('login'))

# 📌 Página inicial
@app.route('/')
def index():
    return render_template('index.html')

# 🔐 Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        senha = request.form['senha']
        if models.verificar_login(username, senha):
            session['username'] = username
            flash("✅ Login realizado com sucesso!", "success")
            return redirect(url_for('index'))
        else:
            flash("❌ Usuário ou senha incorretos.", "danger")
    return render_template('login.html')

# 🆕 Cadastro de usuário
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        username = request.form['username']
        senha = request.form['senha']
        nome = request.form['nome']
        if models.criar_usuario(username, senha, nome):
            flash("✅ Usuário criado com sucesso! Faça login.", "success")
            return redirect(url_for('login'))
        else:
            flash("⚠️ Nome de usuário já existe.", "warning")
    return render_template('cadastro.html')

# 🔐 Logout
@app.route('/logout')
def logout():
    session.pop('username', None)
    flash("Você saiu do sistema.", "info")
    return redirect(url_for('login'))

# ... (rotas de produtos, clientes, vendas, etc) ...

if __name__ == '__main__':
    database.criar_banco()
    # Cria o usuário admin padrão com senha '1234'
    import sqlite3
    conn = sqlite3.connect('banco.db')
    hashed = bcrypt.generate_password_hash('1234').decode('utf-8')
    conn.execute('''
        INSERT OR IGNORE INTO usuarios (username, senha, nome_completo)
        VALUES ('admin', ?, 'Administrador do Sistema')
    ''', (hashed,))
    conn.commit()
    conn.close()
    # Inicia o app
    app.run(debug=True)