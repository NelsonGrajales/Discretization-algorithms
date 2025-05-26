from flask import Flask, render_template

app = Flask (__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dda')
def dda():
    return render_template('dda.html')

@app.route('/breseham')
def breseham():
    return render_template('breseham.html')

@app.route('/circunferencia')
def circunferencia():
    return render_template('circunferencia.html')

@app.route('/elipse')
def elipse():
    return render_template('elipse.html')

@app.route('/presentacion')
def presentacion():
    return render_template('presentacion.html')


if __name__ == '__main__':
    app.run(debug=True)