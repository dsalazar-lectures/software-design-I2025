# Importar la clase Flask para crear una aplicación flask.
from flask import Flask, render_template

# Instancia de la clase flask, pasando por parámetro el archivo actual,
# necesario para encontrar otros archivos.
app = Flask(__name__)

# Cuando se visita la raíz del sitio web se ejecuta la función 
@app.route("/")
def show_student_info():
  return render_template("estudiante.html")

# Corre el servidor localmente con el debugger activado
if __name__ == '__main__':
  app.run(debug=True)
