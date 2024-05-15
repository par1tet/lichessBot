from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
import tg_bot.keyboards.keyboard as kb

r = Router()

@r.message(Command('start'))
async def cmd_start(mess: Message):
    await mess.answer(f'''Здравствуйте, если бы вы хотели сейчас поиграть в шахматы, то вам бы пришлось заходить в бразуер искать сайт lichess.org, но этот бот способен помочь вам, он просто подключется к сайту и вы сможите играть.
                                    \nВыберете режим.''', reply_markup=kb.start)
    
@r.callback_query(F.data == 'anon')
async def start_game_like_a_anon(cb: CallbackQuery):
    await cb.message.edit_text(text='Окей, теперь выбери контроль времени.', reply_markup=kb.pick_time_control)