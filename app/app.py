from flask import Flask, render_template,request
from algorithm import dda_algorithm, brhm,elip,cir

app = Flask (__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dda', methods = ['POST','GET'])
def dda():
    resultado = []
    if request.method == 'POST':
        x1 = int(request.form['x1'])
        y1 = int(request.form['y1'])
        x2 = int(request.form['x2'])
        y2 = int(request.form['y2'])
        
        resultado = dda_algorithm(x1,y1,x2,y2)
        return render_template('dda.html',puntos=resultado,x1=x1,y1=y1,x2=x2,y2=y2)
    else:
        return render_template('dda.html',puntos=[])

@app.route('/breseham',methods = ['POST','GET'])
def breseham():
    resultado = []
    if request.method == 'POST':
        x1 = int(request.form['x1'])
        y1 = int(request.form['y1'])
        x2 = int(request.form['x2'])
        y2 = int(request.form['y2'])
        
        resultado = brhm(x1,y1,x2,y2)
        return render_template('breseham.html',puntos=resultado,x1=x1,y1=y1,x2=x2,y2=y2)
    else:
        return render_template('breseham.html')

@app.route('/circunferencia',methods = ['POST','GET'])
def circunferencia():
    resultado = []
    if request.method == 'POST':
        x1 = int(request.form['xc'])
        y1 = int(request.form['yc'])
        r = int(request.form['r'])
        
        resultado = cir(x1,y1,r)
        print(resultado)
        return render_template('circunferencia.html',puntos=resultado,x1=x1,y1=y1,r=r)
    else:
        return render_template('circunferencia.html')

@app.route('/elipse',methods = ['POST','GET'])
def elipse():
    resultado = []
    if request.method == 'POST':
        x1 = int(request.form['xc'])
        y1 = int(request.form['yc'])
        x2 = int(request.form['rx'])
        y2 = int(request.form['ry'])
        resultado = elip(x2,y2,x1,x2)
        return render_template('elipse.html',puntos=resultado,x1=x1,y1=y1,x2=x2,y2=y2)
    else:
        return render_template('elipse.html', puntos=[], x1=0, y1=0, x2=0, y2=0)


@app.route('/presentacion')
def presentacion():
    return render_template('presentacion.html')


if __name__ == '__main__':
    app.run(debug=True)