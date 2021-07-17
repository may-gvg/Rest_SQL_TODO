import sqlite3

from flask import Flask

DATABASE = "baza.db"
app = Flask(__name__)


class Todos:

    def __init__(self):
        self.connect()

    def connect(self):
        self.db = sqlite3.connect(DATABASE, check_same_thread=False)

    def all(self):
        cur = self.db.cursor()
        cur.execute('SELECT * FROM todo')
        rows = cur.fetchall()
        todos = []
        for [no, title, description, done] in rows:
            done = bool(done)
            todos.append({'id': no, 'title': title, 'description': description, 'done': done})
        # self.todos = todos
        return todos

    def get(self, id):
        cur = self.db.cursor()
        cur.execute('SELECT * FROM todo WHERE id = ?', (id,))
        id, title, description, done = cur.fetchone()
        todo = {'id': id, 'title': title, 'description': description, 'done': bool(done)}
        return todo

    def create(self, data):
        sql = 'INSERT INTO todo (title, description, done) values(?, ?, ?)'
        cur = self.db.cursor()
        cur.execute(sql, (data['title'], data['description'], data['done']))
        self.db.commit()

    def update(self, id, data):
        # data.pop('csrf_token')
        sql = 'UPDATE todo set title = ?, description = ?, done = ? WHERE id = ?'
        cur = self.db.cursor()
        cur.execute(sql, (data['title'], data['description'], data['done'], id))
        self.db.commit()

    def delete(self, id):
        sql = 'DELETE FROM todo WHERE id = ?'
        self.cur.execute(sql, (id,))
        self.db.commit()

todos = Todos()

if __name__ == '__main__':
    app.run(debug=True)
