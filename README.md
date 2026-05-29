```markdown
`🎮 PIXELVAULT – Marketplace de Llaves Digitales de Videojuegos`

**Proyecto:** PIXELVAULT  
**Temática:** Venta de videojuegos digitales  
**Base de datos relacional** con relaciones 1:N y N:M 
Nombre del profesor: JOSÉ CHRISTIAN ROMERO HERNANDEZ
**Equipo:** [Rojas Ortiz Austin Alberto                  
Gonzalez Balbuena Luz Elena
Martinez Urcino Jocelyn
Ventura Aguilar Ian Yafer 
Martinez Navarro Juan Jael
Avalos Garcia Carlos Uriel
]  4AVPG
**Fecha:** 25/05/2026  
**Repositorio:** [https://github.com/tu-usuario/PixelVault](https://github.com/tu-usuario/PixelVault)

---

### 📑 Indice`

1. [Introducción](#1-introducción)
2. [Desarrollo](#2-desarrollo)
   - 2.1 [Modelos de datos y relaciones](#21-modelos-de-datos-y-relaciones)
   - 2.2 [Diseño de la base de datos (diagrama ER)](#22-diseño-de-la-base-de-datos-diagrama-er)
   - 2.3 [CRUD a través del panel de administración](#23-crud-a-través-del-panel-de-administración)
   - 2.4 [Explicación de views.py y su interacción con urls y templates](#24-explicación-de-viewspy-y-su-interacción-con-urls-y-templates)
   - 2.5 [Configuración de settings.py](#25-configuración-de-settingspy)
3. [Conclusiones finales](#3-conclusiones-finales)

---

`1. Introduccion`Introducción

**PIXELVAULT** es una plataforma de comercio electrónico desarrollada con **Django** (Python) especializada en la venta de llaves digitales de videojuegos. El proyecto aplica los conceptos fundamentales de bases de datos relacionales en un entorno web real.

**Requisitos académicos cumplidos:**
- ✅ Mínimo **4 modelos** (tenemos 8: `Desarrolladora`, `Plataforma`, `Genero`, `Vendedor`, `Videojuego`, `Cliente`, `Venta`, `User`).
- ✅ **Relación uno a muchos (1:N)** – Ejemplo: una `Desarrolladora` → muchos `Videojuego`.
- ✅ **Relación muchos a muchos (N:M)** – Ejemplo: un `Videojuego` ↔ muchas `Plataforma`s.

**Funcionalidades implementadas:**
- Registro, inicio y cierre de sesión de usuarios.
- Catálogo de videojuegos con **buscador inteligente** (filtra por título, desarrolladora, género o plataforma).
- **Página de detalle** de cada juego con toda la información técnica.
- **Carrito de compras** (llamado "La Bóveda") con persistencia en sesión.
- Panel de **administración** personalizado para gestión completa de datos.

---

 `2. Desarrollo`

 `2.1 Modelos de datos y relaciones`

El archivo `catalogo/models.py` define las tablas de la base de datos. A continuación se explican los modelos principales:

#### a) `Desarrolladora`
```python
class Desarrolladora(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=50)
```
- **Relación 1:N** con `Videojuego` (una desarrolladora produce muchos juegos).

#### b) `Plataforma`
```python
class Plataforma(models.Model):
    nombre = models.CharField(max_length=50)
    fabricante = models.CharField(max_length=50)
```
- **Relación N:M** con `Videojuego` (un juego puede estar en varias plataformas).

#### c) `Genero`
```python
class Genero(models.Model):
    nombre = models.CharField(max_length=50)
```
- **Relación N:M** con `Videojuego` (un juego puede tener varios géneros).

#### d) `Vendedor`
```python
class Vendedor(models.Model):
    nombre = models.CharField(max_length=100)
    alias = models.CharField(max_length=50)
```
- **Relación 1:N** con `Videojuego` (un vendedor puede ofrecer muchos juegos).

#### e) `Videojuego` (modelo central)
```python
class Videojuego(models.Model):
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    anio = models.IntegerField()
    portada = models.ImageField(upload_to='portadas/')
    
    desarrolladora = models.ForeignKey(Desarrolladora, on_delete=models.CASCADE)  # 1:N
    vendedor = models.ForeignKey(Vendedor, on_delete=models.SET_NULL, null=True)  # 1:N
    plataformas = models.ManyToManyField(Plataforma)  # N:M
    generos = models.ManyToManyField(Genero)          # N:M
```

#### f) `Cliente` y `Venta`
```python
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    direccion = models.TextField()

class Venta(models.Model):
    videojuego = models.ForeignKey(Videojuego, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_compra = models.DateField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
```
- **Relación 1:N** entre `Cliente` y `Venta` (un cliente puede tener muchas ventas).

**Resumen de relaciones:**

| Entidad origen | Relación | Entidad destino |
|----------------|----------|------------------|
| Desarrolladora | 1 → N    | Videojuego       |
| Vendedor       | 1 → N    | Videojuego       |
| Cliente        | 1 → N    | Venta            |
| Videojuego     | N → M    | Plataforma       |
| Videojuego     | N → M    | Genero           |

---

### 2.2 Diseño de la base de datos (diagrama ER)

```
┌─────────────┐        ┌─────────────┐        ┌─────────────┐
│Desarrolladora│ 1    N │ Videojuego  │ N    M │  Plataforma │
│  - nombre    │───────→│  - titulo   │←──────→│  - nombre   │
│  - pais      │        │  - precio   │        │ - fabricante│
└─────────────┘        │  - anio     │        └─────────────┘
                       │  - portada  │
┌─────────────┐        └─────────────┘        ┌─────────────┐
│  Vendedor   │ 1          ↑                  │   Genero    │
│  - nombre   │────────────┘ N                │  - nombre   │
│  - alias    │           M                   └─────────────┘
└─────────────┘           │
                          │
                    ┌─────┴─────┐
                    │   Venta   │
                    │  - fecha  │
                    │  - total  │
                    └───────────┘
                          │ N
                          │
                    ┌─────┴─────┐
                    │  Cliente  │
                    │  - nombre │
                    │  - email  │
                    └───────────┘
```

**Explicación:**  
- Las flechas sólidas representan relaciones **1:N**.  
- Las flechas punteadas bidireccionales representan relaciones **N:M**.

---

### 2.3 CRUD a través del panel de administración

El archivo `catalogo/admin.py` personaliza la interfaz de administración de Django.

```python
from django.contrib import admin
from .models import Desarrolladora, Plataforma, Genero, Vendedor, Videojuego, Cliente, Venta

class VideojuegoAdmin(admin.ModelAdmin):
    filter_horizontal = ('plataformas', 'generos')   # Facilita selección N:M
    list_display = ('titulo', 'precio', 'anio', 'vendedor')
    search_fields = ('titulo',)

admin.site.register(Videojuego, VideojuegoAdmin)
admin.site.register(Desarrolladora)
admin.site.register(Plataforma)
admin.site.register(Genero)
admin.site.register(Vendedor)
admin.site.register(Cliente)
admin.site.register(Venta)
```

**Operaciones CRUD:**

| Operación | Cómo se realiza en el admin |
|-----------|------------------------------|
| **Crear** | Botón "Agregar" → llenar formulario → Guardar. |
| **Leer**  | Listado de registros; se puede buscar. |
| **Actualizar** | Entrar al registro, modificar campos, Guardar. |
| **Eliminar** | Seleccionar el registro y elegir "Eliminar". |

**Ejemplo con relaciones N:M:**  
Al crear un `Videojuego`, el campo `plataformas` muestra dos columnas con flechas. Para asignar una plataforma, se selecciona de la columna izquierda y se presiona la flecha `→` para moverla a la columna derecha ("Elegidos"). Esto garantiza que la relación muchos a muchos quede correctamente guardada.

---

### 2.4 Explicación de views.py y su interacción con urls y templates

#### a) Archivo `catalogo/urls.py` – Rutas
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('juego/<int:juego_id>/', views.detalle_juego, name='detalle_juego'),
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('agregar/<int:juego_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('registro/', views.registro, name='registro'),
]
```
- Cada URL llama a una función de `views.py`.

#### b) Archivo `catalogo/views.py` – Lógica de negocio
```python
from django.shortcuts import render, get_object_or_404
from .models import Videojuego

def detalle_juego(request, juego_id):
    juego = get_object_or_404(
        Videojuego.objects.select_related('desarrolladora', 'vendedor')
                         .prefetch_related('plataformas', 'generos'),
        pk=juego_id
    )
    return render(request, 'catalogo/detalle_juego.html', {'juego': juego})
```
- `select_related` optimiza la carga de relaciones **1:N** (desarrolladora, vendedor) en una sola consulta SQL.  
- `prefetch_related` prepara las relaciones **N:M** (plataformas, géneros) para evitar múltiples consultas al recorrerlas en el template.  
- `render` combina el template con el objeto `juego` y devuelve el HTML.

#### c) Template `catalogo/templates/catalogo/detalle_juego.html` – Presentación
```html
<h1>{{ juego.titulo }}</h1>
<p>Precio: ${{ juego.precio }}</p>

<div>
    <strong>Plataformas:</strong>
    {% for plataforma in juego.plataformas.all %}
        {{ plataforma.nombre }}{% if not forloop.last %}, {% endif %}
    {% empty %}
        Sin plataforma
    {% endfor %}
</div>
```
- El bucle `for` recorre la lista de plataformas (relación N:M) y muestra cada nombre separado por comas.

**Flujo completo:**  
1. Usuario hace clic en un juego desde el catálogo.  
2. El navegador pide `http://.../juego/5/`.  
3. Django ejecuta `detalle_juego` con `juego_id=5`.  
4. La vista obtiene el juego y todas sus relaciones.  
5. Renderiza el template y envía el HTML al navegador.  
6. El usuario ve la ficha técnica del juego.

---

### 2.5 Configuración de settings.py

El archivo `config/settings.py` contiene la configuración global:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'catalogo',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

LANGUAGE_CODE = 'es-mx'
TIME_ZONE = 'America/Mexico_City'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

**Importancia de cada línea:**  
- `'catalogo'` registra la app.  
- `MEDIA_ROOT` permite subir portadas de juegos.  
- `LOGIN_REDIRECT_URL` evita errores después de iniciar sesión.  
- `LANGUAGE_CODE = 'es-mx'` traduce el admin al español.

---

## 3. Conclusiones finales

El proyecto **PIXELVAULT** cumple satisfactoriamente todos los requisitos:

1. **Modelado relacional completo** – 8 modelos interconectados con relaciones 1:N (Desarrolladora→Videojuego, Vendedor→Videojuego, Cliente→Venta) y N:M (Videojuego↔Plataforma, Videojuego↔Genero).

2. **CRUD funcional desde el admin** – Creación, lectura, actualización y eliminación de datos, con soporte visual para relaciones N:M mediante `filter_horizontal`.

3. **Correcta interacción entre capas** – Las URLs envían peticiones a las vistas, que optimizan consultas con `select_related`/`prefetch_related` y pasan datos a los templates, los cuales recorren las relaciones N:M con bucles `for`.

4. **Funcionalidades extra** – Autenticación de usuarios, buscador inteligente, carrito de compras basado en sesiones, y diseño responsivo con estética gamer (neón oscuro).

**En resumen**, PIXELVAULT no solo demuestra el dominio de bases de datos relacionales en Django, sino que se aproxima a un producto real listo para escalar (pasarela de pago, API REST, etc.). El equipo ha aprendido a aplicar conceptos teóricos en un entorno web completo y funcional.

---

## 🔧 Instalación y ejecución

```bash
git clone https://github.com/tu-usuario/PixelVault.git
cd PixelVault
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install django
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Accede a:  
- Tienda: http://127.0.0.1:8000/  
- Panel admin: http://127.0.0.1:8000/admin/

---

```