# Sistema de Gestión de Encuestas sobre Alcohol y Salud

Este proyecto es un sistema de gestión de encuestas relacionadas con el consumo de alcohol y la salud. Proporciona una interfaz gráfica de usuario (GUI) para agregar, actualizar, eliminar y ver registros de encuestas. El sistema también permite exportar datos a Excel y visualizar datos a través de gráficos.

## Características

- Agregar, actualizar y eliminar registros de encuestas
- Ver registros de encuestas en una tabla
- Exportar datos de encuestas a Excel
- Visualizar datos a través de gráficos
- Interfaz fácil de usar con temas de `ttkbootstrap`

## Requisitos

- Python 3.x
- `ttkbootstrap`
- `pandas`
- `matplotlib`
- `pymysql`

## Instalación

1. Clona el repositorio:
    ```sh
    git clone https://github.com/tuusuario/turepositorio.git
    cd turepositorio
    ```

2. Instala los paquetes de Python requeridos:
    ```sh
    pip install ttkbootstrap pandas matplotlib pymysql
    ```

3. Configura tu base de datos MySQL y actualiza los detalles de conexión en `database.py`:
    ```python
    self.conn = pymysql.connect(
        host="localhost",
        user="tuusuario",
        password="tucontraseña",
        database="ENCUESTAS"
    )
    ```

## Uso

1. Ejecuta la aplicación:
    ```sh
    python main.py
    ```

2. Usa la GUI para gestionar los registros de encuestas:
    - **Agregar Registro**: Rellena el formulario y haz clic en "Agregar Registro".
    - **Actualizar Registro**: Selecciona un registro, actualiza los campos del formulario y haz clic en "Actualizar Registro".
    - **Eliminar Registro**: Selecciona un registro y haz clic en "Eliminar Registro".
    - **Ver Registros**: Haz clic en "Ver Registros" para actualizar la tabla.
    - **Exportar a Excel**: Usa el menú "Archivo" para exportar datos a Excel.
    - **Mostrar Gráfico**: Haz clic en "Mostrar Gráfico" para visualizar datos.

## Estructura de Archivos

- `main.py`: Punto de entrada de la aplicación.
- `ui.py`: Contiene la implementación de la GUI.
- `database.py`: Maneja las operaciones de la base de datos.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT.
