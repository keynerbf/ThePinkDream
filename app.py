from flask import Flask, render_template, request, redirect, url_for, session, flash
from config import conectar
import psycopg2
import psycopg2.extras
from functools import wraps

app = Flask(__name__)
app.secret_key = "clave_segura"

# ----------------- HELPERS -----------------
def get_current_user():
    usuario = session.get("usuario")
    if not usuario:
        return None
    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute("SELECT rol FROM registro WHERE id = %s", (usuario,))
        row = cur.fetchone()
        cur.close()
        conn.close()
        rol = row[0] if row else "usuario"
        return {"id": usuario, "rol": rol}
    except:
        return {"id": usuario, "rol": "usuario"}

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        usuario = get_current_user()
        if not usuario or usuario['rol'] != 'admin':
            flash("⚠️ Solo administradores pueden acceder", "error")
            return redirect(url_for("index"))
        return f(*args, **kwargs)
    return decorated_function

# ----------------- INICIO -----------------
@app.route("/THE_PINK_DREAM")
def index():
    return render_template("index.html")

# ----------------- REGISTRO -----------------
@app.route("/THE_PINK_DREAM/registro", methods=["GET", "POST"])
def registrar():
    if request.method == "POST":
        documento = request.form["documento"]
        nombre_completo = request.form["nombre_completo"]
        email = request.form["email"]
        contraseña = request.form["contraseña"]
        rol = 'usuario'
        try:
            conn = conectar()
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO registro (id, nombre_completo, email, contraseña, rol) VALUES (%s, %s, %s, %s, %s)",
                (documento, nombre_completo, email, contraseña, rol),
            )
            conn.commit()
            cur.close()
            conn.close()
            flash("✅ Usuario registrado con éxito", "success")
            return redirect(url_for("iniciar_sesion"))
        except Exception as e:
            flash(f"⚠️ Error al registrar: {e}", "error")
    return render_template("registro.html")

# ----------------- LOGIN -----------------
@app.route("/THE_PINK_DREAM/iniciar_sesion", methods=["GET", "POST"])
def iniciar_sesion():
    if request.method == "POST":
        documento = request.form["documento"]
        contraseña = request.form["contraseña"]

        try:
            conn = conectar()
            cur = conn.cursor()
            cur.execute(
                "SELECT id, nombre_completo, rol FROM registro WHERE id=%s AND contraseña=%s",
                (documento, contraseña),
            )
            usuario = cur.fetchone()
            cur.close()
            conn.close()

            if usuario:
                session["usuario"] = usuario[0]   # documento
                session["nombre"] = usuario[1]    # nombre
                session["rol"] = usuario[2]       # rol: 'admin' o 'usuario'
                session.setdefault("carrito", [])
                return redirect(url_for("index"))
            else:
                return """
                <script>
                    alert('❌ Documento o contraseña incorrectos');
                    window.location.href = '/THE_PINK_DREAM/iniciar_sesion';
                </script>
                """
        except Exception as e:
            return f"Error en inicio de sesión: {e}"

    return render_template("iniciar_sesion.html")

# ----------------- CERRAR SESIÓN -----------------
@app.route("/THE_PINK_DREAM/cerrar_sesion")
def cerrar_sesion():
    session.clear()
    flash("🔒 Sesión cerrada correctamente", "success")
    return redirect(url_for("index"))

# ----------------- PERFIL -----------------
@app.route("/THE_PINK_DREAM/perfil")
def perfil():
    if "usuario" not in session:
        flash("⚠️ Debes iniciar sesión para acceder al perfil", "error")
        return redirect(url_for("iniciar_sesion"))
    return render_template("perfil.html")

# ----------------- CARRITO -----------------
@app.route("/THE_PINK_DREAM/agregar_carrito/<int:ramo_id>")
def agregar_carrito(ramo_id):
    if "carrito" not in session:
        session["carrito"] = []
    conn = conectar()
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    producto = None
    for tabla in ["productos_base", "productos_ofertas", "productos_nuevos"]:
        cur.execute(f"SELECT * FROM {tabla} WHERE id=%s", (ramo_id,))
        producto = cur.fetchone()
        if producto:
            break
    cur.close()
    conn.close()
    if producto:
        session["carrito"].append(dict(producto))
        session.modified = True
    return redirect(url_for("catalogo"))

