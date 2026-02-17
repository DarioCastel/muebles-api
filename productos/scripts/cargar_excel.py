import pandas as pd
from pathlib import Path

from productos.models import Producto, Categoria, ProductoImagen


def run():
    # 1. Ruta absoluta a este archivo
    base_dir = Path(__file__).resolve().parent
    excel_path = base_dir / "productos.xlsx"

    if not excel_path.exists():
        print(f"❌ No se encontró el Excel en: {excel_path}")
        return

    # 2. Leer Excel
    df = pd.read_excel(excel_path)

    print("📄 Columnas detectadas:", list(df.columns))
    print(f"📦 Filas encontradas: {len(df)}")

    for _, row in df.iterrows():
        nombre = str(row["nombre"]).strip()
        categoria_nombre = str(row["categoria"]).strip().lower()
        precio = row["precio"]

        descripcion = row.get("descripcion", "")
        largo = row.get("largo", "")
        alto = row.get("alto", "")
        profundidad = row.get("profundidad", "")
        peso = row.get("peso_kg", None)
        stock = bool(row.get("stock", True))

        # 3. Categoría
        categoria, _ = Categoria.objects.get_or_create(
            nombre=categoria_nombre,
            defaults={"slug": categoria_nombre.replace(" ", "-")}
        )

        # 4. Producto (evita duplicados)
        producto, creado = Producto.objects.get_or_create(
            nombre=nombre,
            defaults={
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

        # 5. Imágenes (columna: imagenes)
        imagenes_raw = row.get("imagenes", "")

        if isinstance(imagenes_raw, str) and imagenes_raw.strip():
            urls = [url.strip() for url in imagenes_raw.split("|") if url.strip()]

            # Evi
