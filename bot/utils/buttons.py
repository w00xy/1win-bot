from config import REF_URL
from kbds.inline import *

start_buttons = get_url_btns(
    btns={
        "💻 Зарегистрироваться": f"{REF_URL}",
    }
)

registered_btns = get_callback_btns(
    btns={
        "📚Инструкция": "instruction",
        "Получить сигнал💣": "get_signal",
    }
)

success_reg_buttons = get_callback_btns(
    btns={
        "📚Инструкция": "instruction",
        "Получить сигнал💣": "get_signal",
    }
)

get_signal_buttons = get_callback_btns(
    btns={
        "Получить сигнал💣": "get_signal",
    }
)
