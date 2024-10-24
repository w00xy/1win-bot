import aiogram.enums
import aiogram.types
import os
from typing import Union

from aiogram import Router, types, F
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from sqlalchemy.ext.asyncio import AsyncSession
from aiogram.enums import ParseMode

from utils.extra import get_start
from config import BASE_DIR
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
    
    win_id = await orm_check_id(session, message.from_user.id)
    print(win_id)
    if win_id:
        await get_start(message, state, registered_btns)
        return
    
    await get_start(message, state, start_buttons)

    
@start_router.message(States.WIN_REGISTRATION, F.text)
async def win_registration_bot(message: types.Message, session: AsyncSession, state: FSMContext):
    
    win_id = message.text
    
    try:
        win_id = int(win_id)
    except ValueError:
        await message.answer("Please enter a valid ID (numbers only).")
        return
    
    
    result = await orm_search_win_id(session, message.from_user.id, win_id)     
    
    if result:
        await message.delete()
        await message.answer(
            text=success_reg_text,
            reply_markup=success_reg_buttons,
        )
        return
    
    await message.answer(
        text=await no_reg_text(message.text),
    )
    

@start_router.callback_query(F.data == "instruction")
async def instucrion_handler(callback: types.CallbackQuery, session: AsyncSession, state: FSMContext):
    await state.clear()
    
    photo = types.FSInputFile(os.path.join(BASE_DIR, "utils", "images", "instruction.jpg"))

    try:
        await callback.message.delete()
    except:
        pass

    await callback.message.answer_photo(photo, instruction_text, reply_markup=get_signal_buttons, parse_mode=ParseMode.HTML)
    
