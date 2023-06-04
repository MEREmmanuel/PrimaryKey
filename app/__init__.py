from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect
from config import Config
from config import DevelopmentConfig
from .models.ModeloEstacionamiento import ModeloEstacionamiento
from .models.entities.Usuario import Usuario
from .models.ModeloUsuario import ModeloUsuario
from flask_login import LoginManager, login_user, logout_user, login_required
from .consts import *

app = Flask(__name__)

app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect(app)
app.config.from_object(Config)
db = MySQL(app)
login_manager_app = LoginManager(app)


@login_manager_app.user_loader
def load_user(id):
    return ModeloUsuario.obtener_por_id(db, id)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=('GET', 'POST'))
def login():
    # CSRF (SOLICITUD DE FALSIFICACION ENTRE SITIOS)
    if request.method == 'POST':
        """print(request.form['usuario'])
        print(request.form['password'])"""
        usuario = Usuario(
            None, request.form['usuario'], request.form['password'], None)
        usuario_logeado = ModeloUsuario.login(db, usuario)
        if usuario_logeado != None:
            login_user(usuario_logeado)
            flash(BIENVENIDA,'success')
            return redirect(url_for('index'))
        else:
            flash(LOGIN_CREDENCIALES_INVALIDAS, 'warning')
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')

@app.route('/logout')
def logout():
    logout_user()
    flash(LOGOUT_CORRECTO, 'success')
    return redirect(url_for('index'))

@app.route('/estacionamientos')
@login_required
def listar_estacionamientos():
    try:
        estacionamientos = ModeloEstacionamiento.listar_estacionamientos(db)
        data = {
            'estacionamientos': estacionamientos
        }
        return render_template('listado_estacionamientos.html', data=data)
    except Exception as ex:
        print(ex)


def pagina_no_encontrada(error):
    return render_template('errores/404.html'), 404

def pagina_no_autorizada(error):
    return redirect(url_for('login'))


app.register_error_handler(404, pagina_no_encontrada)
app.register_error_handler(401, pagina_no_autorizada)

def inicializar_app(config):
    app.config.from_object(config)
    csrf.init_app(app)
    return app