🏥 Cómo ejecutar el proyecto HospitalFormulario
📋 Requisitos previos

Python 3.8 o superior

pip (gestor de paquetes de Python)

Git (opcional, para clonar el repositorio)

⚙️ 1. Clonar el repositorio
git clone https://github.com/GerardoCL31/HospitalFormulario.git
cd HospitalFormulario

🧱 2. Crear y activar un entorno virtual
python -m venv venv


Activar el entorno:

En Windows:

venv\Scripts\activate


En macOS / Linux:

source venv/bin/activate

📦 3. Instalar dependencias

El proyecto usa Django, así que instala:

pip install django


(Otras dependencias se pueden agregar según sea necesario.)

🗃️ 4. Aplicar migraciones
python manage.py migrate

🚀 5. Ejecutar el servidor
python manage.py runserver


Luego abre tu navegador y entra a:
👉 http://localhost:8000

🔑 6. (Opcional) Crear un usuario administrador
python manage.py createsuperuser


Luego entra al panel en
👉 http://localhost:8000/admin
