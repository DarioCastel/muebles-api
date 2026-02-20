import os
import sys
from pathlib import Path
import pandas as pd

# =========================
# BOOTSTRAP DJANGO
# =========================
BASE_DIR = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(BASE_DIR))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")  # ⚠️ cambiá si tu settings se llaman distinto

import django
django.setup()

# =========================
# IMPORTS DJANGO
# =========================
from productos.models import Producto, Categoria, ProductoImagen


def run():
    # =========================
    # RUTA EXCEL
    # =========================
    excel_path = Path(__file__).resolve().parent / "productos.xlsx"

    if not excel_path.exists():
        print(f"❌ No se encontró el Excel en: {excel_path}")
        return

    # =========================
    # LEER EXCEL
    # =========================
    df = pd.read_excel(excel_path)

    print("📄 Columnas:", list(df.columns))
    print(f"📦 Filas: {len(df)}")

    for _, row in df.iterrows():
        # =========================
        # DATOS BÁSICOS
        # =========================
        producto_id = str(row["id"]).strip()
        nombre = str(row["nombre"]).strip()
        slug = str(row.get("slug") or producto_id).strip()

        categoria_nombre = str(row["categoria"]).strip().lower()
        precio = int(row["precio"])

        descripcion = row.get("descripcion", "")
        largo = row.get("largo", 0)
        alto = row.get("alto", 0)
        profundidad = row.get("profundidad", 0)
        peso = row.get("peso_kg", None)
        stock = bool(row.get("stock", True))

        # =========================
        # CATEGORIA
        # =========================
        categoria, _ = Categoria.objects.get_or_create(
            id=categoria_nombre.replace(" ", "-"),
            defaults={"nombre": categoria_nombre}
        )

        # =========================
        # PRODUCTO (PK = ID)
        # =========================
        producto, creado = Producto.objects.update_or_create(
    id=row["id"],
    defaults={
        "nombre": nombre,
        "slug": row.get("slug", row["id"]),
        "categoria": categoria,
        "descripcion": descripcion,
        "precio": precio,
        "largo": largo,
        "alto": alto,
        "profundidad": profundidad,
        "peso_kg": peso,
        "stock": stock,
    }
)

        if creado:
            print(f"✅ Producto creado: {nombre}")
        else:
            print(f"⚠️ Producto ya existía: {nombre}")

        # =========================
        # IMÁGENES
        # =========================
        imagenes_raw = row.get("imagenes") or row.get("imágenes")

        if isinstance(imagenes_raw, str) and imagenes_raw.strip():
            urls = [u.strip() for u in imagenes_raw.split("|") if u.strip()]

            for url in urls:
                ProductoImagen.objects.get_or_create(
                    producto=producto,
                    imagen_url=url
                )

    print("🎉 Carga finalizada sin errores")