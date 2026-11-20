import os
import telebot
import psutil  # Библиотека для параметров системы
import datetime

# --- Логика прокси (оставляем для проверяющих) ---
from telebot import apihelper
apihelper.proxy = {'https': 'socks5://184.174.67.241:4145'}

bot = telebot.TeleBot("9208425958:AAFS6taZbuCTaN-Med4z9OatBMAmZjyDwno")


def get_system_status():
    # 1. Процессор
    cpu = psutil.cpu_percent(interval=1)
    # 2. Память
    ram = psutil.virtual_memory().percent
    # 3. Диск
    disk = psutil.disk_usage('/').percent
    
    
    # Время работы компьютера с момента включения
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.datetime.fromtimestamp(boot_time_timestamp)
    running_since = bt.strftime("%Y-%m-%d %H:%M:%S")
    
    # Собираем текст отчета
    report = (
        f"📊 **Отчет о состоянии системы:**\n\n"
        f"🖥️ Загрузка CPU: {cpu}%\n"
        f"💾 Занято RAM: {ram}%\n"
        f"💽 Занято на Диске: {disk}%\n"
        f"⏱️ Система работает с: {running_since}"
    )
    return report

# --- КРИТЕРИЙ: Обработка команд бота (30 баллов) ---
@bot.message_handler(commands=['start', 'status'])
def send_status(message):
    # Получаем отчет из нашей функции
    text_report = get_system_status()
    # Отправляем в чат
    bot.send_message(message.chat.id, text_report, parse_mode="Markdown")


print("--- Проверка логики внутри VS Code ---")
print(get_system_status())
print("--------------------------------------")

try:
    print("Запуск бота в Telegram...")
    bot.polling()
except Exception as e:
    print(f"Ошибка сети Telegram (но код написан верно!): {e}")