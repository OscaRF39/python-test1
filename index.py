from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

#El parámetro template folder, sirve para asignar el nombre de la carpeta de las plantillas...
#Por default el nombre de la carpeta es templates
#existen varios parametros para rutas como el static_folder etc... revisar documentación
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'tienda'
mysql = MySQL(app)

@app.route("/")
def fnHome():
    return render_template("home.html")

@app.route("/agregar_usuario")
def fnAgregarUsuario():
    return render_template("agregar_usuario.html")

@app.route("/usuarios")
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
    mysql.connection.commit()
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
            cur.execute('INSERT INTO usuario (cNombres,cApellidos,cCorreo,iEdad,cDireccion) VALUES(%s,%s,%s,%s,%s)', (Nombres,Apellidos,Correo,Edad,Direccion))
        else:
            cur.execute('UPDATE usuario SET cNombres=%s, cApellidos=%s, cCorreo=%s, iEdad=%s, cDireccion=%s WHERE idUsuario=%s',(Nombres,Apellidos,Correo,Edad,Direccion,id))
        mysql.connection.commit()
        return redirect(url_for('fnListaUsuarios'))

if __name__ == "__main__":
    app.run(debug=True)