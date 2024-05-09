from flask import Flask,request,render_template,url_for
from werkzeug.utils import redirect
from werkzeug.exceptions import abort

app = Flask(__name__)

#http://localhost:5000/

app.secret_key = 'my_clave_secreta'

@app.route('/')
def inicio():
    if 'username' in session:
        return f'el usuario ya ha hecho login{session['username']}'
    #app.logger.debug('Mensaje a nivel debug')
    app.logger.info(f'Entramos al path => {request.path}')
    #app.logger.warn('Mensaje de nivel warning')
    #app.logger.error('Mensaje a niver de error')
    app.logger.info('no ha hecho login ')
    return 'no ha hecho login'

@app.route('/login',method=['GET','POST'])
def login():
    if request.method == 'POST':
        #omitimo las validaciones de usuario y password
        usuario = request.form['username']
        session['username'] = usuario
        return redirect(url_for('inicio'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username')
    return redirect(url_for('inicio'))
#tipo de variable string
@app.route('/saludar/<nombre>')
def saludar(nombre):
    return f'saludos {nombre.upper()}'
#
@app.route('/edad/<int:edad>')
def mostar_edad(edad):
    return f'tu edad es {edad + 1 }'
#

@app.route('/mostrar/<nombre>',methods=['GET','POST'])
def mostar_nombre(nombre):
    return f'tu nombre es {nombre}'

#
@app.route('/mostrar/<nombre>',methods=['GET','POST'])
def mostar_nombre_vista(nombre):
    return render_template('mostar.html',nombre_llave=nombre)

@app.route('/redireccionar')
def redireccionar():
    return redirect(url_for('inicio'))
#
#manejo de errores
@app.route('/salir')
def salir():
    return abort(404)

@app.errorhandler(404)
def pagina_no_enconrada(error):
    return render_template('error404.html', error=error),404

@app.route('/api/mostar/<nombre>')
def retur_app_json(nombre):
    valores = {'nombre':nombre, 'metodo_http': request.method }
    return jsonify(valores)

