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

ÍNDICE
INTRODUCCIÓN
1.1 Propósito del documento
1.2 ¿Qué es PIXELVAULT?
1.3 Contexto del mercado de videojuegos
1.4 Objetivos del proyecto
1.4.1 Objetivo general
1.4.2 Objetivos específicos
1.5 Alcance y limitaciones
1.6 Estructura del documento
DESARROLLO
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
CONCLUSIONES FINALES
3.1 Cumplimiento de objetivos (tabla de verificación)
3.2 Aprendizajes técnicos adquiridos
3.3 Dificultades encontradas y soluciones aplicadas
3.4 Conclusión final del proyecto

1. INTRODUCCIÓN
1.1 Propósito del documento
El presente documento tiene como propósito describir de manera exhaustiva, detallada y sistemática el desarrollo del proyecto PIXELVAULT, un marketplace de videojuegos implementado con el framework Django (Python). Este proyecto constituye la evidencia principal para demostrar la correcta implementación de una base de datos relacional que incluye un mínimo de cuatro modelos interconectados, una relación uno a muchos (1:N) y una relación muchos a muchos (N:M). El documento está dirigido a profesores, evaluadores académicos y cualquier persona interesada en comprender cómo se construye una aplicación web completa utilizando herramientas de código abierto y buenas prácticas de desarrollo. Además, servirá como memoria técnica y guía de mantenimiento para futuras iteraciones del proyecto.
1.2 ¿Qué es PIXELVAULT?
PIXELVAULT, cuyo nombre proviene de la combinación de las palabras "Pixel" (píxel, la unidad mínima de una imagen digital) y "Vault" (bóveda, un lugar seguro para guardar objetos de valor), es una plataforma de comercio electrónico especializada en la venta de llaves digitales de videojuegos. Una llave digital es un código alfanumérico único que permite a los usuarios activar y descargar un juego en plataformas como Steam, Epic Games Store, PlayStation Store o Xbox Store.
El proyecto simula un entorno de marketplace real donde interactúan tres actores principales:
Vendedores: Son las personas o tiendas que ofrecen llaves digitales de videojuegos. Cada vendedor puede tener múltiples juegos publicados en su catálogo. Por ejemplo, un vendedor llamado "PixelVault Oficial" puede ofrecer juegos como Elden Ring, Zelda y GTA V.
Compradores (Clientes): Son los usuarios finales que navegan por el catálogo, utilizan el buscador para encontrar juegos específicos, visualizan los detalles de cada producto, los agregan a un carrito de compras y simulan la transacción de compra.
Administradores: Son los usuarios con permisos especiales (is_staff=True) que gestionan todo el contenido de la plataforma a través de un panel de administración personalizado. Ellos se encargan de crear, modificar y eliminar desarrolladoras, plataformas, géneros, vendedores, videojuegos, clientes y ventas.

1.3 Contexto del mercado de videojuegos
La industria de los videojuegos ha experimentado un crecimiento sostenido durante las últimas dos décadas. Según reportes de la consultora Newzoo (2023), el mercado global de videojuegos generó más de 184 mil millones de dólares, superando ampliamente a las industrias del cine y la música combinadas. Este crecimiento exponencial ha impulsado la creación de plataformas digitales donde los usuarios no solo consumen entretenimiento, sino que también compran, venden e intercambian productos relacionados.
En particular, el mercado de llaves digitales ha crecido de manera significativa. Plataformas como G2A, Eneba y Kinguin han demostrado que existe una demanda real de juegos a precios competitivos, ofrecidos por vendedores mayoristas que adquieren lotes de llaves a precios reducidos. PIXELVAULT se inserta en este contexto como un proyecto académico que busca replicar las funcionalidades esenciales de estos marketplaces, aplicando conceptos fundamentales de bases de datos relacionales.
1.4 Objetivos del proyecto
1.4.1 Objetivo general
Desarrollar una aplicación web funcional que sirva como marketplace de videojuegos, demostrando la implementación correcta de una base de datos relacional que incluya un mínimo de cuatro modelos, una relación uno a muchos (1:N) y una relación muchos a muchos (N:M), utilizando el framework Django y su sistema de modelos ORM.
1.4.2 Objetivos específicos
A continuación se enumeran los objetivos específicos del proyecto, cada uno con su nivel de cumplimiento:
ID
Objetivo específico
Descripción detallada
OE1
Implementar mínimo 4 modelos
Diseñar y codificar las tablas necesarias para representar desarrolladoras, plataformas, géneros, vendedores, videojuegos, clientes y ventas. En total se implementaron 8 modelos.
OE2
Implementar relación uno a muchos (1:N)
Demostrar la relación uno a muchos mediante ejemplos concretos: una desarrolladora tiene muchos videojuegos; un vendedor ofrece muchos juegos; un cliente realiza muchas ventas.
OE3
Implementar relación muchos a muchos (N:M)
Demostrar la relación muchos a muchos mediante ejemplos concretos: un videojuego puede estar disponible en múltiples plataformas; un videojuego puede tener múltiples géneros.
OE4
Crear panel de administración personalizado
Configurar el admin de Django para gestionar los datos, incluyendo soporte visual para relaciones N:M mediante filter_horizontal, list_display, list_filter, search_fields y fieldsets.
OE5
Implementar CRUD completo
Permitir la Creación, Lectura, Actualización y Eliminación de registros de todos los modelos desde el panel de administración.
OE6
Desarrollar interfaz de usuario funcional
Crear templates HTML que muestren el catálogo de juegos (home), la página de detalle de cada juego (mostrando relaciones N:M), el carrito de compras y los formularios de autenticación.
OE7
Implementar buscador inteligente
Permitir búsquedas por título, desarrolladora, género o plataforma utilizando objetos Q de Django para construir consultas complejas con operador OR.
OE8
Implementar carrito de compras
Desarrollar un carrito que persista en la sesión del usuario, permitiendo agregar, eliminar, actualizar cantidades de productos y simular una compra exitosa.
OE9
Implementar autenticación de usuarios
Registrar nuevos usuarios, iniciar sesión, cerrar sesión, con una barra de navegación (navbar) que cambie dinámicamente según el estado de autenticación del usuario.
OE10
Optimizar consultas a la base de datos
Utilizar select_related para relaciones 1:N y prefetch_related para relaciones N:M, evitando el problema de N+1 consultas que degrada el rendimiento.

