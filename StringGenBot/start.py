from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""✇︙ مرحـباً بـك عزيـزي  {msg.from_user.mention} فـي بـوت اسـتـخـراج الـجـلـسـات لسـورس لــورد
✇︙ يمكنك استخراج الجلسات الـتالية
✇︙ بايروجرام v1 للميوزك والتليثون الإصدار القديم
✇︙ بايروجرام v2 للميوزك والتليثون الاصدار الجديد
✇︙ تريمكس (تليثون)  للحسابات & للبوتات

✇︙ بواسطـة : [𝐒𝐎𝐔𝐑𝐂𝐄 𝐋𝐎𝐑𝐃](t.me/m_r_zc) """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="‹ بـدء إسـتـخـراج جـلـسـة ›", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("𝚂𝙾𝚄𝚁𝙲𝙴 𝙻𝙾𝚁𝙳 𝙲𝙷", url="https://t.me/m_r_zc"),
                    InlineKeyboardButton("𝙼𝚈 𝚆𝙾𝚁𝙻𝙳 𝙲𝙷", url="https://t.me/oooj30")
                ],
                [
                    InlineKeyboardButton("ᯓ 𝙳𝙴𝚅 𝙻𝙾𝚁𝙳 ❥", user_id=6443044496)
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
