from __future__ import annotations
import logging
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from cardinal import Cardinal

from FunPayAPI.updater.events import NewMessageEvent
from FunPayAPI.common.enums import MessageTypes

# Метаданные плагина (эти значения обязательны)
NAME = "Мини GPT"
VERSION = "1.0"
DESCRIPTION = "Минимальный плагин для GPT консультанта"
CREDITS = "@your_username"
UUID = "mini_gpt_plugin_3213"
SETTINGS_PAGE = False

# Настройка логгера
logger = logging.getLogger("FPC.MiniGPT")
LOGGER_PREFIX = "[МиниGPT]"
logger.info(f"{LOGGER_PREFIX} Плагин загружен.")

def init(cardinal: Cardinal):
    """Инициализация плагина"""
    logger.info(f"{LOGGER_PREFIX} Плагин инициализирован!")
    
    # Добавляем команду в Telegram
    if cardinal.telegram:
        cardinal.add_telegram_commands(UUID, [
            ("mini_gpt", "тестовая команда GPT плагина", True)
        ])
        
        # Обработчик команды
        @cardinal.telegram.msg_handler(commands=["mini_gpt"])
        def mini_gpt_cmd(message):
            if message.from_user.id not in cardinal.telegram.authorized_users:
                return
            cardinal.telegram.bot.send_message(message.chat.id, "✅ Мини GPT плагин работает!")

def message_handler(cardinal: Cardinal, event: NewMessageEvent):
    """Обработчик сообщений"""
    # Получаем информацию о сообщении
    message = event.message
    text = message.text
    
    # Пропускаем системные сообщения
    if message.type != MessageTypes.NON_SYSTEM:
        return
    
    # Отвечаем на #minigpt
    if text and text.strip() == "#minigpt":
        cardinal.account.send_message(message.chat_id, "Привет! Я мини GPT консультант. Как я могу помочь?")

# Привязки к событиям
BIND_TO_PRE_INIT = [init]
BIND_TO_NEW_MESSAGE = [message_handler]
BIND_TO_DELETE = None 