from flask import Flask, request, render_template, redirect, url_for
import sqlite3
import os

app = Flask(__name__)

def conectar_db():
    dir_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_db = os.path.join(dir_actual, 'DB.db')
    return sqlite3.connect(ruta_db)

@app.route('/')
def index():
    # Consolidamos la info de todos los sectores aquí
    sectores = {
        'alimenticio': {
            'nombre': 'Insumo Alimenticio',
            'prediccion': 'Aumento de demanda del 15% en granos básicos.',
            'insight': 'Se recomienda aumentar inventario de maíz y sorgo antes de junio.',
            'labels': ["Ene", "Feb", "Mar", "Abr", "May", "Jun"],
            'valores': [120, 150, 140, 180, 210, 250]
        },
        'turismo': {
            'nombre': 'Turismo Gto',
            'prediccion': 'Crecimiento del 20% en ocupación hotelera.',
            'insight': 'Fortalecer campañas digitales para el Festival Cervantino.',
            'labels': ["Ene", "Feb", "Mar", "Abr", "May", "Jun"],
            'valores': [80, 95, 110, 130, 150, 190]
        },
        'agro': {
            'nombre': 'Agroindustria',
            'prediccion': 'Estabilidad en exportaciones de berries.',
            'insight': 'Invertir en sistemas de riego automatizado por sequía.',
            'labels': ["Ene", "Feb", "Mar", "Abr", "May", "Jun"],
            'valores': [200, 190, 210, 205, 220, 230]
        }
    }
    return render_template('home.html', sectores=sectores)

@app.route('/registrar_usuario', methods=['POST'])
def registrar_usuario():
    nombre = request.form.get('nombre')
    correo = request.form.get('correo')
    telefono = request.form.get('telefono')
    try:
        conn = conectar_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Usuario (Nombre, Correo, Numero) VALUES (?, ?, ?)", 
                       (nombre, correo, telefono))
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Error: {e}")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)