@app.route("/THE_PINK_DREAM/carrito")
def carrito():
    if "usuario" not in session:
        flash("⚠️ Debes iniciar sesión para acceder al carrito", "error")
        return redirect(url_for("iniciar_sesion"))
    carrito = session.get("carrito", [])
    total = sum(float(item["precio"]) for item in carrito)
    return render_template("carrito.html", carrito=carrito, total=total)

@app.route("/THE_PINK_DREAM/eliminar_carrito/<int:index>")
def eliminar_carrito(index):
    carrito = session.get("carrito", [])
    if 0 <= index < len(carrito):
        carrito.pop(index)
        session.modified = True
    return redirect(url_for("carrito"))

@app.route("/THE_PINK_DREAM/finalizar_compra", methods=["POST"])
def finalizar_compra():
    if "usuario" not in session:
        flash("⚠️ Debes iniciar sesión", "error")
        return redirect(url_for("iniciar_sesion"))
    carrito = session.get("carrito", [])
    if not carrito:
        flash("⚠️ Carrito vacío", "error")
        return redirect(url_for("catalogo"))
    direccion = request.form.get("direccion")
    metodo_pago = request.form.get("pago")
    num_pago = request.form.get("num_pago")
    productos_texto = ", ".join([item["nombre"] for item in carrito])
    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO pedidos (usuario_id, direccion, metodo_pago, num_metodo_pago, productos) VALUES (%s,%s,%s,%s,%s)",
            (session["usuario"], direccion, metodo_pago, num_pago, productos_texto),
        )
        conn.commit()
        cur.close()
        conn.close()
        session.pop("carrito")
        flash("✅ Compra finalizada con éxito", "success")
    except Exception as e:
        flash(f"⚠️ Error al registrar compra: {e}", "error")
    return redirect(url_for("index"))

# ----------------- CATALOGO -----------------
@app.route("/THE_PINK_DREAM/catalogo")
def catalogo():
    conn = conectar()
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("SELECT * FROM productos_base")
    base = cur.fetchall()
    cur.execute("SELECT * FROM productos_ofertas")
    ofertas = cur.fetchall()
    cur.execute("SELECT * FROM productos_nuevos")
    nuevos = cur.fetchall()
    cur.close()
    conn.close()
    return render_template("catalogo.html", base=base, ofertas=ofertas, nuevos=nuevos)

# ----------------- RAMO -----------------
@app.route("/THE_PINK_DREAM/ramo/<int:ramo_id>")
def ramo(ramo_id):
    conn = conectar()
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    producto = None
    for tabla in ["productos_base", "productos_ofertas", "productos_nuevos"]:
        cur.execute(f"SELECT * FROM {tabla} WHERE id=%s", (ramo_id,))
        producto = cur.fetchone()
        if producto:
            break
    cur.close()
    conn.close()
    if not producto:
        return "❌ Ramo no encontrado", 404
    return render_template("ramo.html", ramo=producto)

# ----------------- ADMIN PRODUCTOS -----------------
@app.route("/THE_PINK_DREAM/admin/productos")
@admin_required
def admin_productos():
    conn = conectar()
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("SELECT * FROM productos_base")
    base = cur.fetchall()
    cur.execute("SELECT * FROM productos_ofertas")
    ofertas = cur.fetchall()
    cur.execute("SELECT * FROM productos_nuevos")
    nuevos = cur.fetchall()
    cur.close()
    conn.close()
    return render_template("admin_productos.html", base=base, ofertas=ofertas, nuevos=nuevos)

@app.route("/THE_PINK_DREAM/admin/agregar_producto", methods=["GET","POST"])
@admin_required
def agregar_producto():
    if request.method=="POST":
        nombre=request.form["nombre"]
        descripcion=request.form["descripcion"]
        precio=float(request.form["precio"])
        imagen=request.form["imagen"]
        categoria=request.form["categoria"]
        tabla={"base":"productos_base","ofertas":"productos_ofertas","nuevos":"productos_nuevos"}.get(categoria,"productos_base")
        try:
            conn=conectar()
            cur=conn.cursor()
            if tabla=="productos_ofertas":
                descuento=float(request.form.get("descuento",0))
                cur.execute(f"INSERT INTO {tabla} (nombre, descripcion, precio, imagen, descuento) VALUES (%s,%s,%s,%s,%s)",
                    (nombre, descripcion, precio, imagen, descuento))
            else:
                cur.execute(f"INSERT INTO {tabla} (nombre, descripcion, precio, imagen) VALUES (%s,%s,%s,%s)",
                    (nombre, descripcion, precio, imagen))
            conn.commit()
            cur.close()
            conn.close()
            flash("✅ Producto agregado", "success")
        except Exception as e:
            flash(f"⚠️ Error: {e}", "error")
        return redirect(url_for("admin_productos"))
    return render_template("admin_agregar_producto.html")

