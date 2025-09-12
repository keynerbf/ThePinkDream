from flask import Flask, render_template, request, redirect, url_for, session, flash
from config import conectar

import psycopg2

app = Flask(__name__)
app.secret_key = "clave_segura"

@app.route("/THE_PINK_DREAM")
def index():
    return render_template("index.html")

@app.route("/THE_PINK_DREAM/registro", methods=["GET","POST"])
def registrar():
    if request.method=="POST":
        documento=request.form["documento"]
        nombre_completo=request.form["nombre_completo"]
        email=request.form["email"]
        contraseña=request.form["contraseña"]
        try:
            conexion=conectar()
            cursor=conexion.cursor()
            consulta= "INSERT INTO registro (id, nombre_completo, email, contraseña) VALUES (%s, %s, %s, %s);"
            datos=(documento, nombre_completo, email, contraseña)
            cursor.execute(consulta, datos)
            conexion.commit()
            print("Usuario registrado exitosamente")
            return """
            <script>
                alert('✅ El usuario fue registrado con éxito!');
                setTimeout(function() {
                    window.location.href = '/THE_PINK_DREAM';
                }, 1000);
            </script>
            """
        except (Exception, psycopg2.Error) as error:
            print("Error al registrar el usuario:", error)
            return ("Error al registrar el usuario")
    return render_template("registro.html")


@app.route("/THE_PINK_DREAM/iniciar_sesion", methods=["GET", "POST"])
def iniciar_sesion():
    if request.method == "POST":
        documento = request.form["documento"]
        contraseña = request.form["contraseña"]

        try:
            conn = conectar()
            cur = conn.cursor()
            cur.execute(
                "SELECT id, nombre_completo FROM registro WHERE id=%s AND contraseña=%s", 
                (documento, contraseña)
            )
            usuario = cur.fetchone()
            cur.close()
            conn.close()

            if usuario:
                session["usuario"] = usuario[0]   # documento
                session["nombre"] = usuario[1]    # nombre
                if "carrito" not in session:
                    session["carrito"] = []       # inicializar carrito vacío
                return redirect(url_for("index"))  # <-- ahora dentro del if
            else:
                return """
                <script>
                    alert('❌ Documento o contraseña incorrectos');
                    window.location.href = '/THE_PINK_DREAM/iniciar_sesion';
                </script>
                """
        except Exception as e:
            return f"""
            <script>
                alert('⚠️ Error en inicio de sesión: {e}');
                window.location.href = '/THE_PINK_DREAM/iniciar_sesion';
            </script>
            """
    return render_template("iniciar_sesion.html")



@app.route("/THE_PINK_DREAM/catalogo")
def catalogo():
    productos = {
        1: {"id": 1, "nombre": "Ramo de Girasoles", "precio": 25000, "imagen": "/static/girasoles_1.jpg"},
        2: {"id": 2, "nombre": "Ramo de Tulipanes", "precio": 35000, "imagen": "/static/tulipanes_1.jpg"},
        3: {"id": 3, "nombre": "Ramo Mixto (Oferta)", "precio": 20000, "imagen": "/static/mixto.jpg"},
        4: {"id": 4, "nombre": "Ramo de Rosas (Oferta)", "precio": 25000, "imagen": "/static/oferta_rosas.jpg"},
        5: {"id": 5, "nombre": "Ramo Pequeño (Oferta)", "precio": 10000, "imagen": "/static/ramo_2.webp"},
        6: {"id": 6, "nombre": "Ramo de Rosas Rojas", "precio": 40000, "imagen": "/static/rojo.jpg"},
        7: {"id": 7, "nombre": "Ramo Mixto Colorido", "precio": 35000, "imagen": "/static/color_mixto.jpg"},
        8: {"id": 8, "nombre": "Ramo de Margaritas Blancas", "precio": 20000, "imagen": "/static/blancas_margaritas.jpg"},
        9: {"id": 9, "nombre": "Ramo de Tulipanes", "precio": 30000, "imagen": "/static/tulipanes_2.jpg"},
        10: {"id": 10, "nombre": "Ramo de Lirios Elegantes", "precio": 50000, "imagen": "/static/lirios.jpg"},
        11: {"id": 11, "nombre": "Ramo de Girasoles", "precio": 25000, "imagen": "/static/girasoles_2.jpg"},
        12: {"id": 12, "nombre": "Ramo de Orquídeas Exóticas", "precio": 60000, "imagen": "/static/orquideas.jpg"},
        13: {"id": 13, "nombre": "Ramo de Rosas Blancas", "precio": 45000, "imagen": "/static/blancas.jpg"},
        14: {"id": 14, "nombre": "Ramo Elegante con Rosas", "precio": 50000, "imagen": "/static/rosas_1.jpg"},
        15: {"id": 15, "nombre": "Ramo Clásico de Margaritas", "precio": 30000, "imagen": "/static/margaritas_1.jpg"},
    }
    return render_template("catalogo.html", productos=productos)

