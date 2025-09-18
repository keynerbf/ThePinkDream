from config import conectar

productos_base = {
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

productos_ofertas = {
    3: {"id": 3, "nombre": "Ramo Mixto (Oferta)", "precio": 20000, "imagen": "/static/mixto.jpg"},
    4: {"id": 4, "nombre": "Ramo de Rosas (Oferta)", "precio": 25000, "imagen": "/static/oferta_rosas.jpg"},
    5: {"id": 5, "nombre": "Ramo Pequeño (Oferta)", "precio": 10000, "imagen": "/static/ramo_2.webp"},
}

productos_nuevos = {
    1: {"id": 1, "nombre": "Ramo de Girasoles", "precio": 25000, "imagen": "/static/girasoles_1.jpg"},
    2: {"id": 2, "nombre": "Ramo de Tulipanes", "precio": 35000, "imagen": "/static/tulipanes_1.jpg"},
}

# Conexión
conn = conectar()
cur = conn.cursor()

# Migrar base
for p in productos_base.values():
    cur.execute("""
        INSERT INTO productos_base (nombre, descripcion, precio, imagen)
        VALUES (%s, %s, %s, %s)
    """, (p["nombre"], None, p["precio"], p["imagen"]))

# Migrar ofertas
for p in productos_ofertas.values():
    cur.execute("""
        INSERT INTO productos_ofertas (nombre, descripcion, precio, imagen, descuento)
        VALUES (%s, %s, %s, %s, %s)
    """, (p["nombre"], None, p["precio"], p["imagen"], 0))

# Migrar nuevos
for p in productos_nuevos.values():
    cur.execute("""
        INSERT INTO productos_nuevos (nombre, descripcion, precio, imagen)
        VALUES (%s, %s, %s, %s)
    """, (p["nombre"], None, p["precio"], p["imagen"]))

conn.commit()
cur.close()
conn.close()
