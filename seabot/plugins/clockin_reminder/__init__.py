from nonebot.rule import T_State
from nonebot import on_command, require, get_driver, get_bot
from nonebot.permission import SUPERUSER
from nonebot.adapters.cqhttp import Bot, GroupMessageEvent, Message
from .config import Config

driver = get_driver()
global_config = driver.config
config = Config(**global_config.dict())
nickname = list(global_config.nickname)[0]
admin = list(global_config.superusers)[0]
scheduler = require("nonebot_plugin_apscheduler").scheduler
clockin = on_command("打卡提醒", permission=SUPERUSER, priority=1, block=True)


async def clockin_reminder(content):
    bot = get_bot()
    # 若消息风控，添加[CQ:at,qq={admin}]绕过
    msg = f"「{nickname}·打卡提醒」\n[CQ:at,qq=all]\n\n{content}"
    for i in config.clockin_reminder_groups:
        await bot.call_api('send_group_msg', **{'group_id': i, 'message': Message(msg)})


@clockin.handle()
async def clockin_handle(bot: Bot, event: GroupMessageEvent, state: T_State):
    content = config.clockin_reminder_contents[-1]
    msg = f"「{nickname}·打卡提醒」\n[CQ:at,qq={event.get_user_id()}]\n\n{content}"
    await clockin.finish(Message(msg))


@driver.on_startup
async def _():
    if config.clockin_reminder_start:
        assert(len(config.clockin_reminder_time) == len(config.clockin_reminder_contents))
        for i in range(len(config.clockin_reminder_contents)):
            temp = config.clockin_reminder_time[i].split(":")
            hour = int(temp[0])
            minute = int(temp[1])
            scheduler.add_job(clockin_reminder, 'cron', hour=hour, minute=minute, id=f"clockin_reminder_{i}", args=[config.clockin_reminder_contents[i]])
