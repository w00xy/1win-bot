from aiogram.fsm.state import State, StatesGroup

class States(StatesGroup):
    WIN_REGISTRATION = State()
    DELAY_SIGNAL = State()