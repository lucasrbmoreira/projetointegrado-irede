from flask import Flask
import os
from datetime import datetime

app = Flask(__name__)

LOG_PATH = os.getenv("LOG_PATH", "/app/dados/acessos.txt")
APP_PORT = int(os.getenv("PORT", "8080"))

@app.route('/')
def home():
    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)

    with open(LOG_PATH, "a") as f:
        f.write(f"Acesso em: {now}\n")

    return f"""
    <h1>Aplicação Web Ativa</h1>
    <p>Projeto de exemplo com Python e Flask.</p>
    <p><b>Status:</b> Em execução local/container.</p>
    <p><b>Persistência:</b> Último registro em {now}.</p>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=APP_PORT)