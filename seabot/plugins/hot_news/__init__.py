from nonebot import on_command, require, get_driver, get_bot
from nonebot.rule import T_State, to_me
from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent, Message
from .config import Config
from .data_source import *

driver = get_driver()
global_config = driver.config
config = Config(**global_config.dict())
nickname = list(global_config.nickname)[0]
scheduler = require("nonebot_plugin_apscheduler").scheduler
weibo = on_command("微博热搜", rule=to_me(), priority=2, aliases={"微博"}, block=True)
zhihu = on_command("知乎热榜", rule=to_me(), priority=3, aliases={"知乎"}, block=True)
cctv = on_command("央视新闻", rule=to_me(), priority=4, aliases={"新闻"}, block=True)
tonghuashun = on_command("同花顺快讯", rule=to_me(), priority=5, aliases={"同花顺"}, block=True)


async def weibo_reminder():
    now = get_time()
    bot = get_bot()
    data = await get_weibo(config.weibo_amount)
    for i in config.weibo_reminder_groups:
        msg = f"「{nickname}·微博热搜·定时」\n[{now}]\n{data}"
        await bot.call_api('send_group_msg', **{'group_id': i, 'message': Message(msg)})


async def zhihu_reminder():
    now = get_time()
    bot = get_bot()
    data = await get_zhihu(config.zhihu_amount)
    for i in config.zhihu_reminder_groups:
        msg = f"「{nickname}·知乎热榜·定时」\n[{now}]\n{data}"
        await bot.call_api('send_group_msg', **{'group_id': i, 'message': Message(msg)})


async def cctv_reminder():
    now = get_time()
    bot = get_bot()
    data = await get_cctv(config.cctv_amount)
    for i in config.cctv_reminder_groups:
        msg = f"「{nickname}·央视新闻·定时」\n[{now}]\n{data}"
        await bot.call_api('send_group_msg', **{'group_id': i, 'message': Message(msg)})


async def tonghuashun_reminder():
    now = get_time()
    bot = get_bot()
    data = await get_tonghuashun(config.tonghuashun_amount)
    for i in config.tonghuashun_reminder_groups:
        msg = f"「{nickname}·同花顺快讯·定时」\n[{now}]\n{data}"
        await bot.call_api('send_group_msg', **{'group_id': i, 'message': Message(msg)})


@weibo.handle()
async def weibo_handle(bot: Bot, event: GroupMessageEvent, state: T_State):
    now = get_time()
    data = await get_weibo(config.weibo_amount)
    msg = f"「{nickname}·微博热搜」\n[CQ:at,qq={event.get_user_id()}]\n[{now}]\n{data}"
    await weibo.finish(Message(msg))


@zhihu.handle()
async def zhihu_handle(bot: Bot, event: GroupMessageEvent, state: T_State):
    now = get_time()
    data = await get_zhihu(config.zhihu_amount)
    msg = f"「{nickname}·知乎热搜」\n[CQ:at,qq={event.get_user_id()}]\n[{now}]\n{data}"
    await zhihu.finish(Message(msg))


@cctv.handle()
async def cctv_handle(bot: Bot, event: GroupMessageEvent, state: T_State):
    now = get_time()
    data = await get_cctv(config.cctv_amount)
    msg = f"「{nickname}·央视新闻」\n[CQ:at,qq={event.get_user_id()}]\n[{now}]\n{data}"
    await cctv.finish(Message(msg))


@tonghuashun.handle()
async def tonghuashun_handle(bot: Bot, event: GroupMessageEvent, state: T_State):
    now = get_time()
    data = await get_tonghuashun(config.tonghuashun_amount)
    msg = f"「{nickname}·同花顺快讯」\n[CQ:at,qq={event.get_user_id()}]\n[{now}]\n{data}"
    await tonghuashun.finish(Message(msg))


@driver.on_startup
async def _():
    if config.weibo_reminder_start:
        for i in range(len(config.weibo_reminder_time)):
            temp = config.weibo_reminder_time[i].split(":")
            hour = int(temp[0])
            minute = int(temp[1])
            scheduler.add_job(weibo_reminder, 'cron', hour=hour, minute=minute, id=f"weibo_reminder_{i}")
    if config.zhihu_reminder_start:
        for i in range(len(config.zhihu_reminder_time)):
            temp = config.zhihu_reminder_time[i].split(":")
            hour = int(temp[0])
            minute = int(temp[1])
            scheduler.add_job(zhihu_reminder, 'cron', hour=hour, minute=minute, id=f"zhihu_reminder_{i}")
    if config.cctv_reminder_start:
        for i in range(len(config.cctv_reminder_time)):
            temp = config.cctv_reminder_time[i].split(":")
            hour = int(temp[0])
            minute = int(temp[1])
            scheduler.add_job(cctv_reminder, 'cron', hour=hour, minute=minute, id=f"cctv_reminder_{i}")
    if config.tonghuashun_reminder_start:
        for i in range(len(config.tonghuashun_reminder_time)):
            temp = config.tonghuashun_reminder_time[i].split(":")
            hour = int(temp[0])
            minute = int(temp[1])
            scheduler.add_job(tonghuashun_reminder, 'cron', hour=hour, minute=minute, id=f"tonghuashun_reminder_{i}")
