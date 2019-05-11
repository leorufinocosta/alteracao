from flask import Flask, render_template, request, redirect, url_for
from flaskext.mysql import MySQL
from bd import *

app = Flask(__name__)
mysql = MySQL()
mysql.init_app(app)

config(app)

@app.route('/')
def index():
    conn, cursor = get_db(mysql)
    contatos = get_contatos(cursor)
    cursor.close()
    conn.close()
    return render_template('index.html', contatos=contatos)

@app.route('/alterar/<idcontatos>')
def alterar(idcontatos):
    conn, cursor = get_db(mysql)
    contato = get_contato(cursor, idcontatos)

    cursor.close()
    conn.close()

    return render_template('alterar.html', contato=contato)

@app.route('/salvar_alteracao', methods=['POST'])
def salvar_alteracao():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        idcontatos = request.form.get('idcontatos')

        conn, cursor = get_db(mysql)

        update_contato(conn, cursor, nome, email, idcontatos)

        cursor.close()
        conn.close()

        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)