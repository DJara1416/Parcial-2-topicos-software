from flask import Flask, render_template
from models import db, Flight
import math

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flights.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Ruta para la página principal
@app.route('/')
def home():
    return "<h1>Bienvenido a la aplicación de cálculo de factoriales y gestión de vuelos</h1>"

# Ruta para calcular el factorial de un número
@app.route('/factorial/<int:number>')
def factorial(number):
    try:
        result = math.factorial(number)
    except ValueError:
        result = "Número negativo, no se puede calcular el factorial."
    
    return render_template("factorial.html", number=number, result=result)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Crear tablas si no existen
    app.run(host='0.0.0.0', port=8000, debug=True)
