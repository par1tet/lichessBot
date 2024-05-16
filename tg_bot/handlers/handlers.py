from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
import tg_bot.keyboards.keyboard as kb
from lichess.main_parser import start_game_with_player, return_board

r = Router()

@r.message(Command('start'))
async def cmd_start(mess: Message):
    await mess.answer(f'''Здравствуйте, если бы вы хотели сейчас поиграть в шахматы, то вам бы пришлось заходить в бразуер искать сайт lichess.org, но этот бот способен помочь вам, он просто подключется к сайту и вы сможите играть.
                                    \nВыберете режим.''', reply_markup=kb.start)
    
@r.callback_query(F.data == 'anon')
async def start_game_like_a_anon(cb: CallbackQuery):
    await cb.message.edit_text(text='Окей, теперь выбери контроль времени.', reply_markup=kb.pick_time_control)
    
@r.callback_query(F.data.startswith('time_conrtol_'))
async def pick_control(cb: CallbackQuery):
    await cb.answer('')
    id = int(cb.data.split('_')[-1])
    print(id)
    start_game_with_player(id)
    board = return_board()
    await cb.message.edit_text(text = f'Игра началась, выберайте фигуры и ходите', reply_markup=await kb.board_game(board))
    
@r.callback_query(F.data.startswith('piece_choice_'))
async def pick_control(cb: CallbackQuery):
    await cb.answer('')

    print(cb.data)
    coords = [(cb.data).split('_')[-2], (cb.data).split('_')[-1]]
    print(coords)

    board = return_board()
    await cb.message.edit_text(text = f'Вы выбрали фигуру, делайте ход', reply_markup=await kb.board_game(board))