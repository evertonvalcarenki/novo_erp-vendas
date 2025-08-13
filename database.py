# database.py (atualizado)
import sqlite3

def criar_banco():
    conn = sqlite3.connect('banco.db')
    cursor = conn.cursor()

    # Produtos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL
        )
    ''')

    # Clientes
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT
        )
    ''')

    # Vendas
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS vendas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente_id INTEGER,
            data TEXT,
            total REAL,
            FOREIGN KEY(cliente_id) REFERENCES clientes(id)
        )
    ''')

    # Parcelas
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS parcelas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            venda_id INTEGER,
            valor REAL,
            vencimento TEXT,
            pago INTEGER DEFAULT 0,
            FOREIGN KEY(venda_id) REFERENCES vendas(id)
        )
    ''')

    # Usuários (NOVO)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            senha TEXT NOT NULL,
            nome_completo TEXT
        )
    ''')

    # Insere um usuário admin padrão (se não existir)
    cursor.execute('''
        INSERT OR IGNORE INTO usuarios (username, senha, nome_completo)
        VALUES ('admin', 'pbkdf2:sha256:600000$...', 'Administrador')
    ''')

    conn.commit()
    conn.close()