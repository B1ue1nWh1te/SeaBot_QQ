from nonebot.rule import T_State, to_me
from nonebot import on_command, require, get_driver, get_bot
from nonebot.adapters.cqhttp import Bot, GroupMessageEvent, Message
from .config import Config
from .data_source import get_todaybefore

global_config = get_driver().config
config = Config(**global_config.dict())
groups = list(global_config.group_id)
nickname = list(global_config.nickname)[0]
admins = list(global_config.superusers)

scheduler = require("nonebot_plugin_apscheduler").scheduler
todaybefore = on_command("历史上的今天", rule=to_me(), priority=6, aliases={"历史"})


@scheduler.scheduled_job("cron", hour=config.reminder_time_hour, minute=config.reminder_time_minute, id="todaybefore_reminder")
async def todaybefore_reminder():
    bot = get_bot()
    data = await get_todaybefore()
    for i in range(len(groups)):
        msg = f"「{nickname}·历史上的今天·定时」\n\n[CQ:at,qq={admins[i]}]\n{data}"
        await bot.call_api('send_group_msg', **{'group_id': groups[i], 'message': msg})


@todaybefore.handle()
async def todaybefore_handle(bot: Bot, event: GroupMessageEvent, state: T_State):
    data = await get_todaybefore()
    msg = f"「{nickname}·历史上的今天」[CQ:at,qq={event.get_user_id()}]\n\n{data}"
    await todaybefore.finish(Message(msg))
