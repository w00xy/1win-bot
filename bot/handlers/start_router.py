import os
from typing import Union

from aiogram import Router, types, F
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from sqlalchemy.ext.asyncio import AsyncSession

from bot.config import BASE_DIR
from database.orm_query import *
from utils.buttons import *
from utils.states import States
from utils.texts import *

start_router = Router()


@start_router.message(CommandStart())
async def start_bot(message: types.Message, session: AsyncSession, state: FSMContext):
    try:
        await orm_add_user(session, message.from_user.id)
    except:
        pass
    
    photo_path = os.path.join(BASE_DIR, "utils", "images", "win_id.jpg")
    
    await message.answer_photo(
        photo=types.FSInputFile(path=photo_path),
        caption=start_text,
        reply_markup=start_buttons
    )

    await state.set_state(States.WIN_REGISTRATION)
    
    
@start_router.message(States.WIN_REGISTRATION, F.text)
async def win_registration_bot(message: types.Message, session: AsyncSession, state: FSMContext):
    await message.answer(
        text=no_reg_text,
    )
    
    