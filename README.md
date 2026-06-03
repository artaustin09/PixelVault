## ÍNDICE

1. INTRODUCCIÓN  
   1.1 Propósito del documento  
   1.2 ¿Qué es PIXELVAULT?  
   1.3 Contexto del mercado de videojuegos  
   1.4 Objetivos del proyecto  
   1.5 Alcance y limitaciones  
   1.6 Estructura del documento  

2. DESARROLLO  
   2.1 Modelos de datos y relaciones  
       2.1.1 Lista completa de modelos (8 modelos)  
       2.1.2 Relación uno a muchos (1:N) – Explicación con ejemplos y código  
       2.1.3 Relación muchos a muchos (N:M) – Explicación con ejemplos y código  
       2.1.4 Diagrama entidad-relación (ER) completo  
   2.2 Operaciones CRUD a través del panel de administración  
       2.2.1 Creación de datos (Create) – Paso a paso con ejemplo real  
       2.2.2 Visualización de datos (Read) – Filtros, búsqueda, listados  
       2.2.3 Modificación de datos (Update) – Cómo editar relaciones N:M  
       2.2.4 Eliminación de datos (Delete) – Comportamiento con on_delete  
       2.2.5 Gestión de relaciones N:M en el admin con filter_horizontal  
   2.3 Configuración del proyecto (settings.py) – Explicación línea por línea  
   2.4 URLs del proyecto – Cómo funcionan las rutas y los nombres  
   2.5 Vistas (views.py) – Lógica de negocio explicada en detalle  
       2.5.1 Vista home (catálogo y buscador avanzado con objetos Q)  
       2.5.2 Vista detalle_juego (optimización con select_related y prefetch_related)  
       2.5.3 Vistas del carrito de compras (agregar, eliminar, limpiar, confirmar)  
       2.5.4 Vistas de autenticación (registro, login, logout)  
   2.6 Templates (interfaz de usuario) – Explicación detallada  
       2.6.1 Template base (base.html) – Navbar dinámica y estilos  
       2.6.2 Template home.html – Catálogo en tarjetas con buscador  
       2.6.3 Template detalle_juego.html – Ficha técnica y bucles for para N:M  
       2.6.4 Template carrito_detalle.html – Lista de productos, cantidades, totales  
       2.6.5 Template registro.html – Formulario de registro personalizado  
       2.6.6 Template login.html – Formulario de inicio de sesión  
   2.7 Interacción entre views, urls y templates – Flujo completo de una petición  
       2.7.1 Paso a paso desde el clic del usuario hasta el HTML renderizado  
       2.7.2 Ejemplo práctico con la página de detalle de Elden Ring  

3. CONCLUSIONES FINALES  
   3.1 Cumplimiento de objetivos (tabla de verificación)  
   3.2 Aprendizajes técnicos adquiridos  
   3.3 Dificultades encontradas y soluciones aplicadas  
   3.4 Conclusión final del proyecto  

---

## 1. INTRODUCCIÓN

### 1.1 Propósito del documento

El presente documento tiene como propósito describir de manera exhaustiva, detallada y sistemática el desarrollo del proyecto **PIXELVAULT**, un marketplace de videojuegos implementado con el framework Django (Python). Este proyecto constituye la evidencia principal para demostrar la correcta implementación de una base de datos relacional que incluye un mínimo de cuatro modelos interconectados, una relación uno a muchos (1:N) y una relación muchos a muchos (N:M). El documento está dirigido a profesores, evaluadores académicos y cualquier persona interesada en comprender cómo se construye una aplicación web completa utilizando herramientas de código abierto y buenas prácticas de desarrollo. Además, servirá como memoria técnica y guía de mantenimiento para futuras iteraciones del proyecto.

### 1.2 ¿Qué es PIXELVAULT?

PIXELVAULT, cuyo nombre proviene de la combinación de las palabras "Pixel" (píxel, la unidad mínima de una imagen digital) y "Vault" (bóveda, un lugar seguro para guardar objetos de valor), es una plataforma de comercio electrónico especializada en la venta de llaves digitales de videojuegos. Una llave digital es un código alfanumérico único que permite a los usuarios activar y descargar un juego en plataformas como Steam, Epic Games Store, PlayStation Store o Xbox Store.

