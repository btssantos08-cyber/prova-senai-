import sqlite3

def conectar():
    conn = sqlite3.connect("escola.db")
    return conn

def criar_tabela():

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS alunos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL,
            nota REAL)
    """)

    conn.commit()
    conn.close()

def cadastro_aluno(nome: str, idade, nota):

    if nome.strip() == "":
        return "Nome do aluno não pode ficar em branco."
    
    elif idade > 22:
        return "Idade acima de 22 anos."
    
    else:
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("INSERT INTO alunos (nome, idade, nota) VALUES (?, ?, ?)", (nome, idade, nota))  

        conn.commit()
        conn.close()

        return "Aluno cadastrado com sucesso!"

def delete_aluno(id):
    if id > 0:
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM alunos WHERE id = ?", (id,))  

        conn.commit()
        conn.close()

        return f"O aluno de ID {id} foi deletado"
    else:
        return "ID inserido é inválido"
