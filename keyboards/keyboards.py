from aiogram import types


def send_phone(one_time=False):
    '''Записываем телефон'''
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=one_time,
                                       input_field_placeholder='Нажмите кнопку ниже',
                                       resize_keyboard=True)
    btn_phone = types.KeyboardButton(text='📞 Передать номер телефона',
                                     request_contact=True)
    markup.row(btn_phone)
    return markup


def add_step_keyboard(array: list, one_time=False, row_width=2):
    '''Обычные кнопки для step_handler
    Принимает список, возвращает кнопки
    one_time(одноразовая клавиатура), row_width(ряды кнопок)'''
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                       one_time_keyboard=one_time,
                                       row_width=row_width)
    markup.add(*array)
    return markup


def infostart_auth_keyboard(uuid):
    is_url = "https://infostart.ru"
    auth_url = f"{is_url}/auth/tg/?a=cQ&h={uuid}"
    keyboard = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton('Авторизоваться на infostart.ru', url=auth_url)
    keyboard.add(button)
    return keyboard


# def inline_keyboard(array: list, row_width=1):
#     '''Inline кнопки
#     Принимает текст кнопок списком, callback.
#     Возвращает кнопки'''
#     markup = types.InlineKeyboardMarkup(row_width=row_width)
#     for text in array:
#         button = types.InlineKeyboardButton(text=text,
#                                             callback_data=text)
#         markup.add(button)

#     return markup