El proyecto simula un entorno de marketplace real donde interactúan tres actores principales:
- **Vendedores**: Son las personas o tiendas que ofrecen llaves digitales de videojuegos. Cada vendedor puede tener múltiples juegos publicados en su catálogo. Por ejemplo, un vendedor llamado "PixelVault Oficial" puede ofrecer juegos como Elden Ring, Zelda y GTA V.
- **Compradores (Clientes)**: Son los usuarios finales que navegan por el catálogo, utilizan el buscador para encontrar juegos específicos, visualizan los detalles de cada producto, los agregan a un carrito de compras y simulan la transacción de compra.
- **Administradores**: Son los usuarios con permisos especiales (is_staff=True) que gestionan todo el contenido de la plataforma a través de un panel de administración personalizado. Ellos se encargan de crear, modificar y eliminar desarrolladoras, plataformas, géneros, vendedores, videojuegos, clientes y ventas.

**INSERTAR CAPTURA 1: Pantalla principal (home) de PIXELVAULT.**  
*Descripción: Debe mostrarse el catálogo de juegos en tarjetas, la barra de navegación superior con el logo, el campo de búsqueda y los botones de registro/login o el nombre del usuario si ya ha iniciado sesión.*

### 1.3 Contexto del mercado de videojuegos

La industria de los videojuegos ha experimentado un crecimiento sostenido durante las últimas dos décadas. Según reportes de la consultora Newzoo (2023), el mercado global de videojuegos generó más de 184 mil millones de dólares, superando ampliamente a las industrias del cine y la música combinadas. Este crecimiento exponencial ha impulsado la creación de plataformas digitales donde los usuarios no solo consumen entretenimiento, sino que también compran, venden e intercambian productos relacionados.

En particular, el mercado de llaves digitales ha crecido de manera significativa. Plataformas como G2A, Eneba y Kinguin han demostrado que existe una demanda real de juegos a precios competitivos, ofrecidos por vendedores mayoristas que adquieren lotes de llaves a precios reducidos. PIXELVAULT se inserta en este contexto como un proyecto académico que busca replicar las funcionalidades esenciales de estos marketplaces, aplicando conceptos fundamentales de bases de datos relacionales.

### 1.4 Objetivos del proyecto

#### 1.4.1 Objetivo general

Desarrollar una aplicación web funcional que sirva como marketplace de videojuegos, demostrando la implementación correcta de una base de datos relacional que incluya un mínimo de cuatro modelos, una relación uno a muchos (1:N) y una relación muchos a muchos (N:M), utilizando el framework Django y su sistema de modelos ORM.

#### 1.4.2 Objetivos específicos

| ID | Objetivo específico | Descripción detallada |
|----|---------------------|----------------------|
| OE1 | Implementar mínimo 4 modelos | Diseñar y codificar las tablas necesarias para representar desarrolladoras, plataformas, géneros, vendedores, videojuegos, clientes y ventas. En total se implementaron 8 modelos. |
| OE2 | Implementar relación uno a muchos (1:N) | Demostrar la relación uno a muchos mediante ejemplos concretos: una desarrolladora tiene muchos videojuegos; un vendedor ofrece muchos juegos; un cliente realiza muchas ventas. |
| OE3 | Implementar relación muchos a muchos (N:M) | Demostrar la relación muchos a muchos mediante ejemplos concretos: un videojuego puede estar disponible en múltiples plataformas; un videojuego puede tener múltiples géneros. |
| OE4 | Crear panel de administración personalizado | Configurar el admin de Django para gestionar los datos, incluyendo soporte visual para relaciones N:M mediante filter_horizontal, list_display, list_filter, search_fields y fieldsets. |
| OE5 | Implementar CRUD completo | Permitir la Creación, Lectura, Actualización y Eliminación de registros de todos los modelos desde el panel de administración. |
| OE6 | Desarrollar interfaz de usuario funcional | Crear templates HTML que muestren el catálogo de juegos (home), la página de detalle de cada juego (mostrando relaciones N:M), el carrito de compras y los formularios de autenticación. |
| OE7 | Implementar buscador inteligente | Permitir búsquedas por título, desarrolladora, género o plataforma utilizando objetos Q de Django para construir consultas complejas con operador OR. |
| OE8 | Implementar carrito de compras | Desarrollar un carrito que persista en la sesión del usuario, permitiendo agregar, eliminar, actualizar cantidades de productos y simular una compra exitosa. |
| OE9 | Implementar autenticación de usuarios | Registrar nuevos usuarios, iniciar sesión, cerrar sesión, con una barra de navegación (navbar) que cambie dinámicamente según el estado de autenticación del usuario. |
| OE10 | Optimizar consultas a la base de datos | Utilizar select_related para relaciones 1:N y prefetch_related para relaciones N:M, evitando el problema de N+1 consultas que degrada el rendimiento. |

