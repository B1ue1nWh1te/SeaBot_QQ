import aiohttp
import asyncio

Headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"}


async def get_todaybefore() -> str:
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("http://www.ipip5.com/today/api.php", params={"type": "json"}, headers=Headers, timeout=5, verify_ssl=False) as response:
                RawData = await response.json(content_type=None)
                Today = RawData["today"]
                Result = RawData["result"][:-1]
                Data = []
                for i in Result:
                    Data.append(f'[{i["year"]}年{Today}]{i["title"]}')
                return "\n".join(Data)
    except:
        return "获取信息失败"