@app.route("/THE_PINK_DREAM/ramo/<int:ramo_id>")
def ramo(ramo_id):
    productos = {
    1: {"id": 1, "nombre": "Ramo de Girasoles", "precio": 25000, "imagen": "/static/girasoles_1.jpg"},
    2: {"id": 2, "nombre": "Ramo de Tulipanes", "precio": 35000, "imagen": "/static/tulipanes_1.jpg"},
    3: {"id": 3, "nombre": "Ramo Mixto (Oferta)", "precio": 20000, "imagen": "/static/mixto.jpg"},
    4: {"id": 4, "nombre": "Ramo de Rosas (Oferta)", "precio": 25000, "imagen": "/static/oferta_rosas.jpg"},
    5: {"id": 5, "nombre": "Ramo Pequeño (Oferta)", "precio": 10000, "imagen": "/static/ramo_2.webp"},
    6: {"id": 6, "nombre": "Ramo de Rosas Rojas", "precio": 40000, "imagen": "/static/rojo.jpg"},
    7: {"id": 7, "nombre": "Ramo Mixto Colorido", "precio": 35000, "imagen": "/static/color_mixto.jpg"},
    8: {"id": 8, "nombre": "Ramo de Margaritas Blancas", "precio": 20000, "imagen": "/static/blancas_margaritas.jpg"},
    9: {"id": 9, "nombre": "Ramo de Tulipanes", "precio": 30000, "imagen": "/static/tulipanes_2.jpg"},
    10: {"id": 10, "nombre": "Ramo de Lirios Elegantes", "precio": 50000, "imagen": "/static/lirios.jpg"},
    11: {"id": 11, "nombre": "Ramo de Girasoles", "precio": 25000, "imagen": "/static/girasoles_2.jpg"},
    12: {"id": 12, "nombre": "Ramo de Orquídeas Exóticas", "precio": 60000, "imagen": "/static/orquideas.jpg"},
    13: {"id": 13, "nombre": "Ramo de Rosas Blancas", "precio": 45000, "imagen": "/static/blancas.jpg"},
    14: {"id": 14, "nombre": "Ramo Elegante con Rosas", "precio": 50000, "imagen": "/static/rosas_1.jpg"},
    15: {"id": 15, "nombre": "Ramo Clásico de Margaritas", "precio": 30000, "imagen": "/static/margaritas_1.jpg"}
}
    ramo = productos.get(ramo_id)
    return render_template("ramo.html", ramo=ramo)


@app.route("/THE_PINK_DREAM/perfil")
def perfil():
    if "usuario" not in session:
        flash("⚠️ Debes iniciar sesión para acceder a tu perfil", "error")
        return redirect(url_for("iniciar_sesion"))
    return render_template("perfil.html")

@app.route("/THE_PINK_DREAM/modificar_nombre", methods=["POST"])
def modificar_nombre():
    if "usuario" not in session:
        return redirect(url_for("iniciar_sesion"))

    nuevo_nombre = request.form["nombre"]
    usuario_id = session["usuario"]

    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute("UPDATE registro SET nombre_completo=%s WHERE id=%s", (nuevo_nombre, usuario_id))
        conn.commit()
        cur.close()
        conn.close()

        session["nombre"] = nuevo_nombre  # actualizar en sesión también
        flash("✅ Nombre actualizado correctamente", "success")
    except Exception as e:
        flash(f"⚠️ Error al actualizar el nombre: {e}", "error")

    return redirect(url_for("perfil"))

@app.route("/THE_PINK_DREAM/modificar_contraseña", methods=["POST"])
def modificar_contraseña():
    if "usuario" not in session:
        return redirect(url_for("iniciar_sesion"))

    nueva_contraseña = request.form["nueva_contraseña"]
    usuario_id = session["usuario"]

    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute("UPDATE registro SET contraseña=%s WHERE id=%s", (nueva_contraseña, usuario_id))
        conn.commit()
        cur.close()
        conn.close()

        flash("✅ Contraseña actualizada correctamente", "success")
    except Exception as e:
        flash(f"⚠️ Error al actualizar la contraseña: {e}", "error")

    return redirect(url_for("perfil"))

@app.route("/THE_PINK_DREAM/eliminar_usuario", methods=["POST"])
def eliminar_usuario():
    if "usuario" not in session:
        return redirect(url_for("iniciar_sesion"))

    usuario_id = session["usuario"]

    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute("DELETE FROM registro WHERE id=%s", (usuario_id,))
        conn.commit()
        cur.close()
        conn.close()

        # cerrar sesión al eliminar
        session.clear()
        flash("🗑️ Usuario eliminado correctamente", "success")
    except Exception as e:
        flash(f"⚠️ Error al eliminar el usuario: {e}", "error")

    return redirect(url_for("index"))

