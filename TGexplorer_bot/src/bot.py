from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from handlers.search import search_channels_and_groups
from handlers.media import search_multimedia_messages

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_text(f"Hi {user.first_name}! Use /search to find channels/groups or /media to find multimedia messages.")

async def search(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if context.args:
        keyword = ' '.join(context.args)
        results = await search_channels_and_groups(keyword)
        await update.message.reply_text(results)
    else:
        await update.message.reply_text("Please provide a keyword to search for.")

async def media(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if context.args:
        keyword = ' '.join(context.args)
        results = await search_multimedia_messages(keyword)
        await update.message.reply_text(results)
    else:
        await update.message.reply_text("Please provide a keyword to search for multimedia messages.")

def main() -> None:
    app = ApplicationBuilder().token("YOUR_TELEGRAM_BOT_TOKEN").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("search", search))
    app.add_handler(CommandHandler("media", media))
    app.run_polling()

if __name__ == "__main__":
    main()