### 1.5 Alcance y limitaciones

**Alcance (qué SÍ incluye el proyecto):**
- Backend completo con 8 modelos y sus relaciones (1:N y N:M).
- Migraciones de base de datos aplicadas correctamente.
- Panel de administración personalizado con filter_horizontal, list_display, list_filter, search_fields y fieldsets.
- Vistas para el catálogo (home), detalle de juegos, carrito de compras y autenticación.
- URLs configuradas con nombres significativos para uso en templates.
- Configuración de archivos multimedia (MEDIA_URL, MEDIA_ROOT) para subir y mostrar portadas de juegos.
- Redirección post-login configurada correctamente (LOGIN_REDIRECT_URL).
- Idioma español configurado para el panel de administración (LANGUAGE_CODE = 'es-mx').
- Template base (base.html) con navbar dinámica y estilos CSS personalizados (tema oscuro neón).
- Página principal (home.html) con catálogo en tarjetas y buscador inteligente.
- Página de detalle (detalle_juego.html) con toda la información técnica y las relaciones N:M (plataformas y géneros) listadas mediante bucles for.
- Página de carrito (carrito_detalle.html) con gestión de cantidades, eliminación de productos y cálculo de totales.
- Pantalla de confirmación de compra (confirmacion.html).
- Formularios de registro y login con estilos personalizados.
- Diseño responsivo adaptable a móvil, tablet y escritorio.
- Autenticación completa (registro, login, logout).
- Sesiones activadas para el carrito de compras.
- Protección CSRF en todos los formularios POST.

**Limitaciones (qué NO incluye el proyecto):**
- No incluye pasarela de pago real (la compra es simulada con una pantalla de confirmación).
- No incluye envío de correos electrónicos de confirmación al comprador o al vendedor.
- No incluye historial de compras visible para el cliente (aunque la tabla Venta existe en la base de datos, no hay una vista pública que la muestre).
- No incluye sistema de valoraciones o reseñas de juegos (calificaciones con estrellas o comentarios).
- No incluye despliegue en la nube (el proyecto se ejecuta solo en entorno local).
- No incluye API REST para consumo desde aplicaciones móviles.
- No incluye pruebas automatizadas (unitarias o de integración).

### 1.6 Estructura del documento

El documento se organiza en tres capítulos principales:
- **Capítulo 1 (Introducción)**: Describe el propósito del documento, qué es PIXELVAULT, el contexto del mercado de videojuegos, los objetivos generales y específicos, el alcance y las limitaciones del proyecto.
- **Capítulo 2 (Desarrollo)**: Es la sección más extensa. Explica detalladamente los modelos de datos y sus relaciones (1:N y N:M) con ejemplos y código, las operaciones CRUD a través del panel de administración (paso a paso), la configuración de settings.py (línea por línea), las URLs del proyecto, las vistas (views.py) con su lógica de negocio, los templates (interfaz de usuario) con indicaciones de dónde colocar las capturas de pantalla, y finalmente la interacción entre views, urls y templates con un flujo de petición explicado paso a paso.
- **Capítulo 3 (Conclusiones finales)**: Presenta el cumplimiento de los objetivos, los aprendizajes técnicos adquiridos, las dificultades encontradas durante el desarrollo y las soluciones aplicadas, y una conclusión final del proyecto.

---

## 2. DESARROLLO

### 2.1 Modelos de datos y relaciones