1.5 Alcance y limitaciones
Alcance (qué SÍ incluye el proyecto):
Backend completo con 8 modelos y sus relaciones (1:N y N:M).
Migraciones de base de datos aplicadas correctamente.
Panel de administración personalizado con filter_horizontal, list_display, list_filter, search_fields y fieldsets.
Vistas para el catálogo (home), detalle de juegos, carrito de compras y autenticación.
URLs configuradas con nombres significativos para uso en templates.
Configuración de archivos multimedia (MEDIA_URL, MEDIA_ROOT) para subir y mostrar portadas de juegos.
Redirección post-login configurada correctamente (LOGIN_REDIRECT_URL).
Idioma español configurado para el panel de administración (LANGUAGE_CODE = 'es-mx').
Template base (base.html) con navbar dinámica y estilos CSS personalizados (tema oscuro neón).
Página principal (home.html) con catálogo en tarjetas y buscador inteligente.
Página de detalle (detalle_juego.html) con toda la información técnica y las relaciones N:M (plataformas y géneros) listadas mediante bucles for.
Página de carrito (carrito_detalle.html) con gestión de cantidades, eliminación de productos y cálculo de totales.
Pantalla de confirmación de compra (confirmacion.html).
Formularios de registro y login con estilos personalizados.
Diseño responsivo adaptable a móvil, tablet y escritorio.
Autenticación completa (registro, login, logout).
Sesiones activadas para el carrito de compras.
Protección CSRF en todos los formularios POST.
Limitaciones (qué NO incluye el proyecto):
No incluye pasarela de pago real (la compra es simulada con una pantalla de confirmación).
No incluye envío de correos electrónicos de confirmación al comprador o al vendedor.
No incluye historial de compras visible para el cliente (aunque la tabla Venta existe en la base de datos, no hay una vista pública que la muestre).
No incluye sistema de valoraciones o reseñas de juegos (calificaciones con estrellas o comentarios).
No incluye despliegue en la nube (el proyecto se ejecuta solo en entorno local).
No incluye API REST para consumo desde aplicaciones móviles.
No incluye pruebas automatizadas (unitarias o de integración).
1.6 Estructura del documento
El documento se organiza en tres capítulos principales:
Capítulo 1 (Introducción): Describe el propósito del documento, qué es PIXELVAULT, el contexto del mercado de videojuegos, los objetivos generales y específicos, el alcance y las limitaciones del proyecto.
Capítulo 2 (Desarrollo): Es la sección más extensa. Explica detalladamente los modelos de datos y sus relaciones (1:N y N:M) con ejemplos y código, las operaciones CRUD a través del panel de administración (paso a paso), la configuración de settings.py (línea por línea), las URLs del proyecto, las vistas (views.py) con su lógica de negocio, los templates (interfaz de usuario) con indicaciones de dónde colocar las capturas de pantalla, y finalmente la interacción entre views, urls y templates con un flujo de petición explicado paso a paso.
Capítulo 3 (Conclusiones finales): Presenta el cumplimiento de los objetivos, los aprendizajes técnicos adquiridos, las dificultades encontradas durante el desarrollo y las soluciones aplicadas, y una conclusión final del proyecto.

2. DESARROLLO
2.1 Modelos de datos y relaciones
Los modelos son la representación en código Python de las tablas que conforman la base de datos. Cada clase que hereda de models.Model se convierte en una tabla dentro de la base de datos SQLite. A continuación se describen en detalle todos los modelos implementados en el archivo catalogo/models.py.

2.1.1 Lista completa de modelos (8 modelos)
A continuación se presenta una tabla con todos los modelos, sus atributos, tipos de datos y propósito:
Modelo
Atributos
Tipo de dato
Propósito
Relación
Desarrolladora
nombre
CharField(max_length=100)
Nombre de la empresa desarrolladora (ej. Nintendo)
1:N con Videojuego


pais
CharField(max_length=50)
País de origen (ej. Japón)
1:N con Videojuego
Plataforma
nombre
CharField(max_length=50)
Nombre de la consola (ej. Nintendo Switch)
N:M con Videojuego


fabricante
CharField(max_length=50)
Empresa fabricante (ej. Nintendo)
N:M con Videojuego
Genero
nombre
CharField(max_length=50)
Categoría del juego (ej. Acción, RPG)
N:M con Videojuego
Vendedor
nombre
CharField(max_length=100)
Nombre real o de la tienda
1:N con Videojuego


alias
CharField(max_length=50)
Nombre de usuario o gamertag
1:N con Videojuego
Videojuego
titulo
CharField(max_length=150)
Título del juego
(modelo central)


descripcion
TextField
Descripción larga del juego
-


precio
DecimalField(max_digits=10, decimal_places=2)
Precio con dos decimales
-


anio
IntegerField
Año de lanzamiento
-


portada
ImageField(upload_to='portadas/')
Imagen de la carátula
-


desarrolladora
ForeignKey(Desarrolladora)
Relación con Desarrolladora
1:N


vendedor
ForeignKey(Vendedor)
Relación con Vendedor
1:N


plataformas
ManyToManyField(Plataforma)
Relación con Plataforma
N:M


generos
ManyToManyField(Genero)
Relación con Genero
N:M
Cliente
nombre
CharField(max_length=100)
Nombre del comprador
1:N con Venta


email
EmailField
Correo electrónico
1:N con Venta


telefono
CharField(max_length=20)
Número de teléfono
1:N con Venta


direccion
TextField
Dirección de facturación
1:N con Venta
Venta
videojuego
ForeignKey(Videojuego)
Relación con Videojuego
N:1 con Videojuego


cliente
ForeignKey(Cliente)
Relación con Cliente
N:1 con Cliente


