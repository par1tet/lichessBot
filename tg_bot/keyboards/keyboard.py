from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Игрок(с регистрацией)', callback_data='player')],
    [InlineKeyboardButton(text='Аноним(без регистрации)', callback_data='anon')],
])

pick_time_control = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='1м+0с', callback_data='time_conrtol_1'),InlineKeyboardButton(text='2м+1с', callback_data='time_conrtol_2'),InlineKeyboardButton(text='3м+0с', callback_data='time_conrtol_3')],
    [InlineKeyboardButton(text='3м+2с', callback_data='time_conrtol_4'),InlineKeyboardButton(text='5м+0с', callback_data='time_conrtol_5'),InlineKeyboardButton(text='5м+3с', callback_data='time_conrtol_6')],
    [InlineKeyboardButton(text='10м+0с', callback_data='time_conrtol_7'),InlineKeyboardButton(text='10м+5с', callback_data='time_conrtol_8'),InlineKeyboardButton(text='15м+10с', callback_data='time_conrtol_9')],
    [InlineKeyboardButton(text='30м+0с', callback_data='time_conrtol_10'),InlineKeyboardButton(text='30м+20с', callback_data='time_conrtol_11')],
])