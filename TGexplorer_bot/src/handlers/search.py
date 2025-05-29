

from telegram import Update
from telegram.ext import ContextTypes
from utils.telegram_search import search_channels_and_groups, search_multimedia_messages


async def search(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not context.args:
        await update.message.reply_text("Please provide a keyword to search.")
        return

    keyword = ' '.join(context.args)
    
    channels_and_groups = await search_channels_and_groups("7703907322:AAH8qh_UGZESmXJisYkRaxsw0AhgoHnpFf8",keyword)
    #multimedia_messages = await search_multimedia_messages("7703907322:AAH8qh_UGZESmXJisYkRaxsw0AhgoHnpFf8",keyword)

    response = "Search Results:\n\n"

    if channels_and_groups:
        response += "Channels and Groups:\n"
        for item in channels_and_groups:
            response += f"- {item}\n"
    else:
        response += "No channels or groups found.\n"

    # if multimedia_messages:
    #     response += "\nMultimedia Messages:\n"
    #     for message in multimedia_messages:
    #         response += f"- {message}\n"
    # else:
    #     response += "No multimedia messages found."

    await update.message.reply_text(response)