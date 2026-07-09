import os
from flask import Flask, render_template, request, redirect, url_for,session, flash
from flask_mysqldb import MySQL
import hashlib
#import mysql.connector
from werkzeug.utils import secure_filename
from functools import wraps

#El parámetro template folder, sirve para asignar el nombre de la carpeta de las plantillas...
#Por default el nombre de la carpeta es templates
#existen varios parametros para rutas como el static_folder etc... revisar documentación
app = Flask(__name__)
app.secret_key = 't1burones'
########DESARROLLO#######
app.config['MYSQL_HOST'] = 'srv521.hstgr.io'
app.config['MYSQL_USER'] = 'u695554080_maya_consola'
app.config['MYSQL_PASSWORD'] = 'wCQ@Z!c8@'
app.config['MYSQL_DB'] = 'u695554080_maya_consola'
mysql = MySQL(app)
########DESARROLLO#######

#######PRODUCCION#######
#mysql = mysql.connector.connect(
 # host="localhost",
 # user="root",
 # password="",
 # database="tienda"
#)
#######PRODUCCION#######
app.config['FOTOS'] = 'images'

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Verifica si el usuario no tiene la sesión activa
        if 'loggedin' not in session:
            flash('Por favor, inicia sesión para acceder a esta página.', 'warning')
            return redirect(url_for('fnLogin'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/salir')
def fnSalir():
    # Elimina los datos de la sesión
    session.pop('loggedin', None)
    session.pop('user', None)
    session.pop('cClave', None)
    # Redirige al login
    return redirect(url_for('fnLogin'))

@app.route("/")
def fnHome():
    return render_template("home.html")

@app.route("/login")
def fnLogin():
    return render_template("login.html")

@app.route("/valida-usuario",methods=['POST'])
def fnValidaUsuario():
    User      = request.form['user']
    Clave     = request.form['clave']
    Usuariomd5 = hashlib.md5(User.encode('utf-8')).hexdigest()
    Clavemd5 = hashlib.md5(Clave.encode('utf-8')).hexdigest()
    cur = mysql.connection.cursor()
    respuesta = ""
    # Consulta parametrizada (evita inyección SQL)
    cur.execute('SELECT cUser,cClave FROM usuario WHERE cUser = %s AND cClave = %s', (Usuariomd5,Clavemd5))
    account = cur.fetchone()
    cursor.close()
    if account:
        session['loggedin'] = True
        session['user'] = account[0]
        session['cClave'] = account[1]
        respuesta = "si"
    else:
        respuesta = "usuario incorrecto"
    return(respuesta)

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
    return render_template("usuarios.html", usuarios = data)

@app.route("/EditarUsuario/<id>")
def fnEditarUsuario(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM usuario WHERE idUsuario={0}".format(id))
    data = cur.fetchall()
    return render_template("editarusuario.html", usuario = data[0])

@app.route("/EditarUsuarioBD/<id>")
def fnEditarUsuarioBD(id):
    cur = mysql.connection.cursor()
    cur.execute("UPDATE usuario SET cNombres={0}, cApellidos={1}, cCorreo={2}, iEdad={3}, cDireccion={4}".format())

@app.route("/CancelarUsuario/<id>")
def fnCancelarUsuario(id):
    cur = mysql.connection.cursor()
    print(id)
    cur.execute("UPDATE usuario SET lActivo=0 WHERE idUsuario={0}".format(id))
    mysql.commit()
    return redirect(url_for('fnListaUsuarios'))

@app.route("/guarda_usuario/<int:id>", methods=['POST'])
def fnGuarda_usuario(id):
    if request.method == 'POST':
        Nombres     = request.form['Nombres']
        Apellidos   = request.form['Apellidos']
        Correo      = request.form['Correo']
        Edad        = request.form['Edad']
        Direccion   = request.form['Direccion']
        cur = mysql.connection.cursor()
        if id == 0:
            Foto        = request.files['Foto']
            filename    = secure_filename(Foto.filename)
            Foto.save(os.path.join(app.config['FOTOS'], filename))
            cur.execute('INSERT INTO usuario (cNombres,cApellidos,cCorreo,iEdad,cDireccion,cFoto) VALUES(%s,%s,%s,%s,%s,%s)', (Nombres,Apellidos,Correo,Edad,Direccion,filename))
        else:
            cur.execute('UPDATE usuario SET cNombres=%s, cApellidos=%s, cCorreo=%s, iEdad=%s, cDireccion=%s WHERE idUsuario=%s',(Nombres,Apellidos,Correo,Edad,Direccion,id))
        mysql.commit()
        return redirect(url_for('fnListaUsuarios'))

#if __name__ == "__main__":
    #app.run(debug=True, port=3000)
