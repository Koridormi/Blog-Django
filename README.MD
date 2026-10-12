# Mi Blog · Django

Blog personal creado con Django. El proyecto incluye registro de usuarios, autenticación y un CRUD de publicaciones con imágenes opcionales, acompañado de una interfaz minimalista y responsive.

## Funcionalidades

- Inicio y página acerca del blog.
- Listado de publicaciones, ordenadas desde la más reciente, y página de lectura individual.
- Registro, inicio y cierre de sesión.
- Creación de publicaciones para usuarios autenticados.
- Edición y eliminación de publicaciones únicamente por su autor.
- Imágenes opcionales de hasta 5 MB, con posibilidad de reemplazarlas o quitarlas al editar.
- Panel de administración de Django para gestionar usuarios y publicaciones.
- Diseño mobile first con imágenes completas, sin recortes.
- SEO básico: títulos, descripciones, URL canónica y metadatos Open Graph en el detalle de cada publicación.
- Accesibilidad básica: HTML semántico, etiquetas de formulario, texto alternativo, foco visible y enlace para saltar al contenido.
- Plantillas para errores 403, 404 y 500.

## Tecnologías y requisitos

| Herramienta | Uso |
| --- | --- |
| Python 3.14 | Versión utilizada en el entorno de desarrollo; verificada con Python 3.14.3. |
| Django | Rutas, vistas, modelos, formularios, autenticación y administración. |
| SQLite | Base de datos local, sin servidor adicional. |
| Pillow | Procesamiento y validación de los archivos de imagen. |
| python-dotenv | Lectura de las variables de entorno desde `.env`. |
| HTML y CSS | Plantillas Django y estilos, sin proceso de compilación frontend. |

Las versiones de las dependencias están fijadas en [`requirements.txt`](The-Blog-Django/requirements.txt). No es necesario instalar Node.js ni ejecutar npm para iniciar el sitio.

## Estructura del proyecto

```text
Blog-Django/
├── README.MD
├── LICENSE
└── The-Blog-Django/
    ├── manage.py
    ├── requirements.txt
    ├── .env.example
    ├── config/
    │   ├── settings.py          # Configuración del proyecto
    │   ├── urls.py              # Rutas principales
    │   ├── asgi.py
    │   └── wsgi.py
    ├── accounts/               # Registro y autenticación
    │   ├── views.py
    │   └── urls.py
    ├── pages/                  # Inicio y acerca del blog
    │   ├── views.py
    │   └── urls.py
    ├── posts/                  # Publicaciones y carga de imágenes
    │   ├── models.py
    │   ├── forms.py
    │   ├── views.py
    │   ├── urls.py
    │   ├── admin.py
    │   └── migrations/
    ├── templates/
    │   ├── base.html
    │   ├── 403.html
    │   ├── 404.html
    │   ├── 500.html
    │   ├── pages/
    │   ├── posts/
    │   └── registration/
    ├── static/
    │   ├── assets/
    │   │   ├── icon.ico
    │   │   └── logo/logo.png
    │   └── css/
    │       ├── normalize.css
    │       └── main.css
    ├── media/posts/            # Imágenes subidas; se genera al cargar archivos
    ├── db.sqlite3              # Base de datos; se genera con las migraciones
    ├── .env                    # Configuración local
    └── .venv/                  # Entorno virtual local
```

El árbol resume los archivos principales. `.env`, `.venv/`, `db.sqlite3` y `media/` están excluidos de Git. Las migraciones sí forman parte del proyecto.

## Instalación local en Windows

Los comandos siguientes están pensados para PowerShell, con Python 3.14 instalado. Usan directamente el intérprete del entorno virtual, por lo que no necesitas activar `.venv`.

### 1. Entrar en el proyecto

Después de clonar o descargar el repositorio, abre una terminal en la carpeta `Blog-Django` y ejecuta:

```powershell
cd The-Blog-Django
```

Los pasos siguientes se ejecutan desde esta carpeta, donde se encuentra `manage.py`.

### 2. Crear el entorno virtual e instalar las dependencias

