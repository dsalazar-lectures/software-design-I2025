from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
    return "Estudiante:Isacc Z. Esta es mi versión esqueleto del proyecto!"

if __name__=='__main__':
    app.run()
