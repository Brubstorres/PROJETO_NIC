import sqlite3
import os
from contextlib import contextmanager

# Caminho para o arquivo do banco de dados SQLite
# O banco será criado na pasta 'backend' do projeto
DB_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.abspath(os.path.join(DB_DIR, "..", "projeto_nic.db"))

def obter_conexao():
    """
    Cria e retorna uma conexão com o banco de dados SQLite.
    Configura a Row Factory para permitir acessar as colunas pelo nome (ex: row['nome']).
    """
    # Garante que a pasta pai exista
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    
    # Habilita o suporte a chaves estrangeiras no SQLite
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

@contextmanager
def abrir_sessao():
    """
    Gerenciador de contexto para uso seguro da conexão.
    Realiza commit automaticamente e fecha a conexão no final.
    Em caso de erro, faz rollback da transação.
    
    Exemplo de uso:
        with abrir_sessao() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM tabela")
            resultados = cursor.fetchall()
    """
    conn = obter_conexao()
    try:
        yield conn
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()

def inicializar_banco():
    """
    Testa a conexão com o banco de dados e cria o arquivo se não existir.
    """
    try:
        with abrir_sessao() as conn:
            print(f"Banco de dados conectado e inicializado em: {DB_PATH}")
            return True
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return False

if __name__ == "__main__":
    inicializar_banco()