```powershell
py -3.14 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

### 3. Preparar las variables de entorno

Este comando crea `.env` a partir de `.env.example`, reemplaza la clave de ejemplo por una clave aleatoria y conserva el archivo si ya existe:

```powershell
.\.venv\Scripts\python.exe -c "from pathlib import Path; from django.core.management.utils import get_random_secret_key; target = Path('.env'); target.exists() or target.write_text(Path('.env.example').read_text(encoding='utf-8').replace('Tu_Clave_Secreta_Generada', get_random_secret_key()), encoding='utf-8')"
```

El archivo contiene estas variables:

| Variable | Descripción | Valor local |
| --- | --- | --- |
| `DJANGO_SECRET_KEY` | Clave utilizada por Django para firmar datos. | Generada por el comando anterior. |
| `DJANGO_DEBUG` | Activa el modo de desarrollo y la entrega local de imágenes. | `True` |
| `DJANGO_ALLOWED_HOSTS` | Hosts permitidos, separados por comas. | `127.0.0.1,localhost` |

La clave generada debe permanecer en tu `.env` local y no publicarse en el repositorio.

### 4. Aplicar las migraciones

```powershell
.\.venv\Scripts\python.exe manage.py migrate
```

Este paso crea la base de datos SQLite y aplica las tablas de usuarios, sesiones y publicaciones, incluido el campo de imagen.

### 5. Iniciar el servidor

```powershell
.\.venv\Scripts\python.exe manage.py runserver
```

Abre [http://127.0.0.1:8000/](http://127.0.0.1:8000/) en el navegador. Para detener el servidor, presiona `Ctrl+C` en la terminal.

## Iniciar el proyecto después de instalarlo

Abre una terminal en `The-Blog-Django` y ejecuta:

```powershell
.\.venv\Scripts\python.exe manage.py runserver
```

Si actualizaste el repositorio y hay nuevas dependencias o migraciones, ejecuta antes:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe manage.py migrate
```

## Uso del blog

1. Visita **Crear cuenta** para registrar un usuario.
2. Inicia sesión y entra en **Publicaciones**.
3. Selecciona **Crear publicación** y completa el título y la descripción.
4. Si quieres, adjunta una imagen de hasta 5 MB.
5. Desde el detalle de tus propias publicaciones puedes editarlas o eliminarlas. Al editar también puedes reemplazar la imagen o marcar **Limpiar** para quitarla de la publicación.

Los visitantes pueden leer las publicaciones sin iniciar sesión. El cierre de sesión y las operaciones de guardado o eliminación utilizan formularios POST con protección CSRF.

### Panel de administración

Para crear un usuario con acceso al panel:

```powershell
.\.venv\Scripts\python.exe manage.py createsuperuser
```

Con el servidor iniciado, visita [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) e inicia sesión con ese usuario.

## Rutas principales

| Ruta | Página o acción |
| --- | --- |
| `/` | Inicio. |
| `/acerca-de/` | Acerca del blog. |
| `/posts/` | Listado de publicaciones. |
| `/posts/<id>/` | Detalle de una publicación. |
| `/posts/create/` | Crear una publicación; requiere sesión. |
| `/posts/<id>/editar/` | Editar una publicación propia. |
| `/posts/<id>/eliminar/` | Confirmar la eliminación de una publicación propia. |
| `/accounts/sign-up/` | Registro de usuario. |
| `/accounts/login/` | Inicio de sesión. |
| `/accounts/logout/` | Cierre de sesión mediante POST. |
| `/admin/` | Administración de Django. |

## Archivos estáticos e imágenes

- `static/` contiene los archivos del sitio: CSS, favicon y logo.
- `media/posts/` contiene las imágenes adjuntadas a las publicaciones. Django crea las carpetas necesarias al guardar archivos.
- En desarrollo, `runserver` sirve los estáticos y, con `DJANGO_DEBUG=True`, las imágenes de `media/`.
- Los títulos, descripciones SEO, textos alternativos y metadatos de las publicaciones se generan desde las plantillas, sin configurar cada página manualmente.
- Para conservar los datos de una instalación, respalda tanto `db.sqlite3` como `media/`.

## Validación

Para comprobar la configuración del proyecto:

```powershell
.\.venv\Scripts\python.exe manage.py check
```

Para ejecutar las pruebas Django disponibles:

```powershell
.\.venv\Scripts\python.exe manage.py test
```

Actualmente, los archivos `tests.py` de las aplicaciones son plantillas sin casos de prueba implementados. No hay una suite Playwright configurada en este repositorio.

## Consideraciones de despliegue

Esta guía describe el entorno local. `runserver` es un servidor de desarrollo.

En producción se necesita un servidor WSGI o ASGI, `DJANGO_DEBUG=False`, los hosts reales en `DJANGO_ALLOWED_HOSTS` y una configuración para servir los estáticos y las imágenes subidas. El proyecto todavía no incluye una configuración completa de despliegue ni `STATIC_ROOT`; la publicación requiere preparar ese entorno por separado.

## Licencia

Este proyecto utiliza la [licencia MIT](LICENSE).