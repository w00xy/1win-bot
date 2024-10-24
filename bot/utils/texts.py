import datetime
from random import randint, uniform
from config import REF_URL


start_text = (
    f"*Добро пожаловать в ISF Signal🚀*\n\n"
    f"● 1. Зарегистрируйтесь по ссылке на сайте [1WIN]({REF_URL})\n"
    f"● 2. После успешной регистрации cкопируйте ваш айди на сайте (Вкладка 'пополнение' и в правом верхнем углу будет ваш ID).\n"
    f"● *3. Отправьте ваш id боту для успешной регистрации*\n\n"
    f"Наш бот основан на нейросети от OpenAI. Он может предугадать расположение звёзд с вероятностью 85%."
)

async def no_reg_text(user_id):
    return (
        f"{user_id} ID не найден. Пожалуйста, введите ID еще раз:"
    )
    
success_reg_text = (
    f"Вы успешно прошли регистрацию✅\n\n"
)

instruction_text = (
    f"<b>ISF SIGNAL🚀</b>"
    f"Бот основан и обучен на кластере нейросети 🖥.\n"
    f"Для тренировки бота было сыграно 🎰10.000+ игр.\n\n"
    f"В данный момент пользователи бота успешно делают в день 15-25% от своего 💸 капитала!\n"
    f"Для получения максимального профита следуйте следующей инструкции:\n\n"
    f"🟢 <b>1. Пройти регистрацию в букмекерской конторе</b> <a href=\"{REF_URL}\">1WIN</a>\n"
    f"🟢 <b>2. Пополнить баланс своего аккаунта.</b>\n"
    f"🟢 <b>3. Перейти в раздел 1win games и выбрать игру</b> 💣'MINES'.\n"
    f"🟢 <b>4. Выставить кол-во ловушек в размере трёх. Это важно!</b>\n"
    f"🟢 <b>5. Запросить сигнал в боте и ставить по сигналам из бота.</b>\n"
    f"🟢 <b>6. При неудачном сигнале советуем удвоить(Х²) ставку что бы полностью перекрыть потерю при следующем сигнале.</b>"
)

async def wait_text(time_left):
    return (
        f"❗️ Пожалуйста, подождите {int(time_left.total_seconds()) + 1} секунд перед следующим запросом."
    )

generating_text = (
    f"📶 Генерация комбинации..."
)

async def get_signal_text():
    number = randint(13425, 124345)
    return (
        f"💣 Игра №{number}\n"
        f"🕓 {str(datetime.datetime.now().date()).replace('-', ' ')} {':'.join(str(datetime.datetime.now().time()).split(':')[:2])}\n\n"
        f"Шанс - {round(uniform(91.0, 98.0),2)}%"
    )
    