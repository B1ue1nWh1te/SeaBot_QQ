from nonebot.rule import T_State
from nonebot import on_command, require, get_driver, get_bot
from nonebot.permission import SUPERUSER
from nonebot.adapters.cqhttp import Bot, GroupMessageEvent, Message
from .config import Config
from .data_source import get_weather, get_saying

global_config = get_driver().config
config = Config(**global_config.dict())
groups = list(global_config.group_id)
nickname = list(global_config.nickname)[0]
admins = list(global_config.superusers)

scheduler = require("nonebot_plugin_apscheduler").scheduler
clockin = on_command("打卡提醒", permission=SUPERUSER, priority=1)


@scheduler.scheduled_job("cron", hour=config.reminder_time_hours[0], minute=config.reminder_time_minutes[0], id="before_sleep", args=[config.first_content, config.weather_city])
async def clockin_reminder1(content, city):
    bot = get_bot()
    weather = await get_weather(city)
    saying = await get_saying()
    # 若消息风控，添加[CQ:at,qq={list(global_config.superusers)[0]}]绕过
    for i in range(len(groups)):
        msg = f"「{nickname}·打卡提醒·定时」\n\n{content}\n[{city}天气]{weather}\n\n[每日一句]{saying}\n[CQ:at,qq={admins[i]}]\n[CQ:at,qq=all]"
        await bot.call_api('send_group_msg', **{'group_id': groups[i], 'message': msg})


@scheduler.scheduled_job("cron", hour=config.reminder_time_hours[1], minute=config.reminder_time_minutes[1], id="after_wakeup", args=[config.second_content, config.weather_city])
async def clockin_reminder2(content, city):
    bot = get_bot()
    weather = await get_weather(city)
    saying = await get_saying()
    for i in range(len(groups)):
        msg = f"「{nickname}·打卡提醒·定时」\n\n{content}\n[{city}天气]{weather}\n\n[每日一句]{saying}\n[CQ:at,qq={admins[i]}]\n[CQ:at,qq=all]"
        await bot.call_api('send_group_msg', **{'group_id': groups[i], 'message': msg})


@clockin.handle()
async def clockin_handle(bot: Bot, event: GroupMessageEvent, state: T_State):
    bot = get_bot()
    content = config.second_content
    weather = await get_weather(config.weather_city)
    saying = await get_saying()
    msg = f"「{nickname}·打卡提醒」[CQ:at,qq={event.get_user_id()}]\n\n{content}\n[{config.weather_city}天气]{weather}\n\n[每日一句]{saying}"
    await clockin.finish(Message(msg))
