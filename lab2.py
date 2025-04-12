from flask import Flask, render_template

app = Flask(__name__) # __name__ es para identificar donde esta el archivo principal

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/secret')
def secret():
    return render_template('secret.html')


if __name__ == '__main__':
    app.run(debug = True)
