from nonebot.rule import T_State, to_me
from nonebot import on_message, get_driver
from nonebot.adapters.cqhttp import Bot, GroupMessageEvent, Message
import random

global_config = get_driver().config

keyword = on_message(rule=to_me(), priority=10)


@keyword.handle()
async def keyword_handle(bot: Bot, event: GroupMessageEvent, state: T_State):
    if str(event.get_plaintext()) == "":
        await keyword.finish(Message(random.choice([
            "?", "怎么说", "[CQ:face,id=277]"
        ])))
