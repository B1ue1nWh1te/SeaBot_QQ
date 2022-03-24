import aiohttp
import asyncio

Headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"}


async def get_total_epidemic_data() -> str:
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://c.m.163.com/ug/api/wuhan/app/data/list-total", headers=Headers, timeout=5) as response:
                RawData = await response.json()
                Temp = RawData["data"]["areaTree"]
                for i in range(len(Temp)):
                    if Temp[i]["name"] == "中国":
                        Temp = Temp[i]
                        break
                Today = Temp["today"]
                Total = Temp["total"]
                TodayConfirm = Today["confirm"]
                TodayHeal = Today["heal"]
                TodayHave = Total["confirm"] - Total["heal"] - Total["dead"]
                UpdateTime = Temp["lastUpdateTime"]
                Data = f"[全国疫情数据]\n[数据更新时间]{UpdateTime}\n[今日新增确诊]{TodayConfirm}\n[今日新增治愈]{TodayHeal}\n[现有确诊总数]{TodayHave}"
                return Data
    except:
        return "获取信息失败"


async def get_city_epidemic_data(province: str, city: str) -> str:
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://c.m.163.com/ug/api/wuhan/app/data/list-total", headers=Headers, timeout=5) as response:
                RawData = await response.json()
                Temp = RawData["data"]["areaTree"]
                for i in range(len(Temp)):
                    if Temp[i]["name"] == "中国":
                        Temp = Temp[i]["children"]
                        break
                for i in range(len(Temp)):
                    if Temp[i]["name"] == province:
                        Temp = Temp[i]["children"]
                        break
                for i in range(len(Temp)):
                    if Temp[i]["name"] == city:
                        Temp = Temp[i]
                        break
                Today = Temp["today"]
                Total = Temp["total"]
                TodayConfirm = Today["confirm"]
                TodayHave = Total["confirm"] - Total["heal"] - Total["dead"]
                UpdateTime = Temp["lastUpdateTime"]
                Data = f"[{province}-{city} 疫情数据]\n[数据更新时间]{UpdateTime}\n[今日新增确诊]{TodayConfirm}\n[现有确诊总数]{TodayHave}"
                return Data
    except:
        return "获取信息失败"
