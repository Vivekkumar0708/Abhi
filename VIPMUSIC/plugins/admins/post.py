from pyrogram import Client, filters
from VIPMUSIC import app
from config import OWNER_ID
from pyrogram.types import Message


@app.on_message(filters.command(["post"], prefixes=["/", "."]) & filters.user(OWNER_ID))
async def copy_messages(_, message):

    if message.reply_to_message:
      
        destination_group_id = -1002097153537

        
        await message.reply_to_message.copy(destination_group_id)
        await message.reply("ᴅᴏɴᴇ")