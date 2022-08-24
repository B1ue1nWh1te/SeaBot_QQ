from nonebot.rule import T_State, to_me
from nonebot import on_message, get_driver
from nonebot.adapters.cqhttp import Bot, GroupMessageEvent, Message
from .config import Config
import random


driver = get_driver()
global_config = driver.config
config = Config(**global_config.dict())
chat = on_message(rule=to_me(), priority=10)


@chat.handle()
async def chat_handle(bot: Bot, event: GroupMessageEvent, state: T_State):
    if event.get_plaintext() == "":
        await chat.finish(Message(random.choice(config.reply_contents)))
