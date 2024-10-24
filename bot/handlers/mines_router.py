import asyncio
from datetime import timedelta
import os
import random
import time
from typing import Union

from aiogram import Router, types, F
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from sqlalchemy.ext.asyncio import AsyncSession
from aiogram.enums import ParseMode

from config import BASE_DIR, IMAGE_FOLDER
from database.orm_query import *
from utils.buttons import *
from utils.states import States
from utils.texts import *
from utils.states import Signal

mines_router = Router()


@mines_router.callback_query(F.data == "get_signal")
async def start_bot(call: types.CallbackQuery, session: AsyncSession, state: FSMContext):
    print(f"ПРОБУЕМ ПОЛУЧИТЬ СИГНАЛ\n\n\n")
    await call.answer()
    await state.set_state(Signal.WAIT_FOR_SIGNAL)
    
    user_id = call.from_user.id
    
    last_sent_time, sent_images = await orm_user_data(session, user_id)
    
    print(f"USER DATA - {last_sent_time}, {sent_images}\n\n\n")
    await send_random_image(call, session, last_sent_time, sent_images)
    

async def send_random_image(call: types.CallbackQuery, session: AsyncSession, last_sent_time, sent_images):
    current_time = datetime.datetime.now()
    cool_down_period = timedelta(seconds=20)

    print(f"OSTATOK VREMENI - ", last_sent_time - current_time)
    print(last_sent_time)
    print(current_time)
    # Проверяем можно ли отправлять новое изображение
    if last_sent_time and current_time - last_sent_time < cool_down_period:
        time_left = cool_down_period - (current_time - last_sent_time)
        print(f"TIME LEFT - {time_left}")
        await call.message.answer(await wait_text(time_left))
        return
    
    generating_msg = await call.message.answer(
        text=generating_text
    )

    # Список всех изображений в директории
    all_images = [f for f in os.listdir(IMAGE_FOLDER) if f.endswith(('.jpg', '.png'))]

    if sent_images is not None:
        # Получаем список доступных для отправки изображений 
        unsent_images = [img for img in all_images if img not in sent_images]
        print(f"ОСТАВШИЕЙСЯ ИЗОБРАЖЕНИЯ - ", unsent_images)
    else:
        unsent_images = all_images
        sent_images = []

    if not unsent_images:  
        unsent_images = all_images 
        sent_images = []

    random_image = random.choice(unsent_images)
    
    # Обновляем данные пользователя
    sent_images.append(random_image)
    sent_images = json.dumps(sent_images)
    
    await orm_update_data(session, call.from_user.id, current_time, sent_images)

    await session.commit()

    # Отправляем изображение пользователю
    
    photo = types.FSInputFile(os.path.join(IMAGE_FOLDER, random_image))
    
    await asyncio.sleep(random.uniform(0.8, 2.3))
    await call.bot.delete_message(chat_id=call.from_user.id, message_id=generating_msg.message_id)
    await call.message.answer_photo(
        photo=photo,
        caption=await get_signal_text(),
        reply_markup=success_reg_buttons,
    )