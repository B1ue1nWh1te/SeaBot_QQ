from nonebot.rule import T_State, to_me
from nonebot import on_command, require, get_driver, get_bot
from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent, Message
from .config import Config
from .data_source import get_saying

driver = get_driver()
global_config = driver.config
config = Config(**global_config.dict())
nickname = list(global_config.nickname)[0]
scheduler = require("nonebot_plugin_apscheduler").scheduler
yiyan = on_command("一言", rule=to_me(), priority=7, block=True)


async def yiyan_reminder():
    bot = get_bot()
    saying = await get_saying()
    for i in config.yiyan_reminder_groups:
        msg = f"「{nickname}·一言」\n{saying}"
        await bot.call_api('send_group_msg', **{'group_id': i, 'message': Message(msg)})


@yiyan.handle()
async def yiyan_handle(bot: Bot, event: GroupMessageEvent, state: T_State):
    saying = await get_saying()
    msg = f"「{nickname}·一言」\n[CQ:at,qq={event.get_user_id()}]\n{saying}"
    await yiyan.finish(Message(msg))


@driver.on_startup
async def _():
    if config.yiyan_reminder_start:
        for i in range(len(config.yiyan_reminder_time)):
            temp = config.yiyan_reminder_time[i].split(":")
            hour = int(temp[0])
            minute = int(temp[1])
            scheduler.add_job(yiyan_reminder, 'cron', hour=hour, minute=minute, id=f"yiyan_reminder_{i}", args=[config.yiyan_weather_city])
