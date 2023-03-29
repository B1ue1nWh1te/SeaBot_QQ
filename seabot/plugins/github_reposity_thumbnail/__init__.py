from nonebot import on_message
from nonebot.rule import T_State
from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent, Message
from .data_source import get_github_reposity_information
import re

github = on_message(priority=10, block=True)


@github.handle()
async def github_handle(bot: Bot, event: GroupMessageEvent, state: T_State):
    url = event.get_plaintext()
    if re.match("https://github.com/.*?/.*?", url) != None:
        imageUrl = await get_github_reposity_information(url)
        if imageUrl != "获取信息失败":
            await github.send(Message(f"[CQ:image,file={imageUrl}]"))
            await github.finish(Message(f"[CQ:image,file=https://image.thum.io/get/width/1280/crop/1440/viewportWidth/1280/png/noanimate/{url}]"))