fecha_compra
DateField(auto_now_add=True)
Fecha automática de la compra
-


total
DecimalField(max_digits=10, decimal_places=2)
Monto total de la transacción
-
User (Django)
username
CharField
Nombre de usuario
-


password
CharField
Contraseña (hasheada)
-


email
EmailField
Correo electrónico
-


is_staff
BooleanField
Permisos de administrador
-

2.1.2 Relación uno a muchos (1:N) – Explicación detallada con ejemplos y código
La relación uno a muchos (1:N) significa que un registro de una tabla A puede estar asociado a muchos registros de una tabla B, pero cada registro de la tabla B está asociado a un único registro de la tabla A. En Django se implementa con models.ForeignKey.
Relación 1: Desarrolladora → Videojuego
Una empresa desarrolladora puede crear muchos videojuegos, pero cada videojuego pertenece a una única desarrolladora.
Ejemplo concreto: La empresa Nintendo (un registro en la tabla Desarrolladora) ha creado múltiples videojuegos: The Legend of Zelda: Breath of the Wild, Super Mario Odyssey, Pokémon Espada. Cada uno de estos juegos tiene como desarrolladora a Nintendo.
Código en models.py:
class Desarrolladora(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=50)


class Videojuego(models.Model):
    titulo = models.CharField(max_length=150)
    desarrolladora = models.ForeignKey(Desarrolladora, on_delete=models.CASCADE)


Explicación del código:
ForeignKey(Desarrolladora, on_delete=models.CASCADE) crea una columna en la tabla Videojuego que almacena la clave primaria (ID) de la desarrolladora asociada.
on_delete=models.CASCADE significa que si se elimina una desarrolladora, todos sus videojuegos también se eliminan automáticamente (integridad referencial en cascada). Esto es útil porque si Nintendo desaparece como empresa, sus juegos ya no tienen sentido en el catálogo.
Relación 2: Vendedor → Videojuego
Un vendedor puede ofrecer muchos videojuegos en su catálogo, pero cada videojuego es ofrecido por un único vendedor.
Ejemplo concreto: El vendedor PixelVault Oficial (un registro en la tabla Vendedor) ofrece múltiples juegos: Elden Ring, GTA V, Cyberpunk 2077. Cada uno de estos juegos tiene a PixelVault Oficial como su vendedor.
Código en models.py:
class Vendedor(models.Model):
    nombre = models.CharField(max_length=100)
    alias = models.CharField(max_length=50)


class Videojuego(models.Model):
    vendedor = models.ForeignKey(Vendedor, on_delete=models.SET_NULL, null=True)


Explicación del código:
on_delete=models.SET_NULL significa que si se elimina un vendedor, los juegos que ofrecía NO se eliminan, sino que el campo vendedor se pone como NULL.
null=True permite que el campo pueda estar vacío (sin vendedor asignado). Esto es razonable porque un juego podría seguir existiendo aunque el vendedor ya no esté activo.
Relación 3: Cliente → Venta
Un cliente puede realizar muchas compras (ventas), pero cada venta pertenece a un único cliente.
Ejemplo concreto: El cliente Juan Pérez (un registro en la tabla Cliente) ha realizado múltiples compras: una compra de Elden Ring el 1 de junio y otra compra de Zelda el 5 de junio. Cada una de estas ventas tiene a Juan Pérez como su cliente.
Código en models.py:
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()


class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_compra = models.DateField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)


2.1.3 Relación muchos a muchos (N:M) – Explicación detallada con ejemplos y código
La relación muchos a muchos (N:M) es aquella en la que un registro de una tabla A puede estar asociado a muchos registros de una tabla B, y viceversa, un registro de la tabla B puede estar asociado a muchos registros de la tabla A. En Django se implementa con ManyToManyField, que crea automáticamente una tabla intermedia (o tabla de unión) para gestionar las asociaciones.
Relación 1: Videojuego ↔ Plataforma
Un videojuego puede estar disponible en múltiples plataformas (consolas o sistemas), y una plataforma puede tener muchos videojuegos disponibles.
Ejemplo concreto: El juego Elden Ring está disponible en PC, PlayStation 5 y Xbox Series X. A su vez, la plataforma PC tiene disponibles múltiples juegos: Elden Ring, GTA V, Cyberpunk 2077.
Código en models.py:


class Plataforma(models.Model):
    nombre = models.CharField(max_length=50)
    fabricante = models.CharField(max_length=50)


class Videojuego(models.Model):
    plataformas = models.ManyToManyField(Plataforma)


Explicación del código:
ManyToManyField(Plataforma) crea automáticamente una tabla intermedia (normalmente llamada catalogo_videojuego_plataformas) con dos columnas: videojuego_id y plataforma_id.
No es necesario definir manualmente la tabla intermedia; Django la maneja automáticamente.
Para acceder a las plataformas de un juego desde el template se usa {% for plataforma in juego.plataformas.all %}.
Relación 2: Videojuego ↔ Genero
Un videojuego puede tener múltiples géneros, y un género puede estar presente en muchos videojuegos.
Ejemplo concreto: El juego Elden Ring es de los géneros Acción y RPG. A su vez, el género Acción está presente en muchos juegos: Elden Ring, GTA V, Zelda.
Código en models.py:
class Plataforma(models.Model):
    nombre = models.CharField(max_length=50)
    fabricante = models.CharField(max_length=50)


class Videojuego(models.Model):
    plataformas = models.ManyToManyField(Plataforma)


.
A continuación se muestra el diagrama entidad-relación completo del proyecto, donde se pueden visualizar gráficamente todas las entidades, sus atributos y las relaciones entre ellas. Las flechas sólidas representan relaciones 1:N. Las líneas con N y M en los extremos representan relaciones N:M.
Convenciones del diagrama:
Las flechas sólidas (───→) representan relaciones 1:N (uno a muchos).
Las líneas con N y M en los extremos representan relaciones N:M (muchos a muchos).
PK indica clave primaria (Primary Key).
Las claves foráneas (ForeignKey) se indican con el sufijo _id en el diagrama.

