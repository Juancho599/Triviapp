from telegram import Update, ReplyKeyboardMarkup # type: ignore
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters # type: ignore
import random

# Lista de preguntas
preguntas = [
    {
        "pregunta": "¿Qué palabra clave se usa para definir una función en Python?",
        "opciones": ["func", "def", "lambda", "define"],
        "respuesta": "def"
    },
    {
        "pregunta": "¿Cuál de estos es un tipo de dato inmutable?",
        "opciones": ["lista", "diccionario", "conjunto", "tupla"],
        "respuesta": "tupla"
    },
    {
        "pregunta": "¿Qué imprime print(2 ** 3)?",
        "opciones": ["5", "6", "8", "9"],
        "respuesta": "8"
    },
]

user_state = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("¡Hola! Usa /trivia para empezar una trivia sobre Python 🐍")

async def trivia(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pregunta = random.choice(preguntas)
    user_id = update.effective_user.id
    user_state[user_id] = pregunta  # guardamos el estado

    # Mostrar opciones como botones
    reply_markup = ReplyKeyboardMarkup(
        [[opt] for opt in pregunta["opciones"]],
        one_time_keyboard=True,
        resize_keyboard=True
    )

    await update.message.reply_text(pregunta["pregunta"], reply_markup=reply_markup)

async def handle_response(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_answer = update.message.text

    if user_id in user_state:
        correct = user_state[user_id]["respuesta"]
        if user_answer.lower() == correct.lower():
            await update.message.reply_text("✅ ¡Correcto! Usa /trivia para otra pregunta.")
        else:
            await update.message.reply_text(f"❌ Incorrecto. La respuesta correcta era: {correct}")
        del user_state[user_id]  # borrar el estado

if __name__ == '__main__':
    app = ApplicationBuilder().token("8043848477:AAG8xjjXR-vLRvzrN__VgU2ovordq308E1s").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("trivia", trivia))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_response))

    print("Bot de trivia activo...")
    app.run_polling()
