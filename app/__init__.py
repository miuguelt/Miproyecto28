from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

db = SQLAlchemy()

login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.urandom(24)
    app.config.from_object('config.Config')
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'login.login.html'

    @login_manager.user_loader
    def load_user(idCliente):
        from .models.Clientes import Clientes
        return Clientes.query.get(int(idCliente))

    from app.routes import auth,autos_routes,motos_routes,reserva_routes,espacio_routes
    app.register_blueprint(auth.bp)
    app.register_blueprint(autos_routes.bp)
    app.register_blueprint(motos_routes.bp)
    app.register_blueprint(reserva_routes.bp)
    app.register_blueprint(espacio_routes.bp)


     #app.register_blueprint(facturas_route.bp)
    return app 