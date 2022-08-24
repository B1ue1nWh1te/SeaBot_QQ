from nonebot import require, get_driver, get_bot
from nonebot.adapters.cqhttp import Message
from .config import Config
from .data_source import get_weather, get_saying

driver = get_driver()
global_config = driver.config
config = Config(**global_config.dict())
nickname = list(global_config.nickname)[0]
admin = list(global_config.superusers)[0]
scheduler = require("nonebot_plugin_apscheduler").scheduler


async def card_reminder(city):
    bot = get_bot()
    weather = await get_weather(city)
    saying = await get_saying()
    for i in config.card_reminder_groups:
        msg = f"「{nickname}·天气丨一言」\n\n[{city}天气]{weather}\n[一言]{saying}"
        await bot.call_api('send_group_msg', **{'group_id': i, 'message': Message(msg)})


@driver.on_startup
async def _():
    if config.card_reminder_start:
        for i in range(len(config.card_reminder_time)):
            temp = config.card_reminder_time[i].split(":")
            hour = int(temp[0])
            minute = int(temp[1])
            scheduler.add_job(card_reminder, 'cron', hour=hour, minute=minute, id=f"card_reminder_{i}", args=[config.card_weather_city])
