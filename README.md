# Proyecto Taular - MVP

Este es un **MVP** (Minimum Viable Product) del proyecto **Taular**, una aplicación basada en Flask que gestiona clases, alumnos, tareas, pruebas, y exámenes. Cada clase está dividida en parciales y cada parcial contiene varias evaluaciones para los alumnos.

## Características principales

- **Gestión de clases**: Las clases están relacionadas con grados.
- **Parciales**: Cada clase se divide en 4 parciales, y en cada parcial se registran las evaluaciones (tareas, pruebas, exámenes).
- **Alumnos**: Los alumnos están asociados a un grado específico.
- **Puntajes**: Los puntajes por alumno se registran por cada tarea, prueba, y examen dentro de cada parcial.

## Estructura del proyecto

```
proyecto_taular-main/
│
├── app/
│   ├── __init__.py                    # Inicialización de la aplicación Flask y la base de datos
│   ├── models/
│   │   ├── __init__.py                # Registro de los modelos
│   │   ├── alumno_model.py            # Modelo de alumnos
│   │   ├── clase_model.py             # Modelo de clases
│   │   ├── examen_model.py            # Modelo de exámenes
│   │   ├── grado_model.py             # Modelo de grados
│   │   ├── parcial_model.py           # Modelo de parciales
│   │   ├── prueba_model.py            # Modelo de pruebas
│   │   └── tarea_model.py             # Modelo de tareas
│   └── seeds/
│       ├── alumno_seed.py             # Seed para alumnos
│       ├── clase_seed.py              # Seed para clases
│       ├── grado_seed.py              # Seed para grados
│       ├── parcial_seed.py            # Seed para parciales y sus evaluaciones
│       └── seed_all.py                # Ejecuta todos los seeds
│
├── migrations/                        # Migraciones de la base de datos (controladas por Flask-Migrate)
│   └── versions/
│       ├── <migration_files>.py       # Archivos de migraciones generados por Flask-Migrate
│
├── config.py                          # Configuraciones para el entorno (base de datos, etc.)
├── requirements.txt                   # Dependencias del proyecto
└── README.md                          # Este archivo
```

## Instalación

1. Clona el repositorio:
    ```bash
    git clone https://github.com/usuario/proyecto_taular.git
    ```
2. Crea un entorno virtual:
    ```bash
    python3 -m venv venv
    ```
3. Activa el entorno virtual:
    - En Linux/Mac:
        ```bash
        source venv/bin/activate
        ```
    - En Windows:
        ```bash
        venv\Scripts\activate
        ```
4. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```
5. Crea la base de datos y ejecuta las migraciones:
    ```bash
    flask db upgrade
    ```

6. Ejecuta la aplicación:
    ```bash
    flask run
    ```

## Seeds

Para poblar la base de datos con datos de prueba, ejecuta los seeds incluidos:

```bash
python -m app.seeds.seed_all
```

## Migraciones

Para crear nuevas migraciones al cambiar los modelos:

1. **Crear una nueva migración**:

    ```bash
    flask db migrate -m "Descripción del cambio"
    ```

2. **Aplicar la migración**:

    ```bash
    flask db upgrade
    ```

## Futuras mejoras

- Incorporación de chat de inteligencia artificial para evaluación y actualización del estado de estudiante.
- Implementar autenticación y roles para los usuarios (admin, maestros).
- Agregar lógica de reportes de rendimiento por alumno y clase.
- Optimización de la interfaz para la gestión de clases y parciales.

## Contacto

Si tienes preguntas o deseas contribuir, por favor contacta a [gerardo.belot@gmail.com].

---

## Actualizaciones recientes

### 1. Autenticación del API mediante tokens

Se ha implementado un sistema básico de autenticación para proteger los endpoints del API mediante un token de seguridad. Este token se debe enviar como parámetro en la URL o en el encabezado de las solicitudes para acceder a los endpoints protegidos.

#### Uso de la API con token

Para acceder a los endpoints del API, como obtener información de alumnos, debes incluir el token en la solicitud:

- Ejemplo de solicitud con token en la URL:
```bash
curl "http://localhost:5000/api/alumno?nombre=Juan&token=mi-token-secreto-dev"
```

### 2. Configuración de la aplicación

El archivo `config.py` ahora incluye claves de configuración separadas para los entornos de desarrollo, pruebas y producción. Asegúrate de definir las variables de entorno adecuadas para cada entorno.

- `SECRET_API_TOKEN`: Token de seguridad para acceder al API.
- `SQLALCHEMY_DATABASE_URI`: URI de la base de datos, configurable por entorno.

### 3. Nuevas características del API

El API ahora permite:
- **Consultar alumnos** por nombre o correo electrónico, incluyendo sus tareas, pruebas, y exámenes organizados por parciales.
- Protección de las rutas del API mediante un token de seguridad.

