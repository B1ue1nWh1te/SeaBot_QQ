from nonebot import on_command, require, get_driver, get_bot
from nonebot.rule import T_State, to_me
from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent, Message
from .config import Config
from .data_source import get_leetcode_daily

driver = get_driver()
global_config = driver.config
config = Config(**global_config.dict())
nickname = list(global_config.nickname)[0]
scheduler = require("nonebot_plugin_apscheduler").scheduler
leetcode = on_command("每日算法", rule=to_me(), priority=6, aliases={"算法"}, block=True)


async def leetcode_reminder():
    bot = get_bot()
    data = await get_leetcode_daily()
    if data != "获取信息失败":
        for i in config.leetcode_reminder_groups:
            msg = f"「{nickname}·每日算法·定时」\n[链接]{data['url']}\n[题目]{data['id']}.{data['title']}\n[难度]{data['difficulty']}\n[描述内容]\n{data['content']}"
            await bot.call_api('send_group_msg', **{'group_id': i, 'message': Message(msg)})
    else:
        for i in config.leetcode_reminder_groups:
            msg = f"「{nickname}·每日算法·定时」\n获取信息失败"
            await bot.call_api('send_group_msg', **{'group_id': i, 'message': Message(msg)})


@leetcode.handle()
async def leetcode_handle(bot: Bot, event: GroupMessageEvent, state: T_State):
    data = await get_leetcode_daily()
    if data != "获取信息失败":
        msg = f"「{nickname}·每日算法」\n[CQ:at,qq={event.get_user_id()}]\n[链接]{data['url']}\n[题目]{data['id']}.{data['title']}\n[难度]{data['difficulty']}\n[描述内容]\n{data['content']}"
        await leetcode.finish(Message(msg))
    else:
        msg = f"「{nickname}·每日算法」\n[CQ:at,qq={event.get_user_id()}]\n获取信息失败"
        await leetcode.finish(Message(msg))


@driver.on_startup
async def _():
    if config.leetcode_reminder_start:
        for i in range(len(config.leetcode_reminder_time)):
            temp = config.leetcode_reminder_time[i].split(":")
            hour = int(temp[0])
            minute = int(temp[1])
            scheduler.add_job(leetcode_reminder, 'cron', hour=hour, minute=minute, id=f"leetcode_reminder_{i}")
