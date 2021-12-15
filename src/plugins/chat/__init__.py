from nonebot.rule import T_State, to_me
from nonebot import on_message
from nonebot.adapters.cqhttp import Bot, GroupMessageEvent, Message
import random

keyword = on_message(rule=to_me(), priority=10)


@keyword.handle()
async def keyword_handle(bot: Bot, event: GroupMessageEvent, state: T_State):
    if event.get_plaintext() == "":
        await keyword.finish(Message(random.choice([
            "?", "怎么说", "[CQ:face,id=277]"
        ])))
