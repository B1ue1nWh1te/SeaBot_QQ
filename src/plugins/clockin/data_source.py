import aiohttp
import asyncio

Headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"}


async def get_weather(city: str):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("http://wthrcdn.etouch.cn/weather_mini", params={"city": city}, headers=Headers, timeout=5) as response:
                WeatherDict = await response.text()
                WeatherDict = dict(eval(WeatherDict))["data"]["forecast"]
                WeatherDetail = "{} {}/{}".format(WeatherDict[0]["type"], WeatherDict[0]["high"].replace("高温 ", ""), WeatherDict[0]["low"].replace("低温 ", ""))
                return WeatherDetail
    except:
        return "获取信息失败"


async def get_saying():
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("http://open.iciba.com/dsapi/", headers=Headers, timeout=5) as response:
                Data = await response.text()
                Data = dict(eval(Data))
                Data = f'{Data["note"]}\n{Data["content"]}\n[CQ:image,file={Data["fenxiang_img"]}]'
                return Data
    except:
        return "获取信息失败"
