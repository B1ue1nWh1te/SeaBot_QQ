import nonebot
from nonebot.adapters.onebot.v11 import Adapter as ONEBOT_V11Adapter

nonebot.init()
app = nonebot.get_asgi()
driver = nonebot.get_driver()
driver.register_adapter(ONEBOT_V11Adapter)
nonebot.load_builtin_plugins()
nonebot.load_from_json("plugins.json")

if __name__ == "__main__":
    nonebot.run(app="__mp_main__:app")
