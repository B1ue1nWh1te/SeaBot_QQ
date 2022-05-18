from nonebot.rule import T_State, to_me
from nonebot import on_command, get_driver
from nonebot.adapters.cqhttp import Bot, GroupMessageEvent, Message
from .config import Config
from .data_source import get_electricity_fee

global_config = get_driver().config
config = Config(**global_config.dict())
nickname = list(global_config.nickname)[0]
electricity = on_command("电费查询", rule=to_me(), priority=6, aliases={"电费"}, block=True)


@electricity.handle()
async def electricity_handle(bot: Bot, event: GroupMessageEvent, state: T_State):
    args = event.get_plaintext()
    state["info"] = args.split("-")
    assert(len(state["info"]) == 3)
    balance = await get_electricity_fee(state["info"][0], state["info"][1], state["info"][2])
    if balance[-1] == "度":
        fee = f"{round(float(balance[:-1])*0.64,2)}元"
        msg = f"「{nickname}·电费查询」\n[CQ:at,qq={event.get_user_id()}]\n[{args}]\n[剩余电量]{balance}\n[电费换算]{fee}"
        await electricity.finish(Message(msg))
    else:
        msg = f"「{nickname}·电费查询」\n[CQ:at,qq={event.get_user_id()}]\n{balance}"
        await electricity.finish(Message(msg))
