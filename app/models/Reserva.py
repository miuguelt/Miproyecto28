from flask_login import UserMixin
from app import db

class Reserva(db.Model, UserMixin): 
    __tablename__ = 'reserva'
    idReserva = db.Column(db.Integer, primary_key=True)
    ubicación = db.Column(db.String(90), unique=True, nullable=False) #(piso, número de espacio)
    estado = db.Column(db.String(90), nullable=False) #(disponible, ocupado)
    fecha_creacion = db.Column(db.DateTime, default=db.func.now())
    idCliente = db.Column(db.Integer, db.ForeignKey('cliente.idCliente'))

    cliente = db.relationship("Clientes", back_populates = "reserva")
    factura = db.relationship("Factura", back_populates = "reserva")