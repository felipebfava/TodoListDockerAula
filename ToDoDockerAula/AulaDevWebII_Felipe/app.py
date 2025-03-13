
# importando bibliotecas
from flask import Flask, render_template, request, redirect
import socket, os
import sqlite3

# dá para utilizar cache para melhor performance -> pip install redis
# import redis
# cache = redis.Redis(host='localhost', port=6379, db=0) 
 
# otimizacao de codigo
import logging

# criando app com Flask
app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# fazer antes da requisicao com logging
@app.before_request
def log_request_info(): 
    hostname = socket.gethostname()
    port = os.environ.get('PORT', '5000')  # Pega a porta do ambiente ou usa 5000 como padrão 
    logger.info(f"Requisição recebida em {hostname} na porta {port}") 

# conexão com o banco de dados sqlite
def connect_db():
    # return sqlite3.connect("database.db") # anterior
    db_path = '/app/db/database.db' 
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row 
    return conn 

@app.route('/env')
def env():
    return str(os.environ)

# teste para ver se a conexão funcionou
@app.route('/oi')
def hello():
    hostname = socket.gethostname()
    port = os.environ.get('PORT', '5000') # Pega a porta do ambiente ou usa 5000 como padrão
    logger.info(f"Requisição recebida em {hostname} na porta {port}") # do logging
    return f"Hello from {hostname} on port {port}!\n"

# utilizando junto com o redis
# @app.route('/')
# def index():
#     tasks = cache.get('tasks') 
#     if not tasks: 
#         con = connect_db() 
#         cur = con.cursor() 
#         cur.execute("SELECT * FROM tasks") 
#         tasks = cur.fetchall() 
#         con.close() 
#         cache.set('tasks', str(tasks), ex=30)  # Expira em 30s 
#     return render_template("index.html", tasks=eval(tasks)) 

# rota básica onde exibe as tarefas
@app.route('/')
def index():
    con = connect_db()
    cur = con.cursor()
    cur.execute("SELECT * FROM tasks")
    tasks = cur.fetchall()
    con.close()
    return render_template("index.html", tasks=tasks)

# rota para adicionar tarefas
@app.route('/add', methods=['POST'])
def add_task():
    task = request.form['task']
    con = connect_db()
    cur = con.cursor()
    cur.execute("INSERT INTO tasks (task, completed) VALUES (?, ?)", (task,
    0))
    con.commit()
    con.close()
    return redirect('/')

# rota para deletar tarefas por id
@app.route('/delete/<int:id>')
def delete_task(id):
    con = connect_db()
    cur = con.cursor()
    cur.execute("DELETE FROM tasks WHERE id=?", (id,))
    con.commit()
    con.close()
    return redirect('/')

# rota para marcar uma tarefa como concluída
@app.route('/complete/<int:id>')
def complete_task(id):
    con = connect_db()
    cur = con.cursor()
    cur.execute("UPDATE tasks SET completed = 1 WHERE id=?", (id,))
    con.commit()
    con.close()
    return redirect('/')

# funcao para chamar a main
if __name__ == "__main__":
    app.run(debug=True)