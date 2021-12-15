from nonebot.rule import T_State, to_me
from nonebot import on_command, require, get_driver, get_bot
from nonebot.adapters.cqhttp import Bot, GroupMessageEvent, Message
from .config import Config
from .data_source import get_time, get_weibo, get_weibo_detail, get_zhihu, get_zhihu_detail, get_cctv, get_cctv_detail, get_tonghuashun, get_tonghuashun_detail

driver = get_driver()
global_config = driver.config
config = Config(**global_config.dict())
groups = list(global_config.group_id)
nickname = list(global_config.nickname)[0]
admins = list(global_config.superusers)
scheduler = require("nonebot_plugin_apscheduler").scheduler
weibo = on_command("微博热搜", rule=to_me(), priority=2, aliases={"微博"})
zhihu = on_command("知乎热榜", rule=to_me(), priority=3, aliases={"知乎"})
cctv = on_command("央视新闻", rule=to_me(), priority=4, aliases={"新闻"})
tonghuashun = on_command("同花顺快讯", rule=to_me(), priority=5, aliases={"同花顺"})


async def weibo_reminder():
    now = get_time()
    bot = get_bot()
    data = await get_weibo(config.weibo_amount)
    for i in range(len(groups)):
        msg = f"「{nickname}·微博热搜·定时」\n\n[{now}][CQ:at,qq={admins[i]}]\n{data}"
        await bot.call_api('send_group_msg', **{'group_id': groups[i], 'message': Message(msg)})


async def zhihu_reminder():
    now = get_time()
    bot = get_bot()
    data = await get_zhihu(config.zhihu_amount)
    for i in range(len(groups)):
        msg = f"「{nickname}·知乎热榜·定时」\n\n[{now}][CQ:at,qq={admins[i]}]\n{data}"
        await bot.call_api('send_group_msg', **{'group_id': groups[i], 'message': Message(msg)})


async def cctv_reminder():
    now = get_time()
    bot = get_bot()
    data = await get_cctv(config.cctv_amount)
    for i in range(len(groups)):
        msg = f"「{nickname}·央视新闻·定时」\n\n[{now}][CQ:at,qq={admins[i]}]\n{data}"
        await bot.call_api('send_group_msg', **{'group_id': groups[i], 'message': Message(msg)})


async def tonghuashun_reminder():
    now = get_time()
    bot = get_bot()
    data = await get_tonghuashun(config.tonghuashun_amount)
    for i in range(len(groups)):
        msg = f"「{nickname}·同花顺快讯·定时」\n\n[{now}][CQ:at,qq={admins[i]}]\n{data}"
        await bot.call_api('send_group_msg', **{'group_id': groups[i], 'message': Message(msg)})


@weibo.handle()
async def weibo_handle(bot: Bot, event: GroupMessageEvent, state: T_State):
    args = event.get_plaintext()
    if args:
        state["number"] = args.split(",")
        for i in range(len(state["number"])):
            msg = await get_weibo_detail(int(state["number"][i]) - 1)
            if i != len(state["number"]) - 1:
                await weibo.send(Message(msg))
            else:
                await weibo.finish(Message(msg))
    else:
        now = get_time()
        data = await get_weibo(config.weibo_amount)
        msg = f"「{nickname}·微博热搜」[CQ:at,qq={event.get_user_id()}]\n\n[{now}]\n{data}"
        await weibo.send(Message(msg))


@weibo.got("number")
async def weibo_got(bot: Bot, event: GroupMessageEvent, state: T_State):
    if "详情-" in state["number"]:
        number = state["number"][3:]
        if len(number) != 0:
            number = number.split(",")
            now = get_time()
            for i in range(len(number)):
                msg = await get_weibo_detail(int(number[i]) - 1)
                if i != len(number) - 1:
                    await weibo.send(Message(msg))
                else:
                    await weibo.finish(Message(msg))


@zhihu.handle()
async def zhihu_handle(bot: Bot, event: GroupMessageEvent, state: T_State):
    args = event.get_plaintext()
    if args:
        state["number"] = args.split(",")
        for i in range(len(state["number"])):
            msg = await get_zhihu_detail(int(state["number"][i]) - 1)
            if i != len(state["number"]) - 1:
                await zhihu.send(Message(msg))
            else:
                await zhihu.finish(Message(msg))
    else:
        now = get_time()
        data = await get_zhihu(config.zhihu_amount)
        msg = f"「{nickname}·知乎热搜」[CQ:at,qq={event.get_user_id()}]\n\n[{now}]\n{data}"
        await zhihu.send(Message(msg))


