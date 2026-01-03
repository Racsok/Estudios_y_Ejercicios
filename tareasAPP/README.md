# Tkinter Tareas App

Este proyecto es una aplicación de gestión de tareas desarrollada en Python utilizando Tkinter para la interfaz gráfica y SQLite para el almacenamiento persistente de datos. La aplicación permite a los usuarios crear, editar y eliminar tareas, que se representan visualmente como tarjetas en la interfaz.

## Estructura del Proyecto

```
tkinter-tareas-app
├── src
│   ├── main.py                # Punto de entrada de la aplicación
│   ├── db
│   │   └── connection.py      # Módulo para manejar la conexión a la base de datos
│   ├── models
│   │   └── tarea.py           # Modelo que representa una tarea
│   ├── ui
│   │   ├── task_card.py       # Clase que representa una tarjeta de tarea
│   │   └── task_board.py      # Clase que gestiona el tablero de tareas
│   └── utils
│       └── color_utils.py     # Funciones para determinar colores de tareas
├── requirements.txt           # Dependencias del proyecto
└── README.md                  # Documentación del proyecto
```

## Instalación

1. Clona el repositorio o descarga el código fuente.
2. Navega al directorio del proyecto.
3. Instala las dependencias necesarias ejecutando:

```
pip install -r requirements.txt
```

## Uso

Para ejecutar la aplicación, utiliza el siguiente comando:

```
python src/main.py
```

## Funcionalidades

- **Crear Tareas**: Permite a los usuarios añadir nuevas tareas a la lista.
- **Editar Tareas**: Los usuarios pueden modificar el título y la descripción de las tareas existentes.
- **Eliminar Tareas**: Las tareas pueden ser eliminadas de la lista.
- **Interfaz Interactiva**: Las tareas se muestran como tarjetas que pueden ser movidas dentro de la interfaz.
- **Colores de Importancia**: Las tarjetas cambian de color según su nivel de importancia, desde rojo (muy importante) hasta verde (menos importante).

## Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar la aplicación, por favor abre un issue o envía un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT.