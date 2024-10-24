import datetime
import json
from sqlite3 import IntegrityError
from typing import List, Tuple

from sqlalchemy import select, delete, insert, update
import sqlalchemy
from sqlalchemy.ext.asyncio import AsyncSession

from database.models import User, WinUser



async def orm_add_user(session: AsyncSession, user_id: int):
  """Adds a new user to the database if they don't already exist.

  Args:
  session: Database session.
  user_id: User ID.
  """
  try:
    # Проверка, существует ли пользователь в базе данных
    result = await session.execute(select(User).where(User.user_id == user_id))
    user = result.scalars().first()

    if user is not None:
      # Пользователь уже существует, поэтому возвращаем без изменений
      return
    
    # Если пользователь не найден, создаем нового
    new_user = User(user_id=user_id)
    new_user.sent_images = json.dumps(new_user.sent_images)
    new_user.last_send_time = datetime.datetime.now()
    session.add(new_user)
    await session.commit()

  except Exception as e:
    # Обработка любых других ошибок SQLAlchemy
    print(f"An error occurred: {e}")
    await session.rollback()


async def orm_search_win_id(session: AsyncSession, user_id: int, win_id: int):
    """
    Checks if a win_id exists in the winusers table and assigns it to a user in the User table.

    Args:
    session: An SQLAlchemy AsyncSession.
    user_id: The user's ID.
    win_id: The win ID to assign.

    Returns:
    True if the win_id was assigned successfully, False otherwise.
    """
    query = select(WinUser).filter(WinUser.user_id == win_id)
    result = await session.execute(query)
    win_user = result.scalar_one_or_none()

    if win_id == 121212:
        print("ТЕСТОВЫЙ АЙДИ")
        # Check if user already has a win_id
        user_query = select(User).filter(User.user_id == user_id)
        user_result = await session.execute(user_query)
        user = user_result.scalar_one_or_none()

        update_query = update(User).where(User.user_id == user_id).values(win_id=win_id)
        await session.execute(update_query)
        await session.commit()
        return True
    
    else:
        # win_id not found in winusers
        return False
    

async def orm_check_id(session: AsyncSession, user_id: int):
    query = select(User.win_id).filter(User.user_id == user_id)
    result = await session.execute(query)
    win_user = result.scalar_one_or_none()
    return win_user


async def orm_user_data(session: AsyncSession, user_id: int):
    query = select(User.last_send_time, User.sent_images).where(User.user_id == user_id)

    try:
        result = await session.execute(query)
        user_data = result.all()
        print(f"ORM - USER_DATA - ", user_data)
        if user_data is not None:
            (last_sent_time, sent_images) = user_data[0]
            # Handle the case where sent_images might be None
            if sent_images is not None:
                sent_images = json.loads(sent_images) # Decode only if not None
            else:
                sent_images = [] # Initialize as an empty list if None
        else:
            last_sent_time = datetime.datetime.now() - datetime.timedelta(seconds=30)
            sent_images = [] # Initialize as an empty list if no user found
        return last_sent_time, sent_images
    except sqlalchemy.exc.NoResultFound:
        print(f"No user found with id: {user_id}")
        return None, None
    except Exception as e:
        print(f"An error occurred during data retrieval: {e}")
        return datetime.datetime.now() - datetime.timedelta(seconds=30), []



async def orm_update_data(session: AsyncSession, user_id: int, last_sent_time: datetime.datetime, sent_images):
    query = update(User).where(User.user_id == user_id).values(
        last_send_time = last_sent_time,
        sent_images = sent_images
    )
    await session.execute(query)
    await session.commit()
    
    

# async def orm_save_message(session: AsyncSession, user_id: int, role: str, message: str, tokens: int):
#     new_message = Message(
#         user_id=user_id,
#         role=role,
#         content=message,
#         tokens=tokens
#     )
#     session.add(new_message)
#     await session.commit()


# async def orm_delete_message(session: AsyncSession, message_id: int):
#     await session.execute(delete(Message).where(Message.id == message_id))
#     await session.commit()


# async def orm_delete_messages(session: AsyncSession, user_id: int):
#     # Проверяем, есть ли сообщения с таким user_id
#     result = await session.execute(select(Message).filter(Message.user_id == user_id))
#     messages = result.scalars().all()

#     if messages:
#         # Если сообщения найдены, выполняем удаление
#         await session.execute(delete(Message).filter(Message.user_id == user_id))
#         await session.commit()
#         print(f"Удалено {len(messages)} сообщений.")
#     else:
#         print("Сообщения с таким user_id не найдены.")


# async def orm_get_messages(session: AsyncSession, user_id: int) -> List[Tuple[int, str, str, int]]:
#     result = await session.execute(select(Message).where(Message.user_id == user_id))
#     messages = result.scalars().all()
#     return [(msg.id, msg.role, msg.content, msg.tokens) for msg in messages]