2.2 Operaciones CRUD a través del panel de administración
El panel de administración de Django es una interfaz gráfica que se genera automáticamente a partir de los modelos definidos. Permite gestionar todos los datos del sistema sin necesidad de escribir consultas SQL manuales. Para acceder, se debe crear un superusuario con python manage.py createsuperuser y luego ingresar a http://127.0.0.1:8000/admin/.


2.2.1 Creación de datos (Create) – Paso a paso con ejemplo real
El siguiente es un ejemplo completo y detallado de cómo crear un nuevo videojuego en el sistema, incluyendo la asignación de relaciones 1:N y N:M.
Paso 1: Acceder a http://127.0.0.1:8000/admin/catalogo/videojuego/add/
Paso 2: Completar los campos básicos:
Título: "Elden Ring"
Descripción: "Un fascinante mundo abierto lleno de peligros, jefes imponentes y una historia profunda creada por Hidetaka Miyazaki y George R. R. Martin."
Precio: 59.99
Año: 2022
Paso 3: Seleccionar la desarrolladora (relación 1:N):
En el campo desplegable "Desarrolladora", seleccionar "FromSoftware". Si no existe, se puede crear haciendo clic en el botón verde "+" al lado.
Paso 4: Seleccionar el vendedor (relación 1:N):
En el campo desplegable "Vendedor", seleccionar "PixelVault Oficial".
Paso 5: Asignar plataformas (relación N:M):
En el campo "Plataformas", se muestran dos columnas con flechas gracias a filter_horizontal.
En la columna izquierda ("Plataformas disponibles"), hacer clic en "PC Master Race" y "PlayStation 5".
Presionar la flecha que apunta a la derecha (→) para moverlos a la columna derecha ("Plataformas elegidas").
Si se cometió un error, se puede mover de vuelta con la flecha izquierda (←).
Paso 6: Asignar géneros (relación N:M):
En el campo "Géneros", mover "RPG" y "Acción" de la columna izquierda a la derecha.
Paso 7: Subir la imagen de portada:
Hacer clic en "Seleccionar archivo" y elegir una imagen de la computadora (formato .jpg, .png recomendado).
Paso 8: Hacer clic en el botón GUARDAR (ubicado en la parte inferior derecha de la pantalla).
Resultado: El juego Elden Ring queda almacenado en la base de datos con su desarrolladora (FromSoftware), su vendedor (PixelVault Oficial), sus plataformas (PC y PS5) y sus géneros (RPG y Acción). Todas las relaciones quedan correctamente establecidas.
INSERTAR CAPTURA 5: Campo "Plataformas" en el administrador de Django mostrando las dos columnas.
Descripción: Debe verse claramente el widget filter_horizontal con la columna izquierda de "Disponibles" y la derecha de "Elegidos", con las flechas entre ellas. Algunos elementos deben estar en la columna derecha (elegidos) y otros en la izquierda.
2.2.2 Visualización de datos (Read)
La lista de videojuegos (/admin/catalogo/videojuego/) muestra columnas configuradas con list_display: título, precio, año y vendedor.
Se pueden aplicar filtros laterales (configurados con list_filter) para mostrar solo juegos de cierta plataforma o género.
La barra de búsqueda (configurada con search_fields) permite encontrar juegos por título.
Al hacer clic en el título de un juego, se abren los detalles completos del registro, incluyendo todas sus relaciones.
2.2.3 Modificación de datos (Update)
En la lista de videojuegos, hacer clic en el título del juego que se desea modificar (por ejemplo, "Elden Ring").
Cambiar los campos necesarios. Por ejemplo, actualizar el precio de 59.99 a 49.99.
Para modificar relaciones N:M:
Si se quiere agregar "Xbox Series X" a las plataformas, moverla de la columna izquierda a la derecha.
Si se quiere quitar "PlayStation 5", moverla de la columna derecha a la izquierda.
Hacer clic en el botón GUARDAR.
2.2.4 Eliminación de datos (Delete)
En la lista de videojuegos, marcar el checkbox (casilla de verificación) del juego o juegos a eliminar.
En el desplegable "Acción", seleccionar "Eliminar los videojuegos seleccionados".
Hacer clic en "Ir" y confirmar la eliminación en la pantalla de confirmación.
Comportamiento según on_delete:
Si se elimina una Desarrolladora que tiene on_delete=CASCADE, todos sus videojuegos se eliminarán automáticamente en cascada.
Si se elimina un Vendedor que tiene on_delete=SET_NULL, los juegos que ofrecía quedarán con el campo vendedor = NULL (sin vendedor asignado), pero los juegos NO se eliminan.
2.2.5 Gestión de relaciones N:M en el admin con filter_horizontal
Gracias a la configuración filter_horizontal = ('plataformas', 'generos') en el archivo admin.py, el campo ManyToMany se muestra como dos columnas con flechas. Esto facilita enormemente la asignación de múltiples valores:
Ventajas de filter_horizontal:
Es visualmente claro qué está asignado y qué no.
No requiere mantener presionada la tecla Ctrl para seleccionar múltiples elementos.
Reduce errores al guardar relaciones N:M.
Es especialmente útil cuando hay muchas opciones disponibles (decenas de plataformas o géneros).

2.3 Configuración del proyecto (settings.py) – Explicación línea por línea
El archivo config/settings.py contiene toda la configuración global del proyecto Django. A continuación se explican las secciones más importantes que se modificaron para que PIXELVAULT funcione correctamente.
python
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR es la ruta absoluta del directorio raíz del proyecto. Se usa para construir rutas a otros archivos (base de datos, media, etc.).
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'catalogo',  # ← Nuestra aplicación principal
]


'catalogo' es la aplicación que contiene todos los modelos, vistas, templates y lógica del marketplace. Debe estar registrada aquí para que Django la reconozca y ejecute sus migraciones.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # ← Habilita sesiones (necesario para el carrito)
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # ← Habilita autenticación de usuarios
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


