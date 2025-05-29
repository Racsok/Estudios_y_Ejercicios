import logging
from telegram import Update, ForceReply
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from handlers.search import search
from handlers.media import search_media

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}! Use /search [keyword] to find channels/groups or /media [keyword] to find multimedia.",
        reply_markup=ForceReply(selective=True),
    )

# async def search(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     if context.args:
#         keyword = ' '.join(context.args)
#         print(f"Searching for: {keyword}")
#         results = await search_channels_and_groups(keyword=keyword)
#         await update.message.reply_text(results)
#     else:
#         await update.message.reply_text("Please provide a keyword to search.")

# async def media(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     if context.args: 
#         keyword = ' '.join(context.args)
#         results = await search_media(keyword=keyword)
#         await update.message.reply_text(results)
#     else:
#         await update.message.reply_text("Please provide a keyword to search for multimedia.")

def main() -> None:
    app = ApplicationBuilder().token("7703907322:AAH8qh_UGZESmXJisYkRaxsw0AhgoHnpFf8").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("search", search))
    app.add_handler(CommandHandler("media", search_media))
    app.run_polling()

if __name__ == "__main__":
    main()