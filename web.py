import logging
from aiohttp import web
from aiogram import Bot, types, md

from core import settings
from utils import bd
from texts import texts, text_buttons as texts_btn
from keyboards import keyboards as kb

logging.basicConfig(level=logging.DEBUG)

# img_dir = 'data/'

# async def handle_qr_question(request):
#     quest_id = request.match_info.get('quest_id', "")
#     text = "Quest ID: " + quest_id
#     raise redirect_to_bot()


async def handle_index(request):
    raise redirect_to_bot()


def redirect_to_bot():
    return web.HTTPFound(f"https://t.me/{settings.TELEGRAM_BOT_NAME}")


async def send_tg_message(chat_id, text, reply_markup=None):
    bot = Bot(token=settings.tg_token, parse_mode=types.ParseMode.MARKDOWN_V2)
    await bot.send_message(chat_id, text, reply_markup=reply_markup)

app = web.Application()
app.add_routes([web.get('/', handle_index),
                web.get('/questionnaire-bot', handle_index),
                # web.get('/questionnaire-bot/{quest_id}', handle_qr_question)
                ])

if __name__ == '__main__':
    web.run_app(app)
