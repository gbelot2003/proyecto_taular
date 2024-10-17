
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
├── run.py                             # Archivo principal para ejecutar la aplicación
├── tests/
│   └── test_app.py                    # Pruebas unitarias
└── README.md                          # Este archivo
```

## Requisitos

- Python 3.12+
- Flask
- SQLAlchemy
- Flask-Migrate

## Instalación

1. **Clona el repositorio**:

    ```bash
    git clone <URL del repositorio>
    cd proyecto_taular-main
    ```

2. **Crea y activa un entorno virtual**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    ```

3. **Instala las dependencias**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Configura la base de datos**:

    Asegúrate de tener configurada correctamente tu base de datos en `config.py`.

5. **Crea las tablas en la base de datos**:

    ```bash
    flask db upgrade
    ```

6. **Seed de la base de datos**:

    Para poblar la base de datos con datos de prueba:

    ```bash
    python app/seeds/seed_all.py
    ```

7. **Ejecuta la aplicación**:

    ```bash
    python run.py
    ```

    La aplicación estará disponible en `http://127.0.0.1:5000/`.

## Estructura de la base de datos

- **Clases**: Están asociadas a un **Grado** y se dividen en 4 **Parciales**.
- **Parciales**: Cada **Parcial** tiene varias **Tareas**, **Pruebas**, y un **Examen** para cada alumno.
- **Alumnos**: Pertenecen a un grado específico y tienen un puntaje por cada evaluación en un parcial.

## Pruebas

El proyecto incluye un conjunto básico de pruebas unitarias. Para ejecutar las pruebas:

```bash
pytest
```

## Migraciones

Para generar nuevas migraciones al cambiar los modelos:

1. **Crear una nueva migración**:

    ```bash
    flask db migrate -m "Descripción del cambio"
    ```

2. **Aplicar la migración**:

    ```bash
    flask db upgrade
    ```

## Futuras mejoras

- Incorporacion de chat de inteligencia artificial para evaluación y actualización del estado de estudiante.
- Implementar autenticación y roles para los usuarios (admin, maestros).
- Agregar lógica de reportes de rendimiento por alumno y clase.
- Optimización de la interfaz para la gestión de clases y parciales.

## Contacto

Si tienes preguntas o deseas contribuir, por favor contacta a [gerardo.belot@gmail.com].

---

Con este **README** puedes guiar a otros usuarios o desarrolladores para entender, instalar y ejecutar el proyecto.