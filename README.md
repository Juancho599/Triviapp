# Triviapp
Bot de Trivia de Python

Es un bot de Telegram que realiza una trivia sobre Python.
El bot elige preguntas al azar, muestra las opciones como botones y valida la respuesta del usuario.

Funcionalidades:

Comando /start → da la bienvenida al usuario.

Comando /trivia → inicia una trivia con una pregunta aleatoria.

Muestra opciones como botones de respuesta.

Informa si la respuesta es correcta o incorrecta y muestra la correcta.

Tecnologías utilizadas:

Python 3.10+

python-telegram-bot (telegram y telegram.ext)

Random para elegir preguntas aleatorias


Instalación y uso:

Clonar este repositorio:

git clone https://github.com/Juancho599/telegram-python-trivia-bot.git
cd telegram-python-trivia-bot


Crear un entorno virtual (opcional):

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows


Instalar dependencias:

pip install python-telegram-bot


Crear un bot en Telegram a través de @BotFather
 y obtener el token.

Reemplazar en el código el token de ejemplo por el tuyo:

app = ApplicationBuilder().token( "TU_TOKEN_AQUI" ).build()


Ejecutar el bot con:

python bot.py


Abrir Telegram y probarlo con los comandos:

/start

/trivia

Bot en funcionamiento: 

![WhatsApp Image 2025-09-13 at 00 54 08](https://github.com/user-attachments/assets/e94aeeb7-3006-40fe-b2c3-4c4c69184dc8)


Mejoras a futuro:

Aumentar la cantidad de preguntas

Seleccionar dificultad (Facil - Avanzado - Experto)


