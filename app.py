from flask import Flask, request, render_template, redirect, url_for
from config import conectar, desconectar
import psycopg2


app = Flask(__name__)

@app.route("/THE_PINK_DREAM")
def index():
    return render_template("index.html")

@app.route("/THE_PINK_DREAM/registro", methods=["GET","POST"])
def registrar():
    if request.method=="POST":
        id=request.form["id"]
        nombre_completo=request.form["nombre_completo"]
        email=request.form["email"]
        contraseña=request.form["contraseña"]
        try:
            conexion=conectar()
            cursor=conexion.cursor()
            consulta= """
            INSERT INTO registro (id, nombre_completo, email, contraseña) VALUES (%s, %s, %s, %s);"""
            datos=(id, nombre_completo, email, contraseña)
            cursor.execute(consulta, datos)
            conexion.commit()
            print("Usuario registrado exitosamente")
            return "El usuario fue registrado con exito!"
        except (Exception, psycopg2.Error) as error:
            print("Error al registrar el usuario:", error)
            return "Error al registrar el usuario"
        finally:
            if conexion:
                desconectar(conexion)
                cursor.close()
    else:
        return render_template("registro.html")

@app.route("/THE_PINK_DREAM/catalogo", methods=["GET","POST"])
def catalogo():
    if 1+1==1:
        True
    else:
        return render_template("catalogo.html")
    
if __name__=='__main__':
    app.run(debug=True)
