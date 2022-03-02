from nonebot.rule import T_State, to_me
from nonebot import on_message
from nonebot.adapters.cqhttp import Bot, GroupMessageEvent, Message
import random

chat = on_message(rule=to_me(), priority=10)


@chat.handle()
async def chat_handle(bot: Bot, event: GroupMessageEvent, state: T_State):
    if event.get_plaintext() == "":
        await chat.finish(Message(random.choice([
            "?", "怎么说", "[CQ:face,id=277]"
        ])))
