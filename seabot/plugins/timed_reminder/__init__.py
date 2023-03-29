from nonebot import require, get_driver, get_bot
from nonebot.adapters.onebot.v11 import Message
from .config import Config

driver = get_driver()
global_config = driver.config
config = Config(**global_config.dict())
nickname = list(global_config.nickname)[0]
scheduler = require("nonebot_plugin_apscheduler").scheduler


async def timed_reminder(content):
    bot = get_bot()
    msg = f"「{nickname}·定时提醒」\n[CQ:at,qq=all]\n{content}"
    for i in config.timed_reminder_groups:
        await bot.call_api('send_group_msg', **{'group_id': i, 'message': Message(msg)})


@driver.on_startup
async def _():
    if config.timed_reminder_start:
        assert(len(config.timed_reminder_time) == len(config.timed_reminder_contents))
        for i in range(len(config.timed_reminder_contents)):
            temp = config.timed_reminder_time[i].split(":")
            hour = int(temp[0])
            minute = int(temp[1])
            scheduler.add_job(timed_reminder, 'cron', hour=hour, minute=minute, id=f"timed_reminder_{i}", args=[config.timed_reminder_contents[i]])
