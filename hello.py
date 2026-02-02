from flask import Flask, render_template, request
import db_module  # <--- Importamos el archivo que acabamos de crear

app = Flask(__name__)

@app.route("/getmail", methods=['GET', 'POST'])
def getmail():
    resultado = None
    error = None
    
    if request.method == 'POST':
        nombre = request.form.get('usuario')
        # Llamamos a la función del otro archivo
        mail = db_module.buscar_mail(nombre)
        
        if mail:
            resultado = f"El mail de {nombre} es: {mail}"
        else:
            error = f"No s'ha trobat cap usuari anomenat '{nombre}'."
            
    return render_template('getmail.html', resultado=resultado, error=error)

@app.route("/addmail", methods=['GET', 'POST'])
def addmail():
    mensaje = None
    
    if request.method == 'POST':
        nombre = request.form.get('usuario')
        mail = request.form.get('mails')
        
        # Intentamos guardar usando el módulo
        if db_module.insertar_usuario(nombre, mail):
            mensaje = "Usuari registrat correctament a la Base de Dades!"
        else:
            mensaje = "Error: No s'ha pogut guardar (potser ja existeix?)."
            
    return render_template('addmail.html', mensaje=mensaje)

if __name__ == "__main__":
    app.run(debug=True)