@zhihu.got("number")
async def zhihu_got(bot: Bot, event: GroupMessageEvent, state: T_State):
    if "详情-" in state["number"]:
        number = state["number"][3:]
        if len(number) != 0:
            number = number.split(",")
            now = get_time()
            for i in range(len(number)):
                msg = await get_zhihu_detail(int(number[i]) - 1)
                if i != len(number) - 1:
                    await zhihu.send(Message(msg))
                else:
                    await zhihu.finish(Message(msg))


@cctv.handle()
async def cctv_handle(bot: Bot, event: GroupMessageEvent, state: T_State):
    args = event.get_plaintext()
    if args:
        state["number"] = args.split(",")
        for i in range(len(state["number"])):
            msg = await get_cctv_detail(int(state["number"][i]) - 1)
            if i != len(state["number"]) - 1:
                await cctv.send(Message(msg))
            else:
                await cctv.finish(Message(msg))
    else:
        now = get_time()
        data = await get_cctv(config.cctv_amount)
        msg = f"「{nickname}·央视新闻」[CQ:at,qq={event.get_user_id()}]\n\n[{now}]\n{data}"
        await cctv.send(Message(msg))


@cctv.got("number")
async def cctv_got(bot: Bot, event: GroupMessageEvent, state: T_State):
    if "详情-" in state["number"]:
        number = state["number"][3:]
        if len(number) != 0:
            number = number.split(",")
            now = get_time()
            for i in range(len(number)):
                msg = await get_cctv_detail(int(number[i]) - 1)
                if i != len(number) - 1:
                    await cctv.send(Message(msg))
                else:
                    await cctv.finish(Message(msg))


@tonghuashun.handle()
async def tonghuashun_handle(bot: Bot, event: GroupMessageEvent, state: T_State):
    args = event.get_plaintext()
    if args:
        state["number"] = args.split(",")
        for i in range(len(state["number"])):
            msg = await get_tonghuashun_detail(int(state["number"][i]) - 1)
            if i != len(state["number"]) - 1:
                await tonghuashun.send(Message(msg))
            else:
                await tonghuashun.finish(Message(msg))
    else:
        now = get_time()
        data = await get_tonghuashun(config.tonghuashun_amount)
        msg = f"「{nickname}·同花顺快讯」[CQ:at,qq={event.get_user_id()}]\n\n[{now}]\n{data}"
        await tonghuashun.send(Message(msg))


@tonghuashun.got("number")
async def tonghuashun_got(bot: Bot, event: GroupMessageEvent, state: T_State):
    if "详情-" in state["number"]:
        number = state["number"][3:]
        if len(number) != 0:
            number = number.split(",")
            now = get_time()
            for i in range(len(number)):
                msg = await get_tonghuashun_detail(int(number[i]) - 1)
                if i != len(number) - 1:
                    await tonghuashun.send(Message(msg))
                else:
                    await tonghuashun.finish(Message(msg))


@driver.on_startup
async def _():
    for i in range(len(config.weibo_reminder_time_hours)):
        scheduler.add_job(weibo_reminder, 'cron', hour=config.weibo_reminder_time_hours[i],
                          minute=config.weibo_reminder_time_minutes[i], id=f"weibo_reminder_{i}")
    for i in range(len(config.zhihu_reminder_time_hours)):
        scheduler.add_job(zhihu_reminder, 'cron', hour=config.zhihu_reminder_time_hours[i],
                          minute=config.zhihu_reminder_time_minutes[i], id=f"zhihu_reminder_{i}")
    for i in range(len(config.cctv_reminder_time_hours)):
        scheduler.add_job(cctv_reminder, 'cron', hour=config.cctv_reminder_time_hours[i],
                          minute=config.cctv_reminder_time_minutes[i], id=f"cctv_reminder_{i}")
    for i in range(len(config.tonghuashun_reminder_time_hours)):
        scheduler.add_job(tonghuashun_reminder, 'cron', hour=config.tonghuashun_reminder_time_hours[i],
                          minute=config.tonghuashun_reminder_time_minutes[i], id=f"tonghuashun_reminder_{i}")
