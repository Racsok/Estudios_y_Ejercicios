from flask import jsonify, Flask, request, flash
from flask_sqlalchemy import SQLAlchemy


def create_app(environmet="dev"):
    app = Flask(__name__)
    return app

app = create_app()

# Configuración de la base de datos SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///base_.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy()
db.init_app(app)

# Definir el modelo de la base de datos
class Personaje(db.Model):
    __tablename__ = 'Personaje'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    edad = db.Column(db.Integer , nullable=False)
    clase = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {"id": self.id, "nombre": self.nombre, "edad": self.edad, "clase": self.clase}


# Ruta para obtener todos los usuarios
@app.route('/Personajes', methods=['GET'])
def obtener_persoanjes():
    personajes = Personaje.query.all()
    return jsonify([personaje.to_dict() for personaje in personajes])

# Ruta para agregar un usuario
@app.route('/crear_personaje', methods=['POST'])
def agregar_persoanje():
    data = request.get_json()
    error = None
    if not data['nombre'] or not data['edad'] or not data['clase']:
        error = 'Se necesitan todos los parametros'
        
    if error is not None:
        flash(error)
    else:
        nuevo_personaje = Personaje(nombre=data['nombre'], edad=data['edad'], clase=data['clase'])
        db.session.add(nuevo_personaje)
        db.session.commit()
        return jsonify(nuevo_personaje.to_dict()), 201
    return jsonify({"error": error}), 400
        
# Iniciar el servidor
if __name__ == '__main__':
    app.run(debug=True)
