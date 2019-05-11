def config(app):
    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
    app.config['MYSQL_DATABASE_DB'] = 'contatos'

def get_db(mysql):
    conn = mysql.connect()
    cursor = conn.cursor()

    return conn, cursor

def get_contatos(cursor):
    # Executar o SQL
    cursor.execute(f'SELECT idcontatos, nome, email FROM contatos')

    # Recuperando o retorno do BD
    contatos = cursor.fetchall()

    # Retornar os dados
    return contatos

def get_contato(cursor, idcontatos):
    # Executar o SQL
    cursor.execute(f'SELECT idcontatos, nome, email FROM contatos where idcontatos = {idcontatos}')

    # Recuperando o retorno do BD
    contato = cursor.fetchone()

    # Retornar os dados
    return contato

def update_contato(conn, cursor, nome, email, idcontatos):
    cursor.execute(f'update contatos set nome = {nome}, email = {email}  where idcontatos = {idcontatos}')
    conn.commit()