@app.route("/THE_PINK_DREAM/admin/eliminar_producto/<categoria>/<int:id>")
@admin_required
def eliminar_producto(categoria,id):
    tabla={"base":"productos_base","ofertas":"productos_ofertas","nuevos":"productos_nuevos"}.get(categoria,"productos_base")
    try:
        conn=conectar()
        cur=conn.cursor()
        cur.execute(f"DELETE FROM {tabla} WHERE id=%s",(id,))
        conn.commit()
        cur.close()
        conn.close()
        flash("🗑️ Producto eliminado", "success")
    except Exception as e:
        flash(f"⚠️ Error: {e}", "error")
    return redirect(url_for("admin_productos"))

@app.route("/THE_PINK_DREAM/admin/editar_producto/<categoria>/<int:id>", methods=["GET","POST"])
@admin_required
def editar_producto(categoria,id):
    tabla={"base":"productos_base","ofertas":"productos_ofertas","nuevos":"productos_nuevos"}.get(categoria,"productos_base")
    conn=conectar()
    cur=conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method=="POST":
        nombre=request.form["nombre"]
        descripcion=request.form["descripcion"]
        precio=float(request.form["precio"])
        imagen=request.form["imagen"]
        try:
            if tabla=="productos_ofertas":
                descuento=float(request.form.get("descuento",0))
                cur.execute(f"UPDATE {tabla} SET nombre=%s, descripcion=%s, precio=%s, imagen=%s, descuento=%s WHERE id=%s",
                    (nombre, descripcion, precio, imagen, descuento, id))
            else:
                cur.execute(f"UPDATE {tabla} SET nombre=%s, descripcion=%s, precio=%s, imagen=%s WHERE id=%s",
                    (nombre, descripcion, precio, imagen, id))
            conn.commit()
            flash("✅ Producto actualizado", "success")
        except Exception as e:
            flash(f"⚠️ Error: {e}", "error")
        finally:
            cur.close()
            conn.close()
        return redirect(url_for("admin_productos"))
    cur.execute(f"SELECT * FROM {tabla} WHERE id=%s",(id,))
    producto=cur.fetchone()
    cur.close()
    conn.close()
    return render_template("admin_editar_producto.html", producto=producto, categoria=categoria)

# ----------------- ADMIN USUARIOS -----------------
@app.route("/THE_PINK_DREAM/admin/usuarios")
@admin_required
def admin_usuarios():
    conn=conectar()
    cur=conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("SELECT id, nombre_completo, email, rol FROM registro")
    usuarios=cur.fetchall()
    cur.close()
    conn.close()
    return render_template("admin_usuarios.html", usuarios=usuarios)

@app.route("/THE_PINK_DREAM/admin/eliminar_usuario/<int:id>")
@admin_required
def admin_eliminar_usuario(id):
    try:
        conn=conectar()
        cur=conn.cursor()
        cur.execute("DELETE FROM registro WHERE id=%s",(id,))
        conn.commit()
        cur.close()
        conn.close()
        flash("🗑️ Usuario eliminado", "success")
    except Exception as e:
        flash(f"⚠️ Error: {e}", "error")
    return redirect(url_for("admin_usuarios"))

@app.route("/THE_PINK_DREAM/admin/editar_usuario/<int:id>", methods=["GET","POST"])
@admin_required
def admin_editar_usuario(id):
    conn=conectar()
    cur=conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method=="POST":
        nombre=request.form["nombre"]
        email=request.form["email"]
        rol=request.form["rol"]
        try:
            cur.execute("UPDATE registro SET nombre_completo=%s, email=%s, rol=%s WHERE id=%s",
                (nombre,email,rol,id))
            conn.commit()
            flash("✅ Usuario actualizado", "success")
        except Exception as e:
            flash(f"⚠️ Error: {e}", "error")
        finally:
            cur.close()
            conn.close()
        return redirect(url_for("admin_usuarios"))
    cur.execute("SELECT id, nombre_completo, email, rol FROM registro WHERE id=%s",(id,))
    usuario=cur.fetchone()
    cur.close()
    conn.close()
    return render_template("admin_editar_usuario.html", usuario=usuario)

# ----------------- MAIN -----------------
if __name__=="__main__":
    app.run(debug=True)
