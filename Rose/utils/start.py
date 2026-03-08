from pyrogram.types import Message

async def get_private_rules(client, message: Message):
    await message.reply_text("Welcome to Rose bot! Use /help for commands.")

async def get_learn(client, message: Message):
    await message.reply_text("Rose bot is running. Use /help for commands.")