from kbds.inline import *

start_buttons = get_url_btns(
    btns={
        "💻 Зарегистрироваться": "https://1wimdx.life/casino/list/4?p=306v",
    }
)

success_reg_buttons = get_callback_btns(
    btns={
        "📚Инструкция": "instruction",
        "Получить сигнал💣": "get_signal",
        "🔙Вернуться в главное меню": "back",
    }
)

get_signal_buttons = get_callback_btns(
    btns={
        "Получить сигнал💣": "get_signal",
        "🔙Вернуться в главное меню": "back",
    }
)
