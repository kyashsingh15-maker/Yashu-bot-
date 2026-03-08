from pyrogram.types import InlineKeyboardButton

def paginate_modules(page, modules, prefix):
    buttons = []
    for name in sorted(modules.keys()):
        buttons.append([InlineKeyboardButton(name, callback_data=f"{prefix}_{name}")])
    return buttons