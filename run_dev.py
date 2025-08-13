# run_dev.py
from app import app

if __name__ == "__main__":
    print("🔧 Iniciando ERP de Vendas...")
    print("👉 Acesse: http://localhost:5000")
    app.run(debug=True)