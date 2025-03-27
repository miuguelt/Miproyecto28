from flask_login import UserMixin
from app import db

class Espacio(db.Model): 
    __tablename__ = 'espacio'
    idEspacio = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.String(50), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
    activo = db.Column(db.Boolean, default=True)
    ubicación = db.Column(db.String(90), unique=True, nullable=False) #(piso, número de espacio)

    factura = db.relationship("Factura", back_populates = "espacio")