import json

from flask import Flask

import sqlite3
from flask import g

DATABASE = "baza.db"

app = Flask(__name__)


# na tyle ile umiałem, nie do końca jeszcze kumam z wyciągnięciem kursora z bloku,
# nie wiem czy dobrze ale połączyło mi się udało mi się dla delete
# update mi wyrzuca błąd konfliktu od dwóch obiektów
# prowadź Sensei proszę ;)

#pzdr


class Todos:


    def __init__(self):
        self.db = sqlite3.connect(DATABASE)

#w co mam opakować dalsą cześć bloku ?

        self.cur = self.db.cursor()
        self.cur.execute(f"SELECT * FROM todo")
        rows = self.cur.fetchall()
        todos = {}
        for [no, title, description, done] in rows:
            todos[no] = {'id': no, 'title': title, 'description': description, 'done': done}
        self.todos = todos

    def all(self):
        lista = []
        for key in self.todos:
            lista.append(self.todos[key])
        return lista

    def get(self, id):
        return self.todos.get(id)

    def create(self, data, id):
        data['id'] = id
        self.todos[id] = data

    def update(self, id, data):
        #data.pop('csrf_token')
        self.todos[id] = data
        sql = 'UPDATE todo set title = ?, description = ?, done = ? WHERE id = ?'
        cur = self.db.cursor()
        cur.execute(sql, (data['title'], data['description'], data['done'], id))
        self.db.commit()

    def delete(self, id):
        todo = self.get(id)
        if todo:
            sql = 'DELETE FROM todo WHERE id = ?'
            self.cur.execute(sql, (id,))
            self.db.commit()
            return True
        return False

    def new_id(self):
        keys = self.todos.keys()
        if keys:
             m = max(keys)
        else:
            return 1
        return m + 1

todos = Todos()

if __name__ == '__main__':
    app.run()