Los modelos son la representación en código Python de las tablas que conforman la base de datos. Cada clase que hereda de `models.Model` se convierte en una tabla dentro de la base de datos SQLite. A continuación se describen en detalle todos los modelos implementados en el archivo `catalogo/models.py`.

**INSERTAR CAPTURA 2: Panel de administración de Django (/admin/).**  
*Descripción: Debe mostrarse la lista de modelos registrados (Desarrolladoras, Plataformas, Géneros, Vendedores, Videojuegos, Clientes, Ventas).*

#### 2.1.1 Lista completa de modelos (8 modelos)

| Modelo | Atributos | Tipo de dato | Propósito | Relación |
|--------|-----------|--------------|-----------|----------|
| Desarrolladora | nombre | CharField(max_length=100) | Nombre de la empresa desarrolladora (ej. Nintendo) | 1:N con Videojuego |
| | pais | CharField(max_length=50) | País de origen (ej. Japón) | 1:N con Videojuego |
| Plataforma | nombre | CharField(max_length=50) | Nombre de la consola (ej. Nintendo Switch) | N:M con Videojuego |
| | fabricante | CharField(max_length=50) | Empresa fabricante (ej. Nintendo) | N:M con Videojuego |
| Genero | nombre | CharField(max_length=50) | Categoría del juego (ej. Acción, RPG) | N:M con Videojuego |
| Vendedor | nombre | CharField(max_length=100) | Nombre real o de la tienda | 1:N con Videojuego |
| | alias | CharField(max_length=50) | Nombre de usuario o gamertag | 1:N con Videojuego |
| Videojuego | titulo | CharField(max_length=150) | Título del juego | (modelo central) |
| | descripcion | TextField | Descripción larga del juego | - |
| | precio | DecimalField(max_digits=10, decimal_places=2) | Precio con dos decimales | - |
| | anio | IntegerField | Año de lanzamiento | - |
| | portada | ImageField(upload_to='portadas/') | Imagen de la carátula | - |
| | desarrolladora | ForeignKey(Desarrolladora) | Relación con Desarrolladora | 1:N |
| | vendedor | ForeignKey(Vendedor) | Relación con Vendedor | 1:N |
| | plataformas | ManyToManyField(Plataforma) | Relación con Plataforma | N:M |
| | generos | ManyToManyField(Genero) | Relación con Genero | N:M |
| Cliente | nombre | CharField(max_length=100) | Nombre del comprador | 1:N con Venta |
| | email | EmailField | Correo electrónico | 1:N con Venta |
| | telefono | CharField(max_length=20) | Número de teléfono | 1:N con Venta |
| | direccion | TextField | Dirección de facturación | 1:N con Venta |
| Venta | videojuego | ForeignKey(Videojuego) | Relación con Videojuego | N:1 con Videojuego |
| | cliente | ForeignKey(Cliente) | Relación con Cliente | N:1 con Cliente |
| | fecha_compra | DateField(auto_now_add=True) | Fecha automática de la compra | - |
| | total | DecimalField(max_digits=10, decimal_places=2) | Monto total de la transacción | - |
| User (Django) | username | CharField | Nombre de usuario | - |
| | password | CharField | Contraseña (hasheada) | - |
| | email | EmailField | Correo electrónico | - |
| | is_staff | BooleanField | Permisos de administrador | - |

#### 2.1.2 Relación uno a muchos (1:N) – Explicación detallada con ejemplos y código

La relación uno a muchos (1:N) significa que un registro de una tabla A puede estar asociado a muchos registros de una tabla B, pero cada registro de la tabla B está asociado a un único registro de la tabla A. En Django se implementa con `models.ForeignKey`.

**Relación 1: Desarrolladora → Videojuego**

Una empresa desarrolladora puede crear muchos videojuegos, pero cada videojuego pertenece a una única desarrolladora.

*Ejemplo concreto:* La empresa **Nintendo** (un registro en la tabla Desarrolladora) ha creado múltiples videojuegos: The Legend of Zelda: Breath of the Wild, Super Mario Odyssey, Pokémon Espada. Cada uno de estos juegos tiene como desarrolladora a Nintendo.

