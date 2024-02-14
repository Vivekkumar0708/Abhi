import asyncio
import datetime
from VIPMUSIC import app
from pyrogram import Client
from VIPMUSIC.utils.database import get_served_chats
from config import START_IMG_URL, AUTO_GCAST_MSG, AUTO_GCAST, LOGGER_ID
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

AUTO_GCASTS = "{AUTO_GCAST}" if AUTO_GCAST else False


MESSAGE = f"""๏ ᴛʜɪs ɪs ˹ʏᴜᴋᴋɪ x ᴍᴜsɪᴄ˼ ʏᴏᴜʀ ᴍᴜsɪᴄ ᴄᴏᴍᴘᴀɴɪᴏɴ!

➻ ᴅɪsᴄᴏᴠᴇʀ ᴀ ᴡᴏʀʟᴅ ᴏғ ᴇɴᴅʟᴇss ᴍᴜsɪᴄ ᴘᴏssɪʙɪʟɪᴛɪᴇs ᴡɪᴛʜ ˹Yukki ꭙ ᴍᴜsɪᴄ˼ ᴛʜᴇ ᴜʟᴛɪᴍᴀᴛᴇ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴜsɪᴄ ʙᴏᴛ ᴡɪᴛʜ sᴏᴍᴇ ᴀᴡᴇsᴏᴍᴇ ғᴇᴀᴛᴜʀᴇs.

• ᴘʀᴏᴍᴏᴛɪᴏɴ / ᴀᴅs ғʀᴇᴇ ʙᴏᴛ.
• 24 ʜʀ ᴜᴘᴛɪᴍᴇ.
• ʟᴀɢ ғʀᴇᴇ sᴍᴏᴏᴛʜ ᴍᴜsɪᴄ ᴇxᴘᴇʀɪᴇɴᴄᴇ.

ᴀᴅᴅ @{app.username} ɴᴏᴡ ᴀɴᴅ ʟᴇᴛ ᴛʜᴇ ᴍᴜsɪᴄ ᴛᴀᴋᴇ ᴏᴠᴇʀ ʏᴏᴜʀ ᴡᴏʀʟᴅ!"""

BUTTON = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ", url=f"https://t.me/{app.username}?startgroup=s&admin=delete_messages+manage_video_chats+pin_messages+invite_users")
        ]
    ]
)

caption = f"""{AUTO_GCAST_MSG}""" if AUTO_GCAST_MSG else MESSAGE

TEXT = """ᴀᴜᴛᴏ ɢᴄᴀsᴛ ɪs ᴇɴᴀʙʟᴇᴅ sᴏ ᴀᴜᴛᴏ ɢᴄᴀsᴛ/ʙʀᴏᴀᴅᴄᴀsᴛ ɪs ᴅᴏɪɴ ɪɴ ᴀʟʟ ᴄʜᴀᴛs ᴄᴏɴᴛɪɴᴜᴏᴜsʟʏ. \nɪᴛ ᴄᴀɴ ʙᴇ sᴛᴏᴘᴘᴇᴅ ʙʏ ᴘᴜᴛ ᴠᴀʀɪᴀʙʟᴇ [ᴀᴜᴛᴏ_ɢᴄᴀsᴛ = (ᴋᴇᴇᴘ ʙʟᴀɴᴋ & ᴅᴏɴᴛ ᴡʀɪᴛᴇ ᴀɴʏᴛʜɪɴɢ)]"""

async def send_text_once():
    try:
        await app.send_message(LOGGER_ID, TEXT)
    except Exception as e:
        pass

async def send_message_to_chats():
    try:
        chats = await get_served_chats()

        for chat_info in chats:
            chat_id = chat_info.get('chat_id')
            if isinstance(chat_id, int):  # Check if chat_id is an integer
                try:
                    await app.send_photo(chat_id, photo=START_IMG_URL, caption=caption, reply_markup=BUTTON)
                    await asyncio.sleep(10)  # Sleep for 10 second between sending messages
                except Exception as e:
                    pass  # Do nothing if an error occurs while sending message
    except Exception as e:
        pass  # Do nothing if an error occurs while fetching served chats

async def continuous_broadcast():
    await send_text_once()  # Send TEXT once when bot starts

    while True:
        if AUTO_GCAST:
            try:
                await send_message_to_chats()
            except Exception as e:
                pass

        # Wait for 100000 seconds before next broadcast
        await asyncio.sleep(43200)

# Start the continuous broadcast loop if AUTO_GCAST is True
if AUTO_GCAST:  
    asyncio.create_task(continuous_broadcast())    except Exception as e:
        pass

async def send_message_to_chats():
    try:
        chats = await get_served_chats()

        for chat_info in chats:
            chat_id = chat_info.get('chat_id')
            if isinstance(chat_id, int):  # Check if chat_id is an integer
                try:
                    await app.send_photo(chat_id, photo=START_IMG_URL, caption=caption, reply_markup=BUTTON)
                    await asyncio.sleep(100)  # Sleep for 100 second between sending messages
                except Exception as e:
                    pass  # Do nothing if an error occurs while sending message
    except Exception as e:
        pass  # Do nothing if an error occurs while fetching served chats

async def continuous_broadcast():
    await send_text_once()  # Send TEXT once when bot starts

    while True:
        if AUTO_GCAST:
            try:
                await send_message_to_chats()
            except Exception as e:
                pass

        # Wait for 100000 seconds before next broadcast
        await asyncio.sleep(100000)

# Start the continuous broadcast loop if AUTO_GCAST is True
if AUTO_GCAST:  
    asyncio.create_task(continuous_broadcast())
