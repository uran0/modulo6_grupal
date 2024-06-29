=== README.txt ===

Bienvenido a TeLoVendo

Este archivo README proporciona una breve guía sobre las funcionalidades de la aplicación TeLoVendo y cómo puedes levantarla en tu servidor local.

1. Funcionalidades de la Aplicación:
   - Registro de usuarios con diferentes roles: admin, staff y user.
   - Inicio de sesión y cierre de sesión con autenticación.
   - Perfiles de usuario con información personalizable (teléfono, dirección).
   - Páginas de perfil específicas para admin, staff y user con permisos diferenciados.
   - Plantilla base con diseño utilizando Bootstrap 5.

2. Requisitos Previos:
   - Python 3.x instalado en tu sistema.
   - Entorno virtual (recomendado) para instalar las dependencias del proyecto.

3. Instalación y Configuración:
   - Clona este repositorio desde GitHub:
     ```
     git clone https://github.com/tu_usuario/telovendo.git
     cd telovendo
     ```

   - Instala las dependencias usando pip:
     ```
     pip install -r requirements.txt
     ```

4. Configuración de la Base de Datos:
   - Asegúrate de tener configurada tu base de datos en `settings.py`.
   - Realiza las migraciones necesarias para crear las tablas en la base de datos:
     ```
     python manage.py makemigrations
     python manage.py migrate
     ```

5. Ejecutar la Aplicación:
   - Inicia el servidor de desarrollo de Django:
     ```
     python manage.py runserver
     ```

6. Acceder a la Aplicación:
   - Abre tu navegador web y accede a la siguiente URL:
     ```
     http://localhost:8000/
     ```

7. Notas Adicionales:
   - Asegúrate de configurar adecuadamente las URLs y vistas según las necesidades de tu proyecto.
   - Personaliza las plantillas HTML y los estilos CSS según los requisitos de diseño de tu aplicación.


