import time
import json
import aiohttp
import asyncio

Headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"}


def get_time():
    return time.strftime("%m{}%d{} %H:%M:%S").format('月', '日')


async def get_weibo(amount: int):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://weibo.com/ajax/statuses/hot_band", headers=Headers, timeout=5) as response:
                RawData = await response.json()
                Result = RawData["data"]["band_list"]
                Top = f'[置顶]{RawData["data"]["hotgov"]["name"]}'
                Data = [Top]
                for i in range(amount):
                    Data.append(f'{i+1}.{Result[i]["note"]}')
                return "\n".join(Data)
    except:
        return "获取信息失败"


async def get_weibo_detail(number: int):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://weibo.com/ajax/statuses/hot_band", headers=Headers, timeout=5) as response:
                RawData = await response.json()
                Result = RawData["data"]["band_list"][number]
                Msg = f'[CQ:share,url=https://s.weibo.com/weibo?q=%23{Result["note"]}%23,title={Result["note"]}]'
                return Msg
    except:
        return "获取信息失败"


async def get_zhihu(amount: int):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.zhihu.com/topstory/hot-list", headers=Headers, timeout=5) as response:
                RawData = await response.json()
                Result = RawData["data"]
                Data = []
                for i in range(amount):
                    Data.append(f'{i+1}.{Result[i]["target"]["title"]}')
                return "\n".join(Data)
    except:
        return "获取信息失败"


async def get_zhihu_detail(number: int):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.zhihu.com/topstory/hot-list", headers=Headers, timeout=5) as response:
                RawData = await response.json()
                Result = RawData["data"]
                Msg = f'[CQ:share,url=https://www.zhihu.com/question/{Result[number]["target"]["id"]},title={Result[number]["target"]["title"]},image={Result[number]["children"][0]["thumbnail"]}]'
                return Msg
    except:
        return "获取信息失败"


async def get_cctv(amount: int):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://news.cctv.com/2019/07/gaiban/cmsdatainterface/page/news_1.jsonp", headers=Headers, timeout=5) as response:
                RawData = await response.text()
                RawData = RawData.strip("news()")
                Result = json.loads(RawData)["data"]["list"]
                Data = []
                for i in range(amount):
                    Data.append(f'{i+1}.{Result[i]["title"]}\n[{Result[i]["brief"]}]\n')
                return "\n".join(Data)
    except:
        return "获取信息失败"


async def get_cctv_detail(number: int):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://news.cctv.com/2019/07/gaiban/cmsdatainterface/page/news_1.jsonp", headers=Headers, timeout=5) as response:
                RawData = await response.text()
                RawData = RawData.strip("news()")
                Result = json.loads(RawData)["data"]["list"]
                Msg = f'[CQ:share,url={Result[number]["url"]},title={Result[number]["title"]},image={Result[number]["image"]}]'
                return Msg
    except:
        return "获取信息失败"


async def get_tonghuashun(amount: int):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://news.10jqka.com.cn/tapp/news/push/stock", headers=Headers, timeout=5) as response:
                RawData = await response.json()
                Result = RawData["data"]["list"]
                Data = []
                for i in range(amount):
                    Data.append(f'{i+1}.{Result[i]["title"]}\n[{Result[i]["digest"]}]\n')
                return "\n".join(Data)
    except:
        return "获取信息失败"


async def get_tonghuashun_detail(number: int):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://news.10jqka.com.cn/tapp/news/push/stock", headers=Headers, timeout=5) as response:
                RawData = await response.json()
                Result = RawData["data"]["list"]
                Msg = f'[CQ:share,url={Result[number]["url"]},title={Result[number]["title"]}]'
                return Msg
    except:
        return "获取信息失败"
