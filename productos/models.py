from django.db import models


class Categoria(models.Model):
    id = models.SlugField(primary_key=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    id = models.SlugField(primary_key=True)
    nombre = models.CharField(max_length=200)

    # lo vas a usar más adelante → perfecto
    slug = models.SlugField(unique=True, blank=True, null=True)

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name='productos'
    )

    descripcion = models.TextField()
    precio = models.PositiveIntegerField()

    largo = models.FloatField()
    alto = models.FloatField()
    profundidad = models.FloatField()

    peso_kg = models.FloatField()
    stock = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class ProductoImagen(models.Model):
    producto = models.ForeignKey(
        Producto,
        related_name='imagenes',
        on_delete=models.CASCADE
    )

    imagen_url = models.URLField()

    def __str__(self):
        return f"Imagen de {self.producto.nombre}"


class Combo(models.Model):
    id = models.SlugField(primary_key=True)
    nombre = models.CharField(max_length=200)

    slug = models.SlugField(unique=True, blank=True, null=True)

    ahorro_porcentaje = models.PositiveIntegerField()
    precio_total = models.PositiveIntegerField()
    descripcion_promo = models.TextField()

    productos = models.ManyToManyField(Producto)

    def __str__(self):
        return self.nombre
