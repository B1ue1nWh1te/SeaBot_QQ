from nonebot.rule import T_State, to_me
from nonebot import on_command, require, get_driver, get_bot
from nonebot.adapters.cqhttp import Bot, GroupMessageEvent, Message
from .config import Config
from .data_source import get_total_epidemic_data, get_city_epidemic_data

driver = get_driver()
global_config = driver.config
config = Config(**global_config.dict())
nickname = list(global_config.nickname)[0]
scheduler = require("nonebot_plugin_apscheduler").scheduler
epidemic_data = on_command("疫情数据", rule=to_me(), priority=8, block=True)


async def epidemic_data_reminder(province, city):
    bot = get_bot()
    total_data = await get_total_epidemic_data()
    city_data = await get_city_epidemic_data(province, city)
    for i in config.epidemic_data_reminder_groups:
        msg = f"「{nickname}·疫情数据」\n\n{total_data}\n\n{city_data}"
        await bot.call_api('send_group_msg', **{'group_id': i, 'message': Message(msg)})


@epidemic_data.handle()
async def epidemic_data_handle(bot: Bot, event: GroupMessageEvent, state: T_State):
    args = event.get_plaintext()
    temp = args.split("-")
    province = temp[0]
    city = temp[1]
    total_data = await get_total_epidemic_data()
    city_data = await get_city_epidemic_data(province, city)
    msg = f"「{nickname}·疫情数据」\n[CQ:at,qq={event.get_user_id()}]\n\n{total_data}\n\n{city_data}"
    await epidemic_data.finish(Message(msg))


@driver.on_startup
async def _():
    if config.epidemic_data_reminder_start:
        for i in range(len(config.epidemic_data_reminder_time)):
            temp = config.epidemic_data_reminder_time[i].split(":")
            hour = int(temp[0])
            minute = int(temp[1])
            scheduler.add_job(epidemic_data_reminder, 'cron', hour=hour, minute=minute, id=f"epidemic_data_reminder_{i}", args=[config.epidemic_data_province, config.epidemic_data_city])