# ---------------- CARRITO ----------------
@app.route("/THE_PINK_DREAM/agregar_carrito/<int:ramo_id>")
def agregar_carrito(ramo_id):
    if "carrito" not in session:
        session["carrito"] = []
        
    productos = {
    1: {"id": 1, "nombre": "Ramo de Girasoles", "precio": 25000, "imagen": "/static/girasoles_1.jpg"},
    2: {"id": 2, "nombre": "Ramo de Tulipanes", "precio": 35000, "imagen": "/static/tulipanes_1.jpg"},
    3: {"id": 3, "nombre": "Ramo Mixto (Oferta)", "precio": 20000, "imagen": "/static/mixto.jpg"},
    4: {"id": 4, "nombre": "Ramo de Rosas (Oferta)", "precio": 25000, "imagen": "/static/oferta_rosas.jpg"},
    5: {"id": 5, "nombre": "Ramo Pequeño (Oferta)", "precio": 10000, "imagen": "/static/ramo_2.webp"},
    6: {"id": 6, "nombre": "Ramo de Rosas Rojas", "precio": 40000, "imagen": "/static/rojo.jpg"},
    7: {"id": 7, "nombre": "Ramo Mixto Colorido", "precio": 35000, "imagen": "/static/color_mixto.jpg"},
    8: {"id": 8, "nombre": "Ramo de Margaritas Blancas", "precio": 20000, "imagen": "/static/blancas_margaritas.jpg"},
    9: {"id": 9, "nombre": "Ramo de Tulipanes", "precio": 30000, "imagen": "/static/tulipanes_2.jpg"},
    10: {"id": 10, "nombre": "Ramo de Lirios Elegantes", "precio": 50000, "imagen": "/static/lirios.jpg"},
    11: {"id": 11, "nombre": "Ramo de Girasoles", "precio": 25000, "imagen": "/static/girasoles_2.jpg"},
    12: {"id": 12, "nombre": "Ramo de Orquídeas Exóticas", "precio": 60000, "imagen": "/static/orquideas.jpg"},
    13: {"id": 13, "nombre": "Ramo de Rosas Blancas", "precio": 45000, "imagen": "/static/blancas.jpg"},
    14: {"id": 14, "nombre": "Ramo Elegante con Rosas", "precio": 50000, "imagen": "/static/rosas_1.jpg"},
    15: {"id": 15, "nombre": "Ramo Clásico de Margaritas", "precio": 30000, "imagen": "/static/margaritas_1.jpg"}
}

    session["carrito"].append(productos[ramo_id])
    session.modified = True
    return redirect(url_for("catalogo"))

@app.route("/THE_PINK_DREAM/carrito")
def carrito():
    if "usuario" not in session:
        flash("⚠️ Debes iniciar sesión para acceder al carrito", "error")
        return redirect(url_for("iniciar_sesion"))
    
    carrito = session.get("carrito", [])
    total = sum(item["precio"] for item in carrito)
    return render_template("carrito.html", carrito=carrito, total=total)

@app.route("/THE_PINK_DREAM/eliminar_carrito/<int:index>")
def eliminar_carrito(index):
    carrito = session.get("carrito", [])
    if 0 <= index < len(carrito):
        carrito.pop(index)
        session["carrito"] = carrito
        session.modified = True
    return redirect(url_for("carrito"))


@app.route("/THE_PINK_DREAM/finalizar_compra", methods=["POST"])
def finalizar_compra():
    if "usuario" not in session:
        return """
        <script>
            alert('⚠️ Debes iniciar sesión para finalizar la compra');
            window.location.href = '/THE_PINK_DREAM/iniciar_sesion';
        </script>
        """

    direccion = request.form.get("direccion")
    metodo_pago = request.form.get("pago")
    num_pago = request.form.get("num_pago")
    usuario_id = session.get("usuario")   # documento del usuario logueado
    carrito = session.get("carrito", [])

    if not carrito:
        return """
        <script>
            alert('⚠️ Tu carrito está vacío');
            window.location.href = '/THE_PINK_DREAM/catalogo';
        </script>
        """

    # Pasar lista de productos a texto
    productos_texto = ", ".join([item["nombre"] for item in carrito])

    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO pedidos (usuario_id, direccion, metodo_pago, num_metodo_pago, productos)
            VALUES (%s, %s, %s, %s, %s)
            """, (usuario_id, direccion, metodo_pago, num_pago, productos_texto))

        conn.commit()
        cur.close()
        conn.close()

        # limpiar carrito
        session.pop("carrito", None)

        return """
        <script>
            alert('✅ Compra finalizada con éxito');
            window.location.href = '/THE_PINK_DREAM';
        </script>
        """

    except Exception as e:
        print("Error al registrar el pago:", e)
        return f"""
        <script>
            alert('⚠️ Error al registrar el pago: {e}');
            window.history.back();
        </script>
        """
    
@app.route("/THE_PINK_DREAM/cerrar_sesion")
def cerrar_sesion():
    session.pop("usuario", None)
    session.pop("nombre", None)
    flash("🔒 Sesión cerrada correctamente", "success")
    return redirect(url_for("index"))

if __name__=='__main__':
    app.run(debug=True)
