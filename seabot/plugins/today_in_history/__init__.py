from nonebot.rule import T_State, to_me
from nonebot import on_command, require, get_driver, get_bot
from nonebot.adapters.cqhttp import Bot, GroupMessageEvent, Message
from .config import Config
from .data_source import get_todaybefore

driver = get_driver()
global_config = driver.config
config = Config(**global_config.dict())
nickname = list(global_config.nickname)[0]
admin = list(global_config.superusers)[0]
scheduler = require("nonebot_plugin_apscheduler").scheduler
todaybefore = on_command("历史上的今天", rule=to_me(), priority=7, aliases={"历史"}, block=True)


async def todaybefore_reminder():
    bot = get_bot()
    data = await get_todaybefore()
    for i in config.todaybefore_reminder_groups:
        msg = f"「{nickname}·历史上的今天·定时」\n{data}"
        await bot.call_api('send_group_msg', **{'group_id': i, 'message': Message(msg)})


@todaybefore.handle()
async def todaybefore_handle(bot: Bot, event: GroupMessageEvent, state: T_State):
    data = await get_todaybefore()
    msg = f"「{nickname}·历史上的今天」\n[CQ:at,qq={event.get_user_id()}]\n{data}"
    await todaybefore.finish(Message(msg))


@driver.on_startup
async def _():
    if config.todaybefore_reminder_start:
        for i in range(len(config.todaybefore_reminder_time)):
            temp = config.todaybefore_reminder_time[i].split(":")
            hour = int(temp[0])
            minute = int(temp[1])
            scheduler.add_job(todaybefore_reminder, 'cron', hour=hour, minute=minute, id=f"todaybefore_reminder_{i}")
