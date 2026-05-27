# 🎮 PixelVault: Marketplace de Llaves Digitales

PixelVault es un ecosistema desarrollado en Django para la gestión y venta de videojuegos. Este proyecto documenta el proceso de construcción desde el modelado de datos hasta la implementación de un motor de búsqueda avanzado y un sistema de carrito de compras persistente.

---

## 🚀 SPRINT 1: Setup & Arquitectura Relacional

**🎯 Objetivo:** Cimentar una base de datos robusta capaz de manejar relaciones complejas entre entidades.

### Pasos realizados:
1. **Inicialización:** Creación del entorno virtual y estructura del proyecto mediante `django-admin startproject`.
2. **Modelado de Datos:** Se diseñaron modelos con relaciones técnicas:
   - **Many-to-Many (N:M):** Un videojuego puede pertenecer a varios géneros (RPG, Aventura, Acción).
   - **Foreign Keys (1:N):** Cada juego está ligado a una **Plataforma** (Nintendo Switch, PC) y una **Desarrolladora** (Game Freak, Nintendo).
3. **UUID:** Se sustituyeron los IDs incrementales (1, 2, 3) por identificadores únicos para proteger la integridad de las URLs.

**Ejemplo de registro en base de datos:**
> **Juego:** Pokémon Legends: Z-A  
> **Relaciones:** [Plataforma: Nintendo Switch] | [Géneros: RPG, Aventura]

---

## 🚀 SPRINT 2: Identidad Visual & Autenticación

**🎯 Objetivo:** Crear una interfaz inmersiva y un sistema de seguridad para usuarios.

### Pasos realizados:
1. **Estética Cyberpunk:** Implementación de CSS personalizado con paleta de colores neón (Cian `#00e5ff` y Morado `#6200ea`).
2. **Templates Dinámicos:** Creación de un `base.html` con bloques de contenido para evitar la duplicación de código.
3. **Control de Acceso:** Lógica para mostrar u ocultar el **Panel de Admin** solo si el usuario tiene permisos de `staff`.

**Lógica implementada:**
```html
{% if user.is_staff %}
   <a href="/admin/">⚙️ PANEL CONTROL</a>
{% endif %}
🚀 SPRINT 3: Motor de Búsqueda & UX Pro
🎯 Objetivo: Optimizar el descubrimiento de productos mediante filtros inteligentes.

Pasos realizados:
Consultas Complejas (Q Objects): Programamos el buscador para que no solo lea títulos, sino que rastree en tablas relacionadas.

Ficha Técnica Detallada: Desarrollo de la vista detalle_juego con carga optimizada (select_related) para mostrar Vendedor y Desarrollador sin lentitud.

Ejemplo de búsqueda:

Si el usuario busca "Nintendo", el sistema devuelve tanto juegos producidos por Nintendo como juegos cuya plataforma sea Nintendo Switch.

🚀 SPRINT 4: El Sistema de "La Bóveda" (Carrito)
🎯 Objetivo: Gestión de sesiones para la compra de múltiples artículos.

Pasos realizados:
Lógica de Sesiones: Implementación de un objeto Carrito que vive en la sesión del navegador del usuario.

CRUD de Carrito:

Agregar: Evita duplicados, sumando cantidad si el juego ya existe.

Eliminar: Limpieza de artículos específicos desde la vista de la Bóveda.

Vaciado: Limpieza total tras la confirmación de pago.

Ejemplo de flujo:

Usuario añade Pokémon Scarlet ($49.99).

El contador en la Navbar se actualiza a [1].

Al confirmar compra, se dispara la vista confirmacion.html y el carrito vuelve a [0].

🛠️ Stack Tecnológico
Lenguaje: Python 3.13

Framework: Django 5.2

Diseño: CSS Custom (Flexbox & Grid)

Base de Datos: SQLite3 (Desarrollo)

🔧 Instalación Rápida
Clonar: git clone https://github.com/tu-usuario/PixelVault.git

Instalar: pip install django

Migrar: python manage.py migrate

Ejecutar: python manage.py runserver