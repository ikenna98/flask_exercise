from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug import exceptions
import sqlite3

app = Flask(__name__)
CORS(app)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    return 'Welcome to our API. By Anisha, Ikenna and Sarushan'

# animes = [
#     {'id': 1, 'name': 'Bubble', 'year': 2022},
#     {'id': 2, 'name': 'Blackover', 'year': 2017},
#     {'id': 3, 'name': 'Blue Period', 'year': 2021}
# ]

@app.route('/anime', methods=['GET', 'POST'])
def anime():
    if request.method == 'GET':
        conn = get_db_connection()
        posts = conn.execute('SELECT * FROM animes').fetchall()
        conn.close()
        anime_list = []
        def render_stuff():
            for p in posts:
                anime_list.append({'id': p['id'], 'name': p['name'], 'year':p['year']})
        render_stuff()
        return jsonify(anime_list)  
    if request.method == 'POST':
        data = request.json
        # data['id'] = len(animes) + 1
        conn = get_db_connection()
        conn.execute("INSERT INTO animes (name, year) VALUES (?, ?)",
                        (data['name'], data['year']))
        conn.commit()
        conn.close()
        # animes.append(data)
        return f"{data['name']} has been added to the anime list!"

@app.errorhandler(exceptions.NotFound)
def handle__404(err):
    return jsonify({"message": f"Oops... {err}"}), 404

@app.errorhandler(exceptions.InternalServerError)
def handle_server_error(err):
    return jsonify({"message": f"{err}. It's not you, it's us. Press F to pay respects"}), 500

if __name__ == '__main__':
    app.run(debug=True)
