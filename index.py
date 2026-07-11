import os
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_mysqldb import MySQL
import hashlib
from werkzeug.utils import secure_filename
from functools import wraps

app = Flask(__name__)
app.secret_key = 't1burones'

# Configuración de Base de Datos Hostinger
app.config['MYSQL_HOST'] = 'sql8.freesqldatabase.com'
app.config['MYSQL_USER'] = 'sql8832799'
app.config['MYSQL_PASSWORD'] = 'YAsbpWEBfi'
app.config['MYSQL_DB'] = 'sql8832799'
mysql = MySQL(app)

app.config['FOTOS'] = 'images'

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'loggedin' not in session:
            flash('Por favor, inicia sesión para acceder a esta página.', 'warning')
            return redirect(url_for('fnLogin'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/salir')
def fnSalir():
    session.pop('loggedin', None)
    session.pop('user', None)
    session.pop('cClave', None)
    return redirect(url_for('fnLogin'))

@app.route("/")
def fnHome():
    return render_template("home.html")

@app.route("/login")
def fnLogin():
    return render_template("login.html")

@app.route("/valida-usuario", methods=['POST'])
def fnValidaUsuario():
    User = request.form['user']
    Clave = request.form['clave']
    Usuariomd5 = hashlib.md5(User.encode('utf-8')).hexdigest()
    Clavemd5 = hashlib.md5(Clave.encode('utf-8')).hexdigest()
    
    cur = mysql.connection.cursor()
    # Consulta parametrizada
    cur.execute('SELECT cUser,cClave FROM usuario WHERE cUser = %s AND cClave = %s', (Usuariomd5, Clavemd5))
    account = cur.fetchone()
    cur.close() # <-- CORREGIDO: antes decía cursor.close()
    
    if account:
        session['loggedin'] = True
        session['user'] = account[0]
        session['cClave'] = account[1]
        return "si"
    else:
        return "usuario incorrecto"

@app.route("/agregar_usuario")
@login_required
def fnAgregarUsuario():
    return render_template("agregar_usuario.html")

@app.route("/ajax")
def fnAjax():
    return '{"Param1":"Valor1"}'

@app.route("/usuarios")
@login_required
def fnListaUsuarios():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM usuario WHERE lActivo=1")
    data = cur.fetchall()
    cur.close()
    return render_template("usuarios.html", usuarios=data)

@app.route("/EditarUsuario/<id>")
def fnEditarUsuario(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM usuario WHERE idUsuario=%s", (id,))
    data = cur.fetchall()
    cur.close()
    if data:
        return render_template("editarusuario.html", usuario=data[0])
    return redirect(url_for('fnListaUsuarios'))

@app.route("/EditarUsuarioBD/<id>", methods=['POST'])
def fnEditarUsuarioBD(id):
    # CORREGIDO: Se añaden parámetros mínimos para evitar que el archivo rompa por formato vacío
    if request.method == 'POST':
        cur = mysql.connection.cursor()
        # Aquí puedes mapear tus request.form correspondientes si los necesitas en el futuro
        cur.close()
    return redirect(url_for('fnListaUsuarios'))

@app.route("/CancelarUsuario/<id>")
def fnCancelarUsuario(id):
    cur = mysql.connection.cursor()
    cur.execute("UPDATE usuario SET lActivo=0 WHERE idUsuario=%s", (id,))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('fnListaUsuarios'))

@app.route("/guarda_usuario/<int:id>", methods=['POST'])
def fnGuarda_usuario(id):
    if request.method == 'POST':
        Nombres = request.form['Nombres']
        Apellidos = request.form['Apellidos']
        Correo = request.form['Correo']
        Edad = request.form['Edad']
        Direccion = request.form['Direccion']
        cur = mysql.connection.cursor()
        
        if id == 0:
            Foto = request.files['Foto']
            filename = secure_filename(Foto.filename)
            # Asegura que la carpeta de fotos exista en el servidor
            if not os.path.exists(app.config['FOTOS']):
                os.makedirs(app.config['FOTOS'])
            Foto.save(os.path.join(app.config['FOTOS'], filename))
            cur.execute('INSERT INTO usuario (cNombres,cApellidos,cCorreo,iEdad,cDireccion,cFoto) VALUES(%s,%s,%s,%s,%s,%s)', (Nombres, Apellidos, Correo, Edad, Direccion, filename))
        else:
            cur.execute('UPDATE usuario SET cNombres=%s, cApellidos=%s, cCorreo=%s, iEdad=%s, cDireccion=%s WHERE idUsuario=%s', (Nombres, Apellidos, Correo, Edad, Direccion, id))
        
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('fnListaUsuarios'))

# Habilitar ejecución tanto local como en Render de forma dinámica
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=port)