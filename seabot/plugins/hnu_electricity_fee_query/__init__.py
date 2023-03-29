from nonebot import on_command, get_driver
from nonebot.rule import T_State, to_me
from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent, Message
from .data_source import get_electricity_fee

global_config = get_driver().config
nickname = list(global_config.nickname)[0]
electricity = on_command("电费查询", rule=to_me(), priority=8, aliases={"电费"}, block=True)


@electricity.handle()
async def electricity_handle(bot: Bot, event: GroupMessageEvent, state: T_State):
    args = event.get_plaintext().split(" ")[-1].split("-")
    assert(len(args) == 3)
    balance = await get_electricity_fee(args[0], args[1], args[2])
    if balance == "获取信息失败":
        msg = f"「{nickname}·电费查询」\n[CQ:at,qq={event.get_user_id()}]\n获取信息失败"
        await electricity.finish(Message(msg))
    else:
        fee = f"{round(float(balance[:-1])*0.64,2)}元"
        msg = f"「{nickname}·电费查询」\n[CQ:at,qq={event.get_user_id()}]\n[{'-'.join(args)}]\n[剩余电量]{balance}\n[电费换算]{fee}"
        await electricity.finish(Message(msg))