*Código en models.py:*
```python
class Desarrolladora(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=50)

class Videojuego(models.Model):
    titulo = models.CharField(max_length=150)
    desarrolladora = models.ForeignKey(Desarrolladora, on_delete=models.CASCADE)
Relación 2: Vendedor → Videojuego

Un vendedor puede ofrecer muchos videojuegos en su catálogo, pero cada videojuego es ofrecido por un único vendedor.

Ejemplo concreto: El vendedor PixelVault Oficial ofrece múltiples juegos: Elden Ring, GTA V, Cyberpunk 2077.

Código en models.py:

python
class Vendedor(models.Model):
    nombre = models.CharField(max_length=100)
    alias = models.CharField(max_length=50)

class Videojuego(models.Model):
    vendedor = models.ForeignKey(Vendedor, on_delete=models.SET_NULL, null=True)
Relación 3: Cliente → Venta

Un cliente puede realizar muchas compras (ventas), pero cada venta pertenece a un único cliente.

Ejemplo concreto: El cliente Juan Pérez ha realizado múltiples compras: Elden Ring y Zelda.

Código en models.py:

python
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()

class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_compra = models.DateField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
2.1.3 Relación muchos a muchos (N:M) – Explicación detallada con ejemplos y código
La relación muchos a muchos (N:M) es aquella en la que un registro de una tabla A puede estar asociado a muchos registros de una tabla B, y viceversa. En Django se implementa con ManyToManyField, que crea automáticamente una tabla intermedia.

Relación 1: Videojuego ↔ Plataforma

Un videojuego puede estar disponible en múltiples plataformas, y una plataforma puede tener muchos videojuegos.

Ejemplo concreto: Elden Ring está disponible en PC, PlayStation 5 y Xbox Series X.

Código en models.py:

python
class Plataforma(models.Model):
    nombre = models.CharField(max_length=50)
    fabricante = models.CharField(max_length=50)

class Videojuego(models.Model):
    plataformas = models.ManyToManyField(Plataforma)
Relación 2: Videojuego ↔ Genero

Un videojuego puede tener múltiples géneros, y un género puede estar presente en muchos videojuegos.

Ejemplo concreto: Elden Ring es de los géneros Acción y RPG.

Código en models.py:

python
class Genero(models.Model):
    nombre = models.CharField(max_length=50)

class Videojuego(models.Model):
    generos = models.ManyToManyField(Genero)
INSERTAR CAPTURA 3: Página de detalle de un juego (ej. Elden Ring).
Descripción: Debe mostrar claramente las plataformas (PC, PS5) y los géneros (RPG, Acción) listados.

2.1.4 Diagrama entidad-relación (ER) completo
text
Desarrolladora (1) ──── (N) Videojuego (N) ──── (M) Plataforma
Vendedor (1)       ──── (N) Videojuego (N) ──── (M) Genero
Videojuego (1)     ──── (N) Venta (N) ──── (1) Cliente
Convenciones:

Las flechas sólidas (───→) representan relaciones 1:N.

Las líneas con N y M representan relaciones N:M.

PK = clave primaria. Las claves foráneas se indican con _id.

2.2 Operaciones CRUD a través del panel de administración
El panel de administración de Django es una interfaz gráfica que se genera automáticamente a partir de los modelos definidos. Permite gestionar todos los datos del sistema sin necesidad de escribir consultas SQL manuales. Para acceder, se debe crear un superusuario con python manage.py createsuperuser y luego ingresar a http://127.0.0.1:8000/admin/.

INSERTAR CAPTURA 4: Formulario de creación de un videojuego en el administrador.
Descripción: Deben verse todos los campos: título, descripción, precio, año, desarrolladora (desplegable), vendedor (desplegable), y los campos de plataformas y géneros con el widget de dos columnas (filter_horizontal).

2.2.1 Creación de datos (Create) – Paso a paso con ejemplo real
Acceder a http://127.0.0.1:8000/admin/catalogo/videojuego/add/.

Completar los campos básicos:

Título: "Elden Ring"

Descripción: "Un fascinante mundo abierto lleno de peligros..."

Precio: 59.99

Año: 2022

Seleccionar la desarrolladora (relación 1:N): "FromSoftware".

Seleccionar el vendedor (relación 1:N): "PixelVault Oficial".

Asignar plataformas (relación N:M): mover "PC Master Race" y "PlayStation 5" a la columna derecha.

Asignar géneros (relación N:M): mover "RPG" y "Acción" a la columna derecha.

Subir la imagen de portada.

Hacer clic en GUARDAR.

INSERTAR CAPTURA 5: Campo "Plataformas" en el admin con dos columnas y flechas (filter_horizontal).

2.2.2 Visualización de datos (Read)
La lista de videojuegos muestra columnas configuradas con list_display.

Se pueden aplicar filtros laterales y buscar por título.

2.2.3 Modificación de datos (Update)
Hacer clic en el título del juego a modificar.

Cambiar campos o relaciones N:M (mover elementos entre columnas).

Guardar.

2.2.4 Eliminación de datos (Delete)
Marcar el checkbox del juego.

Seleccionar "Eliminar" en acciones.

Confirmar.

2.2.5 Gestión de relaciones N:M en el admin con filter_horizontal
filter_horizontal = ('plataformas', 'generos') muestra dos columnas con flechas, facilitando la asignación múltiple.

2.3 Configuración del proyecto (settings.py) – Explicación línea por línea
python
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

INSTALLED_APPS = [
    ...,
    'catalogo',  # Nuestra aplicación
]

MIDDLEWARE = [
    ...,
    'django.contrib.sessions.middleware.SessionMiddleware',  # Carrito
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Login
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
2.4 URLs del proyecto – Cómo funcionan las rutas
config/urls.py

python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catalogo.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
catalogo/urls.py

python
urlpatterns = [
    path('', views.home, name='home'),
    path('juego/<int:juego_id>/', views.detalle_juego, name='detalle_juego'),
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('agregar/<int:juego_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('eliminar/<int:juego_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('limpiar/', views.limpiar_carrito, name='limpiar_carrito'),
    path('confirmar-compra/', views.confirmar_compra, name='confirmar_compra'),
    path('registro/', views.registro, name='registro'),
    path('login/', auth_views.LoginView.as_view(template_name='catalogo/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
]
2.5 Vistas (views.py) – Lógica de negocio explicada en detalle
2.5.1 Vista home (buscador con objetos Q)
python
def home(request):
    juegos = Videojuego.objects.all()
    query = request.GET.get('buscar')
    if query:
        juegos = juegos.filter(
            Q(titulo__icontains=query) |
            Q(generos__nombre__icontains=query) |
            Q(plataformas__nombre__icontains=query) |
            Q(desarrolladora__nombre__icontains=query)
        ).distinct()
    return render(request, 'catalogo/home.html', {'juegos': juegos, 'busqueda': query})
INSERTAR CAPTURA 6: Resultado del buscador en la página principal (ej. buscar "Zelda").

2.5.2 Vista detalle_juego (optimización con select_related y prefetch_related)
python
def detalle_juego(request, juego_id):
    juego = get_object_or_404(
        Videojuego.objects.select_related('desarrolladora', 'vendedor')
                         .prefetch_related('plataformas', 'generos'),
        pk=juego_id
    )
    return render(request, 'catalogo/detalle_juego.html', {'juego': juego})
2.5.3 Vistas del carrito de compras
python
def agregar_al_carrito(request, juego_id):
    carrito = request.session.get('carrito', {})
    juego = get_object_or_404(Videojuego, id=juego_id)
    id_str = str(juego_id)
    if id_str in carrito:
        carrito[id_str]['cantidad'] += 1
    else:
        carrito[id_str] = {'nombre': juego.titulo, 'precio': float(juego.precio), 'cantidad': 1}
    request.session['carrito'] = carrito
    return redirect('home')
2.5.4 Vistas de autenticación (registro, login, logout)
python
def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistroForm()
    return render(request, 'catalogo/registro.html', {'form': form})
2.6 Templates (interfaz de usuario) – Explicación detallada
2.6.1 Template base (base.html)
Define navbar dinámica con {% if user.is_authenticated %}.

2.6.2 Template home.html – Catálogo en tarjetas
Muestra juegos con portada, título, precio, botones.

2.6.3 Template detalle_juego.html – Relaciones N:M con bucles for
html
<p><strong>Plataformas:</strong>
    {% for plataforma in juego.plataformas.all %}
        {{ plataforma.nombre }}{% if not forloop.last %}, {% endif %}
    {% endfor %}
</p>
INSERTAR CAPTURA 7: Otra vista de detalle (opcional, puede ser la misma que la captura 3).

2.6.4 Template carrito_detalle.html
Lista productos del carrito, permite actualizar cantidades, ver total.

INSERTAR CAPTURA 8: Carrito de compras con al menos dos juegos agregados (cantidades, subtotales, total).

2.6.5 Template registro.html
Formulario de registro de usuarios.

INSERTAR CAPTURA 9: Formulario de registro (campos: usuario, email, contraseña, confirmación).

2.6.6 Template login.html
Formulario de inicio de sesión.

INSERTAR CAPTURA 10: Formulario de login (usuario y contraseña).

2.7 Interacción entre views, urls y templates – Flujo completo de una petición
Usuario hace clic en "Ver Detalle".

Navegador solicita /juego/5/.

urls.py ejecuta detalle_juego(request, juego_id=5).

Vista consulta BD con select_related y prefetch_related.

Vista pasa objeto juego al template.

Template genera HTML con datos dinámicos.

Navegador muestra la página.

INSERTAR CAPTURA 11: Pantalla de confirmación de compra (mensaje de éxito).

3. CONCLUSIONES FINALES
3.1 Cumplimiento de objetivos (tabla de verificación)
Objetivo	Estado	Evidencia
Mínimo 4 modelos	✅ Cumplido	8 modelos implementados
Relación 1:N	✅ Cumplido	Desarrolladora→Videojuego, Vendedor→Videojuego, Cliente→Venta
Relación N:M	✅ Cumplido	Videojuego↔Plataforma, Videojuego↔Genero
CRUD en admin	✅ Cumplido	Crear, leer, actualizar, eliminar desde /admin/
Interfaz visual	✅ Cumplido	Catálogo, detalle, carrito, autenticación
Buscador inteligente	✅ Cumplido	Búsqueda por título, desarrolladora, género, plataforma
Carrito de compras	✅ Cumplido	Persistencia en sesión, agregar, eliminar, actualizar
Autenticación	✅ Cumplido	Registro, login, logout, navbar dinámica
Optimización de consultas	✅ Cumplido	Uso de select_related y prefetch_related
3.2 Aprendizajes técnicos adquiridos
Modelado de bases de datos relacionales en Django.

Optimización de consultas con select_related y prefetch_related.

Gestión de sesiones para carrito de compras.

Personalización del panel de administración (filter_horizontal, list_display, etc.).

Búsquedas avanzadas con objetos Q.

Autenticación y navbar dinámica.

3.3 Dificultades encontradas y soluciones aplicadas
Dificultad	Solución
Relaciones N:M no se mostraban	Usar {% for %} para recorrer .all()
Selección múltiple difícil en admin	filter_horizontal
Redirección post‑login	LOGIN_REDIRECT_URL = 'home'
Imágenes no se mostraban	Configurar MEDIA_URL y MEDIA_ROOT
Buscador no encontraba por plataforma	Agregar Q(plataformas__nombre__icontains=query)
3.4 Conclusión final del proyecto
El desarrollo de PIXELVAULT ha demostrado de manera exitosa la implementación de una base de datos relacional en un entorno web real utilizando el framework Django. Se cumplieron todos los objetivos académicos: se implementaron 8 modelos (superando el mínimo de 4), se demostraron tres relaciones uno a muchos y dos relaciones muchos a muchos, se configuró un panel de administración personalizado con soporte visual para relaciones N:M, se desarrolló una interfaz de usuario atractiva y funcional con buscador inteligente, carrito de compras persistente y autenticación completa.

El proyecto constituye una base sólida y escalable para un marketplace real. Las optimizaciones de consultas con select_related y prefetch_related garantizan un rendimiento adecuado. Los conocimientos adquiridos en modelado de datos, manejo de sesiones, personalización del admin y uso de objetos Q sientan las bases para futuras ampliaciones.

En conclusión, PIXELVAULT refleja el dominio de conceptos fundamentales de bases de datos relacionales y desarrollo web con Django, cumpliendo con todos los requisitos de la asignatura.