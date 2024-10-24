import aiogram.fsm.state
import os

from aiogram import types

from config import BASE_DIR
from database.orm_query import *
from utils.buttons import *
from utils.states import States
from utils.texts import *

async def get_start(message, state, markup):
    photo_path = os.path.join(BASE_DIR, "utils", "images", "win_id.jpg")
    
    await message.answer_photo(
        photo=types.FSInputFile(path=photo_path),
        caption=start_text,
        reply_markup=markup
    )

    await state.set_state(States.WIN_REGISTRATION)