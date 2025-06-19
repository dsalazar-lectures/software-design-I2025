from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permite conexión desde React

@app.route("/enviar", methods=["POST"])
def enviar():
    data = request.get_json()
    nombre = data.get("nombre", "").strip()
    if not nombre:
        return jsonify({"error": "Nombre vacío"}), 400
    return jsonify({"mensaje": "Formulario enviado correctamente"}), 200

if __name__ == "__main__":
    app.run(debug=True)