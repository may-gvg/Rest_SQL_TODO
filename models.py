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
        cur.execute(f"SELECT * FROM todo")
        rows = cur.fetchall()
        todos = []
        for [no, title, description, done] in rows:
            if done == 0:
                done = False
            else:
                done = True
            todos.append({'id': no, 'title': title, 'description': description, 'done': done})
        # self.todos = todos
        return todos

    def get(self, id):
        cur = self.db.cursor()
        cur.execute(f"SELECT * FROM todo WHERE id = ?", (id,))
        row = cur.fetchone()
        todo = {'id': row[0], 'title': row[1], 'description': row[2], 'done': row[3]}
        return todo

    def create(self, data, id):
        sql = 'INSERT INTO todo (id, title, description, done) values(?, ?, ?, ?)'
        cur = self.db.cursor()
        cur.execute(sql, (id, data['title'], data['description'], data['done']))
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
        return True

    def new_id(self):
        cur = self.db.cursor()
        cur.execute(f"SELECT max(id)  FROM todo")
        row = cur.fetchone()
        newid = 1
        if row[0] is not None:
            newid = row[0] + 1
        return newid


todos = Todos()

if __name__ == '__main__':
    app.run(debug=True)
