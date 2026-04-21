from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'huiadshgfa5ds5f'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        nueva_cita = {
            'nombre': request.form.get('nombre'),
            'telefono': request.form.get('telefono'),
            'mascota': request.form.get('mascota'),
            'servicio': request.form.get('servicio'),
            'email': request.form.get('email'),
            'mensaje': request.form.get('mensaje')
        }

        if 'lista_citas' not in session:
            session['lista_citas'] = []
        citas = session['lista_citas']
        citas.append(nueva_cita)
        session['lista_citas'] = citas
        return redirect(url_for('ver_tabla'))

@app.route('/tabla')
def ver_tabla():
    citas = session.get('lista_citas', [])
    return render_template('tabla.html', citas=citas)

@app.route('/limpiar')
def limpiar():
    session.pop('lista_citas', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)