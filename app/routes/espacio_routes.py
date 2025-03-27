from flask import Blueprint, render_template, request, redirect, url_for 
from app.models.Espacio import Espacio
from app.models.Clientes import Clientes
from app import db

bp = Blueprint('espacio', __name__)

# Ruta principal que muestra todos los espacios
@bp.route('/espacio')
def index():
    espacios = Espacio.query.all()  # Consultamos todos los espacios
    return render_template('espacio/index.html', data=espacios)

# Ruta para agregar un nuevo espacio
@bp.route('/espacio/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        numero = request.form['numero']
        descripcion = request.form['descripcion']
        ubicacion = request.form['ubicacion']
        activo = 'activo' in request.form  # Verificamos si está marcado como activo
        
        new_espacio = Espacio(numero=numero, descripcion=descripcion, Ubicación=ubicacion, activo=activo)
        db.session.add(new_espacio)
        db.session.commit()
        
        return redirect(url_for('espacio.index'))

    return render_template('espacio/add.html')


# Ruta para editar un espacio existente
@bp.route('/espacio/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    espacio = Espacio.query.get_or_404(id)  # Obtenemos el espacio por ID

    if request.method == 'POST':
        espacio.numero = request.form['numero']
        espacio.descripcion = request.form['descripcion']
        espacio.Ubicación = request.form['ubicacion']
        espacio.activo = 'activo' in request.form  # Actualizamos el estado de activo
        db.session.commit()

        return redirect(url_for('espacio.index'))

    return render_template('espacio/edit.html', espacio=espacio)

# Ruta para eliminar un espacio
@bp.route('/espacio/delete/<int:id>', methods=['GET'])
def delete(id):
    espacio = Espacio.query.get_or_404(id)
    db.session.delete(espacio)
    db.session.commit()

    return redirect(url_for('espacio.index'))

# Ruta para listar los espacios de un cliente (si aplica)
@bp.route('/espacio/list/<int:id>', methods=['GET', 'POST'])
def list_espacios(id):
    cliente = Clientes.query.get_or_404(id) 
    espacios = cliente.espacios 
    return render_template('espacio/list.html', cliente=cliente, espacios=espacios)
