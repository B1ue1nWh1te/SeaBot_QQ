from nonebot.rule import T_State
from nonebot import on_command, require, get_driver, get_bot
from nonebot.permission import SUPERUSER
from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent, Message
from .config import Config

driver = get_driver()
global_config = driver.config
config = Config(**global_config.dict())
nickname = list(global_config.nickname)[0]
admin = list(global_config.superusers)[0]
scheduler = require("nonebot_plugin_apscheduler").scheduler
timing = on_command("定时提醒", permission=SUPERUSER, priority=1, block=True)


async def timing_reminder(content):
    bot = get_bot()
    # 若消息风控，添加[CQ:at,qq={admin}]绕过
    msg = f"「{nickname}·定时提醒」\n[CQ:at,qq=all]\n\n{content}"
    for i in config.timing_reminder_groups:
        await bot.call_api('send_group_msg', **{'group_id': i, 'message': Message(msg)})


@timing.handle()
async def timing_handle(bot: Bot, event: GroupMessageEvent, state: T_State):
    content = config.timing_reminder_contents[-1]
    msg = f"「{nickname}·定时提醒」\n[CQ:at,qq={event.get_user_id()}]\n\n{content}"
    await timing.finish(Message(msg))


@driver.on_startup
async def _():
    if config.timing_reminder_start:
        assert(len(config.timing_reminder_time) == len(config.timing_reminder_contents))
        for i in range(len(config.timing_reminder_contents)):
            temp = config.timing_reminder_time[i].split(":")
            hour = int(temp[0])
            minute = int(temp[1])
            scheduler.add_job(timing_reminder, 'cron', hour=hour, minute=minute, id=f"timing_reminder_{i}", args=[config.timing_reminder_contents[i]])