SessionMiddleware es fundamental para que el carrito de compras pueda persistir entre diferentes páginas. Sin él, request.session no funcionaría.
AuthenticationMiddleware permite que Django reconozca al usuario logueado y que request.user esté disponible en las vistas y templates.
python
ROOT_URLCONF = 'config.urls'
Indica que el archivo principal de URLs es config/urls.py.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,  # ← Busca templates en catalogo/templates/
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


APP_DIRS = True le dice a Django que busque templates dentro de una carpeta templates en cada aplicación. Por eso podemos usar catalogo/templates/catalogo/home.html.
python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
Se utiliza SQLite3 como motor de base de datos, adecuado para desarrollo por su simplicidad (no requiere instalación de servidor adicional). El archivo db.sqlite3 se crea automáticamente en la raíz del proyecto.
python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_ROOT define la ruta física en el sistema de archivos donde se guardarán las imágenes subidas por los administradores (las portadas de los videojuegos).
MEDIA_URL define la URL base desde la cual se podrán acceder a esas imágenes (ej. http://127.0.0.1:8000/media/portadas/elden_ring.jpg).
También es necesario agregar en el archivo config/urls.py las líneas que sirven estos archivos en modo desarrollo (ver sección 2.4).
python
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'
Redirige al home (página principal) después de iniciar o cerrar sesión. Sin estas líneas, Django intentaría redirigir a /accounts/profile/ y generaría un error 404.
python
LANGUAGE_CODE = 'es-mx'
TIME_ZONE = 'America/Mexico_City'
USE_I18N = True
USE_TZ = True
LANGUAGE_CODE = 'es-mx' traduce el panel de administración y los mensajes del sistema al español de México.
TIME_ZONE = 'America/Mexico_City' ajusta la zona horaria a la de Ciudad de México.
python
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
Configuración para archivos estáticos (CSS, JS). En este proyecto se usaron estilos directamente en los templates, por lo que esta sección es opcional.
python
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
Define el tipo de campo automático para las claves primarias. BigAutoField es un entero grande de 64 bits.

2.4 URLs del proyecto – Cómo funcionan las rutas
Archivo principal config/urls.py:
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),           # Panel de administración
    path('', include('catalogo.urls')),        # Incluye las URLs de la app catalogo
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
path('admin/', admin.site.urls) redirige las peticiones a /admin/ al panel de administración.
path('', include('catalogo.urls')) incluye todas las rutas definidas en el archivo catalogo/urls.py.
El bloque if settings.DEBUG sirve para que Django sirva las imágenes de portada durante el desarrollo. En producción esto se hace de otra manera.
Archivo de URLs de la app catalogo/urls.py:
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    # Página principal (catálogo)
    path('', views.home, name='home'),
    
    # Detalle de un juego (recibe un ID)
    path('juego/<int:juego_id>/', views.detalle_juego, name='detalle_juego'),
    
    # Carrito de compras
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('agregar/<int:juego_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('eliminar/<int:juego_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('limpiar/', views.limpiar_carrito, name='limpiar_carrito'),
    path('confirmar-compra/', views.confirmar_compra, name='confirmar_compra'),
    
    # Autenticación
    path('registro/', views.registro, name='registro'),
    path('login/', auth_views.LoginView.as_view(template_name='catalogo/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
]


Explicación de rutas clave:
Ruta
Nombre (name)
Vista
Descripción
/
home
views.home
Página principal con el catálogo de juegos y buscador.
/juego/5/
detalle_juego
views.detalle_juego
Muestra los detalles del juego con ID 5.
/carrito/
ver_carrito
views.ver_carrito
Muestra el contenido del carrito de compras.
/agregar/5/
agregar_al_carrito
views.agregar_al_carrito
Agrega el juego con ID 5 al carrito.
/eliminar/5/
eliminar_del_carrito
views.eliminar_del_carrito
Elimina el juego con ID 5 del carrito.
/limpiar/
limpiar_carrito
views.limpiar_carrito
Vacía todo el carrito.
/confirmar-compra/
confirmar_compra
views.confirmar_compra
Finaliza la compra (simulada) y vacía el carrito.
/registro/
registro
views.registro
Formulario de registro de nuevos usuarios.
/login/
login
auth_views.LoginView
Formulario de inicio de sesión (vista integrada de Django).
/logout/
logout
auth_views.LogoutView
Cierra la sesión y redirige al home.


2.5 Vistas (views.py) – Lógica de negocio explicada en detalle
El archivo catalogo/views.py contiene las funciones que procesan las peticiones del usuario, interactúan con los modelos y devuelven respuestas (generalmente HTML renderizado).
2.5.1 Vista home (catálogo y buscador avanzado con objetos Q)
from django.shortcuts import render
from django.db.models import Q
from .models import Videojuego


def home(request):
    # Obtener todos los videojuegos de la base de datos
    juegos = Videojuego.objects.all()
    
    # Obtener el parámetro de búsqueda desde la URL (ej. ?buscar=zelda)
    query = request.GET.get('buscar')
    
    # Si hay una búsqueda, aplicar filtros
    if query:
        juegos = juegos.filter(
            Q(titulo__icontains=query) |           # El título contiene el texto
            Q(generos__nombre__icontains=query) |   # Algún género contiene el texto
            Q(plataformas__nombre__icontains=query) | # Alguna plataforma contiene el texto
            Q(desarrolladora__nombre__icontains=query) # La desarrolladora contiene el texto
        ).distinct()  # distinct() evita que un mismo juego aparezca múltiples veces
    
    return render(request, 'catalogo/home.html', {
        'juegos': juegos,
        'busqueda': query
    })


Explicación línea por línea:
Q(titulo__icontains=query): el doble guion bajo __icontains significa "contiene el texto, insensible a mayúsculas".
El operador | significa OR. Así, buscamos juegos que cumplan cualquiera de las condiciones.
distinct() es necesario porque si un juego coincide por varios criterios (por ejemplo, su título y su plataforma), aparecería duplicado en la lista.
El contexto {'juegos': juegos, 'busqueda': query} se pasa al template home.html.
2.5.2 Vista detalle_juego (optimización con select_related y prefetch_related)
python
from django.shortcuts import render, get_object_or_404
from .models import Videojuego

def detalle_juego(request, juego_id):
    # Obtener el juego por su ID, o mostrar error 404 si no existe
    juego = get_object_or_404(
        Videojuego.objects.select_related('desarrolladora', 'vendedor')
                         .prefetch_related('plataformas', 'generos'),
        pk=juego_id
    )
    return render(request, 'catalogo/detalle_juego.html', {'juego': juego})
Explicación de la optimización:
Sin select_related y prefetch_related, el template haría una consulta SQL por cada acceso a juego.desarrolladora.nombre, juego.vendedor.nombre, y luego otra consulta por cada plataforma y género. Esto es el problema N+1.
select_related('desarrolladora', 'vendedor') realiza un JOIN en la consulta principal, trayendo los datos de desarrolladora y vendedor en una sola consulta.
prefetch_related('plataformas', 'generos') realiza consultas separadas pero con un JOIN para cada relación N:M, trayendo todos los datos necesarios de una vez.
2.5.3 Vistas del carrito de compras (agregar, eliminar, limpiar, confirmar)
Vista agregar_al_carrito:
def agregar_al_carrito(request, juego_id):
    # Obtener el carrito de la sesión o crear uno vacío
    carrito = request.session.get('carrito', {})
    
    # Obtener el juego de la base de datos
    juego = get_object_or_404(Videojuego, id=juego_id)
    
    # Convertir el ID a string para usarlo como clave en el diccionario
    id_str = str(juego_id)
    
    if id_str in carrito:
        # Si el juego ya está en el carrito, incrementar la cantidad
        carrito[id_str]['cantidad'] += 1
    else:
        # Si no está, agregarlo con cantidad 1
        carrito[id_str] = {
            'nombre': juego.titulo,
            'precio': float(juego.precio),
            'cantidad': 1,
        }
   

    # Guardar el carrito actualizado en la sesión
    request.session['carrito'] = carrito
    
    # Redirigir a la página principal
    return redirect('home')
Vista ver_carrito:
pytho
Vista eliminar_del_carrito:n
def ver_carrito(request):
    return render(request, 'catalogo/carrito_detalle.html')
def eliminar_del_carrito(request, juego_id):
    carrito = request.session.get('carrito', {})
    id_str = str(juego_id)
    
    if id_str in carrito:
        del carrito[id_str]
    
    request.session['carrito'] = carrito
    return redirect('ver_carrito')


Vista limpiar_carrito:
def limpiar_carrito(request):
    request.session['carrito'] = {}
    return redirect('ver_carrito')


Vista confirmar_compra:
def confirmar_compra(request):
    # Vaciar el carrito
    request.session['carrito'] = {}
    return render(request, 'catalogo/confirmacion.html')


2.5.4 Vistas de autenticación (registro, login, logout)
Vista registro (con formulario personalizado):
from django.contrib.auth import login
from .forms import RegistroForm


def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Inicia sesión automáticamente después del registro
            return redirect('home')
    else:
        form = RegistroForm()
    return render(request, 'catalogo/registro.html', {'form': form})


RegistroForm es un formulario personalizado que hereda de UserCreationForm y añade el campo de email.
login(request, user) autentica al usuario automáticamente sin necesidad de que ingrese sus credenciales nuevamente.
Vistas login y logout (usando las vistas integradas de Django):
LoginView se configura con template_name='catalogo/login.html' para usar nuestro template personalizado.
LogoutView se configura con next_page='home' para redirigir al home después de cerrar sesión.
INSERTAR CAPTURA 6: Resultado del buscador en la página principal.
Descripción: Escribir, por ejemplo, "Zelda" en el campo de búsqueda y presionar buscar. La página debe mostrar solo los juegos que contengan esa palabra en el título, desarrolladora, género o plataforma. Esta imagen demuestra el funcionamiento del buscador inteligente.

2.6 Templates (interfaz de usuario) – Explicación detallada
Los templates son archivos HTML que permiten presentar la información al usuario de forma dinámica. Utilizan la sintaxis de Django: {{ variable }} para mostrar datos y {% tag %} para incluir lógica como bucles o condicionales. Todos los templates heredan de una plantilla base (base.html) que contiene la estructura común (navbar, estilos, pies de página).
2.6.1 Template base (base.html) – Estructura común y navbar dinámica
El template base define el esqueleto de todas las páginas. La navbar cambia según si el usuario está autenticado:
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>PIXELVAULT</title>
    <style>
        body { background: #000; color: #fff; font-family: Arial, sans-serif; margin: 0; padding: 0; }
        nav { background: #111; padding: 15px 40px; border-bottom: 2px solid #00e5ff; }
        .logo { color: #00e5ff; font-size: 24px; font-weight: bold; text-decoration: none; }
        .nav-links { float: right; }
        .nav-links a { color: #fff; margin-left: 20px; text-decoration: none; }
        .container { padding: 40px; }
    </style>
</head>
<body>
    <nav>
        <a href="{% url 'home' %}" class="logo">PIXELVAULT</a>
        <div class="nav-links">
            <a href="{% url 'home' %}">INICIO</a>
            <a href="{% url 'ver_carrito' %}">🛒 CARRITO</a>
            {% if user.is_authenticated %}
                <span>Hola, {{ user.username }}</span>
                <a href="{% url 'logout' %}">SALIR</a>
            {% else %}
                <a href="{% url 'registro' %}">REGISTRO</a>
                <a href="{% url 'login' %}">LOGIN</a>
            {% endif %}
        </div>
    </nav>
    <div class="container">
        {% block content %}{% endblock %}
    </div>
</body>
</html>


{% url 'home' %} genera dinámicamente la URL de la página principal.
{% if user.is_authenticated %} muestra opciones diferentes según si el usuario ha iniciado sesión.
{% block content %} es un marcador que las plantillas hijas llenan con su contenido específico.
2.6.2 Template home.html – Catálogo en tarjetas con buscador
{% extends 'catalogo/base.html' %}


{% block content %}
<h1>Catálogo de Videojuegos</h1>


<form method="GET">
    <input type="text" name="buscar" value="{{ busqueda }}" placeholder="Buscar...">
    <button type="submit">BUSCAR</button>
    <a href="{% url 'home' %}">LIMPIAR</a>
</form>


<div class="grid">
    {% for juego in juegos %}
        <div class="card">
            <img src="{{ juego.portada.url }}" alt="{{ juego.titulo }}">
            <h3>{{ juego.titulo }}</h3>
            <p>${{ juego.precio }}</p>
            <a href="{% url 'detalle_juego' juego.id %}">VER DETALLE</a>
            <a href="{% url 'agregar_al_carrito' juego.id %}">AGREGAR</a>
        </div>
    {% empty %}
        <p>No hay juegos disponibles.</p>
    {% endfor %}
</div>
{% endblock %}


{% for juego in juegos %} recorre la lista de juegos que la vista home envió.
{{ juego.portada.url }} muestra la imagen de portada (requiere la configuración de MEDIA).
{% url 'detalle_juego' juego.id %} genera enlaces como /juego/1/, /juego/2/, etc.

2.6.3 Template detalle_juego.html – Ficha técnica y bucles for para N:M


{% extends 'catalogo/base.html' %}


{% block content %}
<h1>{{ juego.titulo }}</h1>
<img src="{{ juego.portada.url }}" width="300">


<p><strong>Precio:</strong> ${{ juego.precio }}</p>
<p><strong>Año:</strong> {{ juego.anio }}</p>
<p><strong>Descripción:</strong> {{ juego.descripcion }}</p>


<p><strong>Desarrolladora:</strong> {{ juego.desarrolladora.nombre }}</p>
<p><strong>Vendedor:</strong> {{ juego.vendedor.nombre }}</p>


<p><strong>Plataformas:</strong>
    {% for plataforma in juego.plataformas.all %}
        {{ plataforma.nombre }}{% if not forloop.last %}, {% endif %}
    {% endfor %}
</p>


<p><strong>Géneros:</strong>
    {% for genero in juego.generos.all %}
        {{ genero.nombre }}{% if not forloop.last %}, {% endif %}
    {% endfor %}
</p>


<a href="{% url 'agregar_al_carrito' juego.id %}">AGREGAR AL CARRITO</a>
<a href="{% url 'home' %}">VOLVER</a>
{% endblock %}


juego.plataformas.all devuelve todas las plataformas asociadas al juego (relación N:M).
El filtro {% if not forloop.last %}, {% endif %} agrega comas entre los elementos pero no al final.
2.6.4 Template carrito_detalle.html – Lista de productos, cantidades, totales
{% extends 'catalogo/base.html' %}


{% block content %}
<h1>Mi Carrito</h1>


{% if request.session.carrito %}
    <table border="1">
        <tr>
            <th>Juego</th>
            <th>Precio</th>
            <th>Cantidad</th>
            <th>Subtotal</th>
            <th></th>
        </tr>
        {% for key, item in request.session.carrito.items %}
        <tr>
            <td>{{ item.nombre }}</td>
            <td>${{ item.precio }}</td>
            <td>
                <form method="POST" action="{% url 'actualizar_carrito' key %}">
                    {% csrf_token %}
                    <input type="number" name="cantidad" value="{{ item.cantidad }}" min="1">
                    <button type="submit">Actualizar</button>
                </form>
            </td>
            <td>${{ item.precio|floatformat:2|multiply:item.cantidad }}</td>
            <td><a href="{% url 'eliminar_del_carrito' key %}">Eliminar</a></td>
        </tr>
        {% endfor %}
    </table>
    <p><strong>Total:</strong> ${{ total }}</p>
    <a href="{% url 'limpiar_carrito' %}">Vaciar carrito</a>
    <a href="{% url 'confirmar_compra' %}">Finalizar compra</a>
{% else %}
    <p>El carrito está vacío.</p>
{% endif %}
{% endblock %}



2.6.5 Template registro.html – Formulario de registro personalizado
html
{% extends 'catalogo/base.html' %}

{% block content %}
<h2>Registro de usuario</h2>
<form method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Registrarse</button>
</form>
{% endblock %}

2.6.6 Template login.html – Formulario de inicio de sesión
html
{% extends 'catalogo/base.html' %}

{% block content %}
<h2>Iniciar sesión</h2>
<form method="POST">
    {% csrf_token %}
    <input type="text" name="username" placeholder="Usuario" required>
    <input type="password" name="password" placeholder="Contraseña" required>
    <button type="submit">Ingresar</button>
</form>
{% endblock %}
I

2.7 Interacción entre views, urls y templates – Flujo completo de una petición
2.7.1 Paso a paso desde el clic del usuario hasta el HTML renderizado
Usuario: Hace clic en "Ver Detalle" de un juego en el catálogo (por ejemplo, Elden Ring).
Navegador: Construye la URL http://127.0.0.1:8000/juego/5/ y envía una petición GET al servidor Django.
Django (urls.py): Busca en urlpatterns un patrón que coincida. Encuentra path('juego/<int:juego_id>/', views.detalle_juego, name='detalle_juego').
Django (views.py): Ejecuta la función detalle_juego(request, juego_id=5).
Vista: Dentro de la función, get_object_or_404 consulta la base de datos utilizando select_related y prefetch_related. Se traduce a SQL y se obtiene el objeto Videojuego con todas sus relaciones (desarrolladora, vendedor, plataformas, géneros).
Vista: Prepara el contexto {'juego': juego} y llama a render(request, 'catalogo/detalle_juego.html', contexto).
Django (templates): El motor de templates carga el archivo detalle_juego.html, que extiende base.html. Reemplaza {{ juego.titulo }} por "Elden Ring", {{ juego.precio }} por "59.99", y ejecuta el bucle {% for plataforma in juego.plataformas.all %} para generar la lista de plataformas.
Servidor: El HTML generado se envía de vuelta al navegador.
Navegador: Interpreta el HTML, descarga las imágenes (portadas) y muestra la página completa al usuario.
2.7.2 Ejemplo práctico con la página de detalle de Elden Ring
URL solicitada: /juego/5/ (asumiendo que Elden Ring tiene ID 5).
En urls.py: path('juego/<int:juego_id>/', views.detalle_juego, name='detalle_juego') captura el 5 y lo pasa a la vista.
En views.py: detalle_juego(request, juego_id=5) obtiene el juego con ID 5.
En el template: {% for plataforma in juego.plataformas.all %} genera "PC, PlayStation 5".
Resultado visual: El usuario ve una página con el título "Elden Ring", las plataformas "PC, PlayStation 5", los géneros "RPG, Acción", y el botón de agregar al carrito.


3. CONCLUSIONES FINALES
3.1 Cumplimiento de objetivos
El proyecto PIXELVAULT cumple satisfactoriamente con todos los objetivos planteados. A continuación se presenta una tabla de verificación:
Objetivo
Estado
Evidencia
Mínimo 4 modelos
✅ Cumplido
Se implementaron 8 modelos (Desarrolladora, Plataforma, Genero, Vendedor, Videojuego, Cliente, Venta, User).
Relación 1:N
✅ Cumplido
Desarrolladora → Videojuego, Vendedor → Videojuego, Cliente → Venta.
Relación N:M
✅ Cumplido
Videojuego ↔ Plataforma, Videojuego ↔ Genero.
CRUD en admin
✅ Cumplido
El panel de administración permite Crear, Leer, Actualizar y Eliminar registros.
Interfaz visual
✅ Cumplido
Catálogo en tarjetas, página de detalle con relaciones N:M, carrito, formularios de autenticación.
Buscador inteligente
✅ Cumplido
Búsqueda por título, desarrolladora, género o plataforma con objetos Q.
Carrito de compras
✅ Cumplido
Persistencia en sesión, agregar, eliminar, actualizar cantidades, simulación de compra.
Autenticación
✅ Cumplido
Registro, login, logout, navbar dinámica.
Optimización de consultas
✅ Cumplido
Uso de select_related y prefetch_related en la vista detalle_juego.

3.2 Aprendizajes técnicos adquiridos
El desarrollo de PIXELVAULT permitió consolidar los siguientes conocimientos:
Modelado de bases de datos relacionales: Identificar entidades, atributos y relaciones, y traducirlas a código Django usando models.Model, ForeignKey y ManyToManyField.
Optimización de consultas: Uso de select_related para relaciones 1:N y prefetch_related para relaciones N:M, evitando el problema de N+1 consultas que degrada el rendimiento.
Gestión de sesiones: Implementar un carrito de compras persistente usando request.session, almacenando un diccionario con los productos.
Personalización del panel de administración: Configurar filter_horizontal, list_display, list_filter, search_fields y fieldsets para mejorar la experiencia de gestión de datos.
Buscador avanzado: Uso de objetos Q para construir consultas complejas con operador OR, permitiendo búsquedas en múltiples campos relacionados.
Autenticación de usuarios: Formularios personalizados de registro, vistas integradas de login/logout, navbar dinámica con {% if user.is_authenticated %}.
Sistema de templates: Herencia de plantillas con {% extends %}, bloques {% block %}, bucles {% for %} y condicionales {% if %}.
Manejo de archivos multimedia: Configuración de MEDIA_URL y MEDIA_ROOT, y servir archivos en desarrollo con static().
3.3 Dificultades encontradas y soluciones aplicadas
A lo largo del desarrollo se presentaron diversas dificultades que fueron resueltas:
Dificultad
Solución aplicada
Las relaciones muchos a muchos no se mostraban en el template (intentaba usar juego.plataforma.nombre en lugar de recorrer .all()).
Se utilizó un bucle {% for plataforma in juego.plataformas.all %} para recorrer la lista y mostrar cada nombre.
La selección múltiple de plataformas y géneros en el admin era confusa (había que mantener presionada la tecla Ctrl).
Se agregó filter_horizontal = ('plataformas', 'generos') en admin.py, transformando el campo en dos columnas con flechas.
Después de iniciar sesión, Django intentaba redirigir a /accounts/profile/ y daba error 404.
Se agregó LOGIN_REDIRECT_URL = 'home' en settings.py.
Las imágenes de portada no se mostraban en las páginas.
Se configuró MEDIA_URL y MEDIA_ROOT en settings.py y se añadieron las rutas en urls.py con static().
El buscador no encontraba juegos por plataforma o género.
Se agregaron las condiciones Q(plataformas__nombre__icontains=query) y Q(generos__nombre__icontains=query) al filtro.
Error de "NoReverseMatch" al generar URLs dinámicas.
Se verificó que los name en urls.py coincidieran exactamente con los {% url %} en los templates.

3.4 Conclusión final del proyecto
El desarrollo de PIXELVAULT ha demostrado de manera exitosa la implementación de una base de datos relacional en un entorno web real utilizando el framework Django. Se cumplieron todos los objetivos académicos: se implementaron 8 modelos (superando el mínimo de 4), se demostraron tres relaciones uno a muchos y dos relaciones muchos a muchos, se configuró un panel de administración personalizado con soporte visual para relaciones N:M, se desarrolló una interfaz de usuario atractiva y funcional con buscador inteligente, carrito de compras persistente y autenticación completa.
El proyecto constituye una base sólida y escalable para un marketplace real. Las optimizaciones de consultas con select_related y prefetch_related garantizan un rendimiento adecuado incluso con un catálogo grande. Los conocimientos adquiridos en modelado de datos, manejo de sesiones, personalización del admin y uso de objetos Q sientan las bases para futuras ampliaciones, como la integración de pasarelas de pago reales, el envío de correos electrónicos o la creación de una API REST.
En conclusión, PIXELVAULT refleja el dominio de conceptos fundamentales de bases de datos relacionales y desarrollo web con Django, cumpliendo con todos los requisitos de la asignatura y dejando abierta la puerta a mejoras posteriores.



