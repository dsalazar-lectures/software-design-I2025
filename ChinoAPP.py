from flask import Flask, render_template

# Crear una instanvia de flask
app = Flask(__name__)

# Definir la URL raiz 
@app.route('/')
# Funcion que se ejecuta al entrar a la URL
def home():
    return render_template("index.html")

@app.route('/grade')
def grade():
    return render_template("grade.html")

# Ejecutar la app solo si el archivo se ejecuta directamente
if __name__ == '__main__':
    # Ayuda durante el desarrollo
    app.run(debug=True)