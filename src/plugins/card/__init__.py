from nonebot import require, get_driver, get_bot
from nonebot.adapters.cqhttp import Message
from .config import Config
from .data_source import get_weather, get_saying

driver = get_driver()
global_config = driver.config
config = Config(**global_config.dict())
groups = list(global_config.timing_group_id)
nickname = list(global_config.nickname)[0]
admin = list(global_config.superusers)[0]
scheduler = require("nonebot_plugin_apscheduler").scheduler


async def card_reminder(city):
    bot = get_bot()
    weather = await get_weather(city)
    saying = await get_saying()
    for i in groups:
        msg = f"「{nickname}·天气与句子」\n[CQ:at,qq={admin}]\n\n[{city}天气]{weather}\n[每日一句]{saying}"
        await bot.call_api('send_group_msg', **{'group_id': i, 'message': Message(msg)})


@driver.on_startup
async def _():
    scheduler.add_job(card_reminder, 'cron', hour=config.card_reminder_time_hours, minute=config.card_reminder_time_minutes, id="card_reminder", args=[config.card_weather_city])
