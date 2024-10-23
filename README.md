🌍 GaiaKm

GaiaKm es un programa sencillo que realiza la conversión de kilómetros en La Menorquina para asegurar que la tarifa se calcule correctamente a 0,26 €/km, ya que el sistema solo detecta una tarifa de 0,19 €/km.

⚙️ Instalación

Requisitos

Asegúrate de tener instalado Python en tu sistema. Puedes verificarlo ejecutando el siguiente comando:

python3 --version

Si no tienes Python instalado, puedes instalarlo usando:

sudo apt-get update
sudo apt-get install python3

Clonar el repositorio

Primero, clona este repositorio en tu máquina local:

git clone https://github.com/wavecheff/gaiaKm.git

Crear y activar un entorno virtual (opcional)

Es recomendable usar un entorno virtual para aislar las dependencias del proyecto. Para crear y activar un entorno virtual, ejecuta los siguientes comandos:

En Linux/Mac:

cd gaiaKm
python3 -m venv venv
source venv/bin/activate

En Windows:

venv\Scripts\activate

Instalar dependencias

Instala las dependencias necesarias utilizando el archivo requirements.txt:

pip install -r requirements.txt

▶️ Ejecución del programa

Para ejecutar GaiaKm, utiliza el siguiente comando:

python gaia_km.py

Esto abrirá la interfaz gráfica donde puedes introducir el número de kilómetros que te pagan a 0,19 €/km, y el programa calculará cuántos deberías declarar para obtener el importe correcto a 0,26 €/km.

🧩 Funcionalidades

	•	Conversión automática: Calcula cuántos kilómetros deberías declarar a 0,19 €/km para recibir el importe correcto a 0,26 €/km.
	•	Interfaz gráfica amigable.
	•	Fácil de usar: Pensado para cualquier usuario sin necesidad de conocimientos técnicos avanzados.

📄 Licencia

Este proyecto está bajo la licencia MIT. Para más detalles, consulta el archivo LICENSE.
