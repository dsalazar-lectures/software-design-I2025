from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.5/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-SgOJa3DmI69IUzQ2PVdRZhwQ+dy64/BUtbMJw1MZ8t5HZApcHrRKUc4W0kG879m7" crossorigin="anonymous">
</head>
<body>
    <div class="container mt-4">
        <p>Estudiante: Jose. Esta es mi versión esqueleto del proyecto!</p>
        <a class="btn btn-primary">Hola asistente</a>
    </div>
    
</body>
</html>"""