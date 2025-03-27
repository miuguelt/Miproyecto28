from flask_login import UserMixin
from app import db

class Clientes(db.Model, UserMixin):
    __tablename__ = 'cliente'
    idCliente = db.Column(db.Integer, primary_key=True)
    namecli = db.Column(db.String(90), nullable=False)
    passworduser = db.Column(db.String(300), nullable=False)
    correo = db.Column(db.String(90), nullable=True)
    imgper = db.Column(db.String(300), nullable=True)
    tipousu = db.Column(db.Integer, nullable=True)
    
    reserva = db.relationship("Reserva", back_populates = "cliente")
    motos = db.relationship("Motos", back_populates = "cliente") 
    autos = db.relationship("Autos", back_populates = "cliente") 
   
    def get_id(self):
        return str(self.idCliente)
    
    def get_img(self, img_attr):
        return getattr(self, img_attr) if getattr(self, img_attr) else "imagenes/usuario.png"
    
    def get_img2(self):
        """Retorna la imagen de perfil del usuario o una imagen por defecto."""
        return f"imagenes/{self.imgper}" if self.imgper else "imagenes/casco1.webp"# esta linea faltaba en este